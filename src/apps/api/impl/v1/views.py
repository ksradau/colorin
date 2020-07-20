from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.api.impl.v1.serializers import PhotoSerializer
from apps.blog.models import Photo


class PhotoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhotoSerializer


    def get_queryset(self):
        return Photo.objects.all()