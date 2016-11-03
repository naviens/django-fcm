from django.conf import settings
from django.utils.module_loading import import_module


def load_object(object_path):
    module_path, object_name = object_path.rsplit('.', 1)
    module = import_module(module_path)
    return getattr(module, object_name)


DEVICE_MODEL = 'drf_fcm.models.Device'
API_URL = "https://fcm.googleapis.com/fcm/send"
API_KEY = None
MAX_RECIPIENTS = 1000

settings_obj = getattr(settings, 'DRF_FCM', None)

if settings_obj:
    DEVICE_MODEL = settings_obj.get('DEVICE_MODEL', 'drf_fcm.models.Device')
    API_URL = settings_obj.get('API_URL',
                               "https://fcm.googleapis.com/fcm/send")
    API_KEY = settings_obj.get('API_KEY', None)
    MAX_RECIPIENTS = settings_obj.get('MAX_RECIPIENTS', 1000)


def get_device_model():
    return load_object(DEVICE_MODEL)
