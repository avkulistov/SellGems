from rest_framework import serializers
from deals.models import Deal
from django.db.models import Sum


class DealCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'


class DealListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'


class DealSpentUsersSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('customer_to_username')
    spent_money = serializers.SerializerMethodField('calculate_spent_money')
    gems = serializers.SerializerMethodField('get_gems')

    def customer_to_username(self, deal):
        return deal['customer']

    def calculate_spent_money(self, deal):
        return deal['total_sum']

    def get_gems(self, deal):
        return deal['gems']

    class Meta:
        model = Deal
        fields = ('username', 'spent_money', 'gems')


class DealDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'
