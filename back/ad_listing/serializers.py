from rest_framework import serializers
from .models import Advert


class AdvertSerializer(serializers.ModelSerializer):
    city = serializers.CharField()
    category = serializers.CharField()

    class Meta:
        model = Advert
        read_only_fields = [
            "id",
            "views"
        ]
        fields = [
            "id",
            "title",
            "category",
            "city",
            "views",
            "description"
        ]
