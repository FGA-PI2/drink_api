from rest_framework import serializers
from models import *




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        partial = True
        # fields = ('username','email','')
        fields = ('email','is_superuser','creditos','data_nascimento','password','id','first_name')
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
