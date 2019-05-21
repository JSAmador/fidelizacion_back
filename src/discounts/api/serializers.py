from rest_framework import serializers
from discounts.models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('name', 'content')
