def get_auth_profile_model() -> type:
    from apps.authorization.models import AuthProfile as _Model

    return _Model
