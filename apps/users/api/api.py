from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

@api_view(['GET','POST']) #Al decorador api_view le pasamos en forma de lista aquellos métodos que va a permitir
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True) #El atributo 'many = True' se emplea cuando queremos que nos retorne un listado de objetos y no solo un único valor
        return Response(users_serializer.data)

    elif request.method=='POST':
        #Toda la información que se envie por el método POST estará guardada en request.data
        print(request.data)
