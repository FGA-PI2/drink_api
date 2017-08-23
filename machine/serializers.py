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

    class Meta:
        model = Rack
        fields = "__all__"

class EstoqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estoque
        fields = "__all__"

class QuantidadeCompraSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuantidadeCompra
        fields = "__all__"
