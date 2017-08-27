from rest_framework import serializers
from models import *



class QrCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QrCode
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

class ItemDrinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemDrink
        fields = "__all__"

class DrinkSerializer(serializers.ModelSerializer):

    proporcao = ItemDrinkSerializer(many=True)

    class Meta:
        model = Drink
        fields = "__all__"

    def create(self,validated_data):
        misturas = validated_data.pop('proporcao')
        drink = Drink.objects.create(**validated_data)

        for mistura in misturas:
            ItemDrink.objects.create(drink=drink,**mistura)

        return drink

class CardapioSerializer(serializers.ModelSerializer):

    proporcao = DrinkSerializer(read_only=True)

    class Meta:
        model = Cardapio
        fields = "__all__"
