from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer): #Se trata de un serializador basado en un modelo
    '''El serializador sera el encargado de convertir cualquier registro de mi tabla 'User' en formato JSON'''
    class Meta:
        model = User
        fields = '__all__' #Le pasamos todos los campos de la clase User
