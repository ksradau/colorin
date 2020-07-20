from os import urandom
from typing import Union

from delorean import Delorean
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.sites.models import Site
from django.http import HttpRequest

from apps.authorization.models import AuthProfile
from apps.authorization.utils.profile import setup_profile

User = get_user_model()


def setup_auth_profile(user: User, site: Site) -> AuthProfile:
    code = urandom(16).hex()
    auth = AuthProfile(user=user, site=site, verification_code=code)
    auth.save()
    return auth


def deactivate_user(user):
    user.is_active = False
    user.save()


def start_verification(request: HttpRequest, user: User):
    setup_auth_profile(user, request.site)
    deactivate_user(user)


def finalize_verification(request: HttpRequest, code: Union[str, None]) -> bool:
    if not code:
        return False

    try:
        auth = AuthProfile.objects.get(verification_code=code)
    except AuthProfile.DoesNotExist:
        return False

    if auth.is_verified:
        return True

    auth.verified_at = Delorean().datetime
    auth.save()
    auth.user.is_active = True
    auth.user.save()

    setup_profile(auth.user)

    login(request, auth.user)

    return True
