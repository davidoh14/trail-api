from .models import APIKey

def is_api_key_authorized(api_key):
    if APIKey.objects.filter(key=api_key, active=True):
        return True
    else:
        return False