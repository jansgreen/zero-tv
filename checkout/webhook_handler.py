from django.http import HttpResponse
from .models import order, OrderLineItem
from catalog.models import Movies
from profiles.models import UserProfile
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

import json
import time


# I Fallow the totorial Boutique Ado

class StripeWH_Handler:
    """
    docstring
    """
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        docstring
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order':order}
        )

        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order':order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL
            [cust_email]
        )
        
    
    def handle_event(self, event):
        """
        docstring
        """
        return HttpResponse(content= f'unhandled Webhook received :{event["type"]}', status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """ 
        docstring
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping_detailsgrant_total = round(intent.charges.data[0].amount/ 100, 2)


        for field, value in shipping_details.address.items():
            if value=="":
                shipping_details.address[field] = None

        #UPDATA PROFILE INFORMATION

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.country
                profile.default_postcade = shipping_details.postcade
                profile.default_town_or_city = shipping_details.town_or_city
                profile.default_address = shipping_details.address.line1
                profile.default_county = shipping_details.address.county
                profile.save()



        order_exists = False
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    user_profile=profile,
                    email__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcade__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.town_or_city,
                    street_address__iexact=shipping_details.address.line1,
                    county__iexact=shipping_details.address.county,
                    date__iexact=shipping_details.date,
                    original_bag = bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            
            except order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(content= f'Webhook intent received :{event["type"]}', status=200)
        
        else:
            try:
                order = Order.objects.create(
                    full_name__iexact=shipping_details.name,
                    email__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcade__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.town_or_city,
                    street_address__iexact=shipping_details.address.line1,
                    county__iexact=shipping_details.address.county,
                    date__iexact=shipping_details.date,
                    original_bag = bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=shipping_details.email,
                    phone_number=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcade__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.town_or_city,
                    street_address__iexact=shipping_details.address.line1,
                    county__iexact=shipping_details.address.county,
                    date=shipping_details.date,
                    )
                movies = Movies.objects.get(id=item_id)
                if isinstance(item_data, int):
                    orde_line_item = OrderLineItem(
                        order=order,
                        movies=movies,
                        quantity=quantity,
                    )
                    orde_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
        return HttpResponse(content= f'Webhook intent received :{event["type"]}', status=200)

    def handle_payment_intent_failed(self, event):
        """
        docstring
        """
        return HttpResponse(content= f'Webhook received :{event["type"]} intent fieled', status=200)