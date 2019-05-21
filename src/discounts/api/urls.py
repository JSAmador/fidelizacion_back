from django.urls import path
from .views import DiscountListView, DiscountDetailView

urlpatterns = [
    path('', DiscountListView.as_view()),
    path('<pk>', DiscountDetailView.as_view())
]
