# views.py

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import uuid
from .models import Payment

@api_view(['POST'])
def sslcommerz_init(request):
    data = request.data
    tran_id = str(uuid.uuid4())  # Generate a unique transaction ID
    amount = 100  # Example amount

    # Save payment information to the database
    payment = Payment.objects.create(
        tran_id=tran_id,
        name=data.get('name'),
        email=data.get('email'),
        address=data.get('address'),
        city=data.get('city'),
        state=data.get('state'),
        zip_code=data.get('zipCode'),
        amount=amount,
        status='Pending'
    )

    payment_data = {
        'store_id': settings.SSL_COMMERZ_STORE_ID,
        'store_passwd': settings.SSL_COMMERZ_STORE_PASSWORD,
        'total_amount': amount,
        'currency': 'BDT',
        'tran_id': tran_id,
        'success_url': 'http://localhost:5173/payment_success',
        'fail_url': 'http://localhost:5173/payment_failed',
        'cancel_url': 'http://localhost:5173/payment_cancel',
        'ipn_url': 'http://127.0.0.1:8000//api/sslcommerz/ipn',
        'cus_name': data.get('name'),
        'cus_email': data.get('email'),
        'cus_add1': data.get('address'),
        'cus_city': data.get('city'),
        'cus_state': data.get('state'),
        'cus_postcode': data.get('zipCode'),
        'cus_country': 'Bangladesh',
        'cus_phone': '01711111111',
        'shipping_method': 'NO',
        'product_name': 'Example Product',
        'product_category':'test',
        'product_profile': 'general'
        
    }

    if settings.SSL_COMMERZ_SANDBOX:
        url = 'https://sandbox.sslcommerz.com/gwprocess/v4/api.php'
    else:
        url = 'https://securepay.sslcommerz.com/gwprocess/v4/api.php'

    response = requests.post(url, data=payment_data)
    
    try:
        response_data = response.json()
        print("Response Data:", response_data)  # Debugging: Print the response data

        if response_data.get('status') == 'SUCCESS':
            return Response({'GatewayPageURL': response_data['GatewayPageURL']})
        else:
            return Response({'error': 'Failed to initialize payment'}, status=400)
    except ValueError:
        return Response({'error': 'Invalid response from SSLCommerz'}, status=500)

# views.py

@api_view(['POST'])
def sslcommerz_ipn(request):
    ipn_data = request.data
    tran_id = ipn_data.get('tran_id')

    try:
        payment = Payment.objects.get(tran_id=tran_id)
    except Payment.DoesNotExist:
        return Response({'status': 'error', 'message': 'Payment not found'}, status=404)

    if ipn_data.get('status') == 'VALID':
        payment.status = 'COMPLETED'
    else:
        payment.status = 'FAILED'

    payment.save()
    return Response({'status': 'success'})
