from django.contrib.auth.hashers import make_password, check_password

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CustomUser

class Register(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        passw = make_password(password)
        try:
            CustomUser.objects.create(email = email, password = passw)
            data = {"msg": "Usuario creado"}
            code = status.HTTP_201_CREATED
        except:
            data = {"msg": "Email ya existe"}
            code = status.HTTP_400_BAD_REQUEST
        return Response(data, status = code)


class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        try:
            user = CustomUser.objects.get(email = email)
            accepted = check_password(user.password, password)
            print(accepted)
            if accepted:
                data = {"msg": "Bienvenido"}
                code = status.HTTP_202_ACCEPTED
            else:
                data = {"msg": "Contraseña inválida"}
                code = status.HTTP_401_UNAUTHORIZED
        except:
            data = {"msg": "Usuario no registrado"}
            code = status.HTTP_400_BAD_REQUEST
        return Response(data, status = code)
