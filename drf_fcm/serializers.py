from rest_framework import serializers

from .settings import get_device_model

Device = get_device_model()


class DeviceSerializer(serializers.ModelSerializer):
    default_error_messages = {
        'inactive_device': 'Inactive Device',
    }

    class Meta:
        model = Device
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class FCMSerializer(serializers.Serializer):
    sender = serializers.ListField()
    data = serializers.DictField()
