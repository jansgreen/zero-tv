
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from checkout.webhooks import my_webhook_view


from .forms import OrderForm
from catalog.models import Movies
from .models import order, OrderLineItem
from profiles.forms import UserProfileforms
from profiles.models import UserProfile
from django.contrib.auth.models import User
from bag.mymovies import my_movies
import stripe
import json
# This is your real test secret API key.


# THIS CODE COME FROM BOUTIQUE ADO, IT WAS MODIFIED TO FIT THIS PROJECT.
@require_POST
def cache_checkout(request):

    try:
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        the_bag = my_movies(request)
        total = the_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(amount=stripe_total, currency=settings.STRIPE_CURRENT)
        get_CS =  intent.client_secret.split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(get_CS, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
            })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'we can not processed your payment, please try again')
        return HttpResponse(content=e, status=400)
    

# Create your views here.
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
  
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'county': request.POST['county'],
            'postcade': request.POST['postcade'],
            'town_or_city': request.POST['town_or_city'],
            'street_address': request.POST['street_address'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST['client_secret_data'].split('_secret')[0]
            order.stripe_paid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for Movies_id, quantity in bag.items():

                try:
                    movie = Movies.objects.get(id= Movies_id)
                    if isinstance(quantity, int):
                        Order_Line = OrderLineItem(
                            order =order,
                            Movie = movie,
                            quantity = quantity,
                        )
                        Order_Line.save()
                        
                except Movies.DoesNotExist:
                    messages.error(request, " The movie not exist, the order will be cancel")
                    order.delete()
                    return redirect(reverse('bag'))
            the_bag = my_movies(request)
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('bag'))
        the_bag = my_movies(request)
        total = the_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(amount=stripe_total, currency=settings.STRIPE_CURRENT)
        order_form = OrderForm()

    if request.user.is_authenticated:
        try:
            profile = get_object_or_404(UserProfile, user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name,
                'email': profile.user.email,
                'default_phone_number': profile.default_phone_number,
                'default_country': profile.default_country,
                'default_postcade': profile.default_postcade,
                'default_town_or_city': profile.default_town_or_city,
                'default_street_address': profile.default_street_address,
                'default_county': profile.default_county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('Movies'))
    the_bag = my_movies(request)
    total = the_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(amount=stripe_total, currency=settings.STRIPE_CURRENT)
    order_form = OrderForm()
    template = 'checkout.html'
     
    context = { 
        'order_form': order_form,
        'stripe_public_key' : stripe_public_key,
        'client_secret' : stripe_secret_key,
        'intent':intent,
    }

    return render(request, template, context)



def checkout_success(request, order_number):
    save_info = request.session.get('save_info',{})
    success_order = get_object_or_404(order, order_number=order_number)
    user = User.objects.get(pk = request.user.id)
    profile = UserProfile.objects.get(user=request.user.id)
    success_order.user_profile = profile
    success_order.save()

    if save_info:
        profile_data = {
            'default_phone_number': success_order.phone_number,
            'default_country': success_order.country,
            'default_postcade': success_order.postcade,
            'default_town_or_city': success_order.town_or_city,
            'default_street_address': success_order.street_address,
            'default_county': success_order.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Thanks for your shopping, your number order is {success_order}, we send you a email at {success_order.email}')

    if 'bag' in request.session:
        del request.session['bag']
    
    template = 'checkout_success.html'

    context = {
        'success_order':success_order,
    }

    return render (request, template, context) 


