from django.core.exceptions import ValidationError
from rest_framework  import serializers
from .models import *
import datetime

class QoshiqchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = "__all__"

class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = "__all__"

class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = "__all__"

    def validate(self, attrs):
        i = len(attrs.get("fayl")) - 4
        if attrs.get("fayl")[i:] != ".mp3":
            raise ValidationError("URLfield'da xatolik kuzatildi!")
        return attrs

    def validate(self, attrs):
        if int(attrs.get("davomiylik").total_seconds()) > 420:
            raise ValidationError("Davomiylikda xatolik kuzatildi!")
        return attrs

