from rest_framework import serializers
from deals.models import Deal


class DealCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'


class DealListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'


class DealDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'
