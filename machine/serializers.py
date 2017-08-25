from rest_framework import serializers
from models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = ('username','email','')
        fields = ('email','is_superuser','creditos','data_nascimento','id','password')
        extra_kwargs = {
            'password' : {'write_only': True}
        }


    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


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

class CompraSerializer(serializers.ModelSerializer):

    quantidade = QuantidadeCompraSerializer()

    class Meta:
        model = Compra
        fields = "__all__"
