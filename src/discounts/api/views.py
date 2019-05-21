from rest_framework.generics import ListAPIView, RetrieveAPIView
from discounts.models import Discount
from .serializers import DiscountSerializer


class DiscountListView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class DiscountDetailView(RetrieveAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
