from django.views import View
from rest_framework.authtoken.views import ObtainAuthToken as _DrfObtainAuthToken
import json
from django.http import HttpResponse
import requests
from project import settings

from apps.api.tgbot.matrix import matrix, beautiful_print


class ObtainAuthToken(_DrfObtainAuthToken):
    swagger_schema = None
