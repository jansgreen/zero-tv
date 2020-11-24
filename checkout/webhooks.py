# Set your secret key. Remember to switch to your live secret key in production!
# See your keys here: https://dashboard.stripe.com/account/apikeys
import json
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


from checkout.webhook_handler import StripeWH_Handler

# setting
webhook_secret = settings.STRIPE_WEBHOOK_KEY
stripe.api_key = settings.STRIPE_SECRET_KEY

# Using Django
@require_POST
@csrf_exempt
def my_webhook_view(request):
    request_data = json.loads(request.body)
    event = None
    data = request_data['data']
    event_type = request_data['type']


    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.META['HTTP_STRIPE_SIGNATURE'] #request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.body, sig_header=signature, secret=webhook_secret)
        except ValueError as e:
        # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
        # Invalid signature
            return HttpResponse(status=400)
        except Exception as e:
            return HttpResponse(content=e, status=400)
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
    else:
        messages.error(request, 'the shopping will be cancel, please call support # not webhook key found!' )
        return HttpResponse(status=400)

    handler = StripeWH_Handler(request)
    event_map = {
        'payment_intet.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intet.payment_feiled': handler.handle_payment_intent_failed
        }
    event_hadler = event_map.get(event_type, handler.handle_event)
    Response = event_hadler(event)
    return Response


