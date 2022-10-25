from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

class UserAPIView(APIView):

    def get(self,request):
        '''Este método sera el encargado de responder cualquier petición que un front envie por el método HTTP GET'''
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True) #El atributo 'many = True' se emplea cuando queremos que nos retorne un listado de objetos y no solo un único valor
        return Response(users_serializer.data)

