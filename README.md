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

**Available Endpoints**:

1. http://localhost:8000/fcm/devices/ (POST)

2. http://localhost:8000/fcm/devices/ (GET)

3. http://localhost:8000/fcm/devices/{pk}/ (GET | PUT)

4. http://localhost:8000/fcm/send/ (POST)

**Register device**:

Endpoint : http://localhost:8000/fcm/devices/ (POST)

Request Header: Authorization : Token "drf auth token"

Request Body:

```json
{
"name": "Lenovo Vibe",
"device_id": "<IMEI>",
"reg_id": "<gcm reg id>",
"is_active": true,
"user": 1
}
```

**List all device for given user**:

Endpoint : http://localhost:8000/fcm/devices/ (GET)

Request Header: Authorization : Token "drf auth token"

Request Body:```

```json
{
  count: 1,
  next: null,
  previous: null,
  results: [
    {
      id: 1,
      created_at: "2016-10-26T14:00:50.422635Z",
      updated_at: "2016-10-26T14:00:50.422664Z",
      name: "Lenovo Vibe",
      device_id: "123456789",
      reg_id: "cOQHI1sddd:reg_id",
      is_active: true,
      user: 1
    }
  ]
}
```

**Send Notifications via REST**:

Endpoint : http://localhost:8000/fcm/send/ (POST)

Request Header: Authorization : Token "drf auth token"

Request Body:

```json
{
"sender": ["reg_id_1", "reg_id_2"],
"data": {"notification":{"title": "hi", "body": "hello world"}}
}
```

**Send Notification messages to 1 device**

```bash
from drf_fcm.models import *
d = Device.objects.all()[0]
d.send_message({"notification":{"title": "hi", "body": "Hello DRF"}})
```

**Send Notification messages to all device**

```bash
from drf_fcm.models import *
d = Device.objects.all()
d.send_message({"notification":{"title": "hi", "body": "Hello DRF"}})
```


**Send Notification messages to all device of particular user**

```bash
from drf_fcm.models import *
d = Device.objects.filter(user=1)
d.send_message({"notification":{"title": "hi", "body": "Hello DRF"}})
```
