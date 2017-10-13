from rest_framework import serializers
from models import *



class QrCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QrCode
        fields = "__all__"
        # exclude = ('usuario',)

class BebidasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bebida
        fields = "__all__"

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = "__all__"

class CompraSerializer(serializers.ModelSerializer):

    pedido = PedidoSerializer(many=True)
    qr_code = QrCodeSerializer()

    class Meta:
        model = Compra
        fields = "__all__"

    def create(self,validated_data):
        quantidades_data = validated_data.pop('pedido')

        qr_code = validated_data.pop('qr_code')
        qr_code['usuario'] = validated_data['usuario']

        code = QrCode.objects.create(**qr_code)

        compra = Compra.objects.create(qr_code=code,**validated_data)

        for quantidade in quantidades_data:
            Pedido.objects.create(compra=compra,**quantidade)

        return compra

class ItemDrinkSerializer(serializers.ModelSerializer):

    # bebida = BebidasSerializer(read_only=True)

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


        valor_drink = 0
        for i in misturas:
            b = Bebida.objects.get(nome=i['bebida'].nome)
            #transformacaoo de ml para litro. 
            volume_bebida_n = validated_data['volume']/100.0
            valor_drink += volume_bebida_n * b.preco / b.volume

        drink = Drink.objects.create(preco=valor_drink,**validated_data)

        for mistura in misturas:
            ItemDrink.objects.create(drink=drink,**mistura)

        return drink

class CardapioSerializer(serializers.ModelSerializer):

    proporcao = DrinkSerializer(read_only=True)

    class Meta:
        model = Cardapio
        fields = "__all__"
