from rest_framework import serializers
from .models import Uploadmusic

class UploadmusicSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    music = serializers.FileField(use_url=True)

    class Meta:
        model = Uploadmusic
        fields = '__all__'