# drf-fcm
Firebase Cloud Messaging Server in Django Rest FrameWork

# Installation
```bash
pip install drf-fcm
```

# Configuration

settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    '...',
    'drf_fcm',
]
```

```python
DRF_FCM = {
    'API_KEY': <FCM_SERVER_KEY>,
}
```

# Docs
Send Notification messages to 1 device

```bash
from drf_fcm.models import *
d = Device.objects.all()[0]
d.send_message({"notification":{"title": "hi", "body": "Hello DRF"}})
```

Send Notification messages to all device

```bash
from drf_fcm.models import *
d = Device.objects.all()
d.send_message({"notification":{"title": "hi", "body": "Hello DRF"}})
```


Send Notification messages to all device of particular user

```bash
from drf_fcm.models import *
d = Device.objects.filter(user=1)
d.send_message({"notification":{"title": "hi", "body": "Hello DRF"}})
```