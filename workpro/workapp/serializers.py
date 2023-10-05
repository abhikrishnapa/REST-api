from rest_framework import serializers # Register,Login and CRUD
from workapp.models import Record

# Register and Login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model




# Login and Register
User=get_user_model()

class UserRegister(serializers.ModelSerializer):
    
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model=User
        fields=["username","password","email","password2"]
        
    def save(self):
        reg=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        return reg
    
class UserDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

# CRUD
class RecordSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100) 
    price = serializers.FloatField()    
    year = serializers.IntegerField()    
    quantity = serializers.CharField(max_length=20)
    
    def create(self, validated_data):
        return Record.objects.create(** validated_data)

    def update(self, instance, validated_data):
        instance.name= validated_data.get('name',instance.name)
        instance.price= validated_data.get('price',instance.price)
        instance.year= validated_data.get('year',instance.year)
        instance.quantity= validated_data.get('quantity',instance.quantity)
        
        instance.save()
        return  instance
    





