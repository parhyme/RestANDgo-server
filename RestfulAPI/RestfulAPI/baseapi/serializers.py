from rest_framework import serializers
from .models import MobileInfo

class MobileInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileInfo
        fields = '__all__'