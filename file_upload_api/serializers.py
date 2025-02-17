from rest_framework import serializers
from .models import *





class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User_tbl
        fields="__all__"
        
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name can't empty")
        return value

    def validate_age(self, value):
        if not (0 <= value <= 120):
            raise serializers.ValidationError("Age must between 0 and 120")
        return value
        