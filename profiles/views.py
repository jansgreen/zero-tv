from django.shortcuts import render, reverse, get_object_or_404
from .models import UserProfile
from .forms import UserProfileforms
from checkout.models import order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User





@login_required
def profiles(request):
    
    profile = UserProfile.objects.get_or_create(user=request.user.id)
    if request.method == 'POST':
        form = UserProfileforms(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successfully')
        else:
            messages.error (request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileforms(instance=profile)
    template = 'profile.html'
    context = {
        'form':form,
        'profile': profile,

    }
    return render(request, template, context)

@login_required
def order_history(request):
    """
    Redirect the user to their user profile
    """
    profile = UserProfile.objects.get_or_create(UserProfile,user=request.user.id)

    orders = profile.orders.all()

    template = 'Order_History.html'
    context = {
        'orders':orders,

    }
    return render(request, template, context)