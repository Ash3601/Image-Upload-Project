from rest_framework import serializers
from .models import Image, Profile


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'image', 'description', 'user']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['user', 'pwd']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'pwd']
