from django.urls import path

from paypal.checkout import views
from paypal.checkout.gateway import buyer_pays_on_paypal

base_patterns = [
    # Views for normal flow that starts on the basket page
    path('redirect/', views.PaypalRedirectView.as_view(), name='checkout-redirect'),
    path('cancel/<int:basket_id>/', views.CancelResponseView.as_view(),
         name='checkout-cancel-response'),
    # View for using PayPal as a payment method
    path('payment/', views.PaypalRedirectView.as_view(as_payment_method=True),
         name='checkout-direct-payment'),
]


buyer_pays_on_paypal_patterns = [
    path('handle-order/<int:basket_id>/',
         views.SuccessResponseView.as_view(preview=True),
         name='checkout-handle-order'),
]

buyer_pays_on_website_patterns = [
    path('place-order/<int:basket_id>/', views.SuccessResponseView.as_view(),
         name='checkout-place-order'),
    path('preview/<int:basket_id>/',
         views.SuccessResponseView.as_view(preview=True),
         name='checkout-success-response'),
]


if buyer_pays_on_paypal():
    urlpatterns = base_patterns + buyer_pays_on_paypal_patterns
else:
    urlpatterns = base_patterns + buyer_pays_on_website_patterns
