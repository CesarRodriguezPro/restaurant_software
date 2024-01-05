import stripe
from api_keys.stripe import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY, STRIPE_ENDPOINT_SECRET, \
    subscription_list
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from accounts.models import CustomUser
from subscription.models import StripeCustomer


@login_required
def home(request):
    return render(request, 'subscription/home.html')


@csrf_exempt
def create_checkout_session(request):
    # create one of this views is for each subscription option.
    # the subscription js has to be updated as well.
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'subscription/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'subscription/cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=subscription_list  # api_keys stripe
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config_ = {'publicKey': STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config_, safe=False)


@login_required
def success(request):
    return render(request, 'subscription/success.html')


@login_required
def cancel(request):
    return render(request, 'subscription/cancel.html')


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = STRIPE_SECRET_KEY
    endpoint_secret = STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            endpoint_secret
        )

        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            client_reference_id = session.get('client_reference_id')
            stripe_customer_id = session.get('customer')
            stripe_subscription_id = session.get('subscription')
            user = CustomUser.objects.get(id=client_reference_id)
            StripeCustomer.objects.create(
                user=user,
                stripeCustomerId=stripe_customer_id,
                stripeSubscriptionId=stripe_subscription_id,
            )
            print(user.username + ' just subscribed.')
        return HttpResponse(status=200)

    except ValueError as e:
        print(f"ValueError -> ", e)
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
        print("SignatureVerification", e)
        return HttpResponse(status=400)
