from rest_framework import serializers
from models import *


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

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = "__all__"

class CompraSerializer(serializers.ModelSerializer):

    pedido = PedidoSerializer(many=True)

    class Meta:
        model = Compra
        fields = "__all__"


    def create(self,validated_data):
        quantidades_data = validated_data.pop('pedido')
        compra = Compra.objects.create(**validated_data)

        for quantidade in quantidades_data:
            QuantidadeCompra.objects.create(compra=compra,**quantidade)

        return compra
