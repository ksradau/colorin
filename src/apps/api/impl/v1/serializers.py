from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import CharField

from apps.blog.models import Photo
from project.utils.forms import a

class PhotoSerializer(serializers.ModelSerializer):

    thumbnail = CharField()

    class Meta:
        model = Photo
        fields = "__all__"