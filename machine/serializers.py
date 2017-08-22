from rest_framework import serializers
from models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = ('username','email','')
        fields = "__all__"

class BebidasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bebida
        fields = "__all__"


class RackSerializer(serializers.ModelSerializer):

    bebida = serializers.SlugRelatedField(
            many=True,
            read_only=True,
            slug_field='name'
            )

    class Meta:
        model = Rack
        fields = "__all__"
