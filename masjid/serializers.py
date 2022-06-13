from masjid.models import Masjid, SalahTime
from rest_framework import serializers





class SalahTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalahTime
        fields = '__all__'

class MasjidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masjid
        fields = ['id', 'name', 'address']