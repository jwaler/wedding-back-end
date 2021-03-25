from rest_framework import serializers
from .models import Guest


class GuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guest
        fields = "__all__"  # show all fields, but you can select which one you want to
