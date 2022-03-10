from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import studInfo

class studSerializers(serializers.ModelSerializer):
    class Meta:
        model=studInfo
        fields='__all__'