from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

@api_view(['GET','POST']) #Al decorador api_view le pasamos en forma de lista aquellos métodos que va a permitir
def user_api_view(request):

    #list
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True) #El atributo 'many = True' se emplea cuando queremos que nos retorne un listado de objetos y no solo un único valor
        return Response(users_serializer.data, status = status.HTTP_200_OK)

    #create
    elif request.method=='POST':
        #El serializador realiza un proceso de validación de los campos del objeto con la información enviada por POST y contenida en 'request.data'

        #queryset
        user_serializer = UserSerializer(data = request.data)   
        
        #validation
        if user_serializer.is_valid():
            '''Si pasa la validación, se genera el registro del usuario en la BD y se guarda la info en 'user_serializer.data' '''
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
        '''Si no pasa la validación los errores se guardan en 'user_serializer.errors' y se envia el código de error '''

@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk=None):
    #queryset
    user = User.objects.filter(id=pk).first() #Factorizamos para evitar repetir la consulta

    #validation
    if user : #Si existe el user

        #retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        
        #update
        elif request.method == 'PUT':
            user_serializer= UserSerializer(user,data = request.data) 
            '''Al colocar 'data = request.data' le estamos pasando al serializador la información nueva que se debe actualizar '''
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
        
        #delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({"message":"Usuario eliminado correctamente"}, status = status.HTTP_200_OK ) 

    return Response({"message":"No se ha encontrado un usuario con estos datos"}, status = status.HTTP_400_BAD_REQUEST ) 
