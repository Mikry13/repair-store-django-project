from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from django.db.models import QuerySet

from users.api.serializers import UserSerializer
from users.api.serializers import UserUpdateSerializer
from users.models import User
from users.services.user_updater import UserUpdater


class SelfView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, *args: list, **kwargs: dict) -> Response:
        user = self.get_object()
        serializer = self.get_serializer(user)

        return Response(serializer.data)

    def put(self, request: Request, *args: list, **kwargs: dict) -> Response:
        raise MethodNotAllowed('PUT')

    def get_object(self) -> User:
        return self.get_queryset().get(pk=self.request.user.pk)

    def get_queryset(self) -> QuerySet[User]:
        return User.objects.filter(is_active=True)

    def patch(self, request: Request, *args: list, **kwargs: dict) -> Response:
        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_updater = UserUpdater(
            user=self.get_object(),
            password=serializer.validated_data.pop('password', ''),
            new_user_data=serializer.validated_data,
        )
        return Response(user_updater(), 200)  # type: ignore
