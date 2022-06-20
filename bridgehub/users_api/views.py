from rest_framework import viewsets

from users_api.serializers import UserSerializer
from users_api.models import User
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if 'nome' in request.data:
            instance.nome = request.data.get("nome")
        if 'email' in request.data:
            instance.email = request.data.get("email")
        if 'telefone' in request.data:
            instance.telefone = request.data.get("telefone")

        instance.save()

        serializer = UserSerializer(data=instance.to_dict())
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)