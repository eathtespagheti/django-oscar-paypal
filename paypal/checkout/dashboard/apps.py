from django.urls import path
from django.utils.translation import gettext_lazy as _
from oscar.core.application import OscarDashboardConfig


class CheckoutDashboardApplication(OscarDashboardConfig):
    name = 'paypal.checkout.dashboard'
    label = 'checkout_dashboard'
    namespace = 'checkout_dashboard'
    verbose_name = _('Checkout Dashboard')

    default_permissions = ["is_staff"]

    def get_urls(self):
        from . import views

        urlpatterns = [
            path('transactions/', views.TransactionListView.as_view(),
                 name='paypal-transaction-list'),
            path('transactions/<int:pk>/', views.TransactionDetailView.as_view(),
                 name='paypal-transaction-detail'),
        ]
        return self.post_process_urls(urlpatterns)
