from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from .settings import get_device_model

Device = get_device_model()


class DeviceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label=_("Device Name"), required=False, allow_blank=False,)
    device_id = serializers.CharField(label=_("Device Unique ID or IMEI"), required=True,)
    reg_id = serializers.CharField(label=_("GCM Registration ID"), required=True,)

    default_error_messages = {
        'inactive_device': 'Inactive Device',
        'duplicate_device': 'This device is already registered in your account',
    }

    def validate_device_id(self, value):
        if self.Meta.model.objects.filter(device_id=value, user=self.context.user).exists():
            raise serializers.ValidationError(self.error_messages['duplicate_device'])
        return value

    class Meta:
        model = Device
        fields = ('id','name', 'device_id', 'reg_id', 'is_active', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class FCMSerializer(serializers.Serializer):
    sender = serializers.ListField()
    data = serializers.DictField()
