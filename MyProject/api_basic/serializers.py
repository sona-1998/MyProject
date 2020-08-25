from rest_framework import serializers
from .models import User
#from .models import LoginUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['first_name','last_name','user_name','phone_no','email', 'password','conform_password']
        fields =  '__all__'

#login
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['first_name','last_name','user_name','phone_no','email', 'password','conform_password']
        fields = ['email', 'password']

'''class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    user_name = serializers.CharField(max_length=100)
    phone_no = serializers.IntegerField()
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)
    conform_password = serializers.CharField(max_length=50)


    def create(self, validated_data):
        return User.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.user_name)
        instance.conform_password = validated_data.get('conform_password', instance.user_name)
        instance.save()
        return instance'''