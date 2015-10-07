from cmdb.models import UpdateInfo
from rest_framework import serializers


class CMDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateInfo



