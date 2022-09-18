from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    remote_addr = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'surname',
            'email',
            'position',
            'rank',
            'phone',
            'remote_addr',
        ]

    def get_remote_addr(self, obj: User) -> str:
        return self.context['request'].META['REMOTE_ADDR']


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, allow_blank=False, required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'surname',
            'email',
            'position',
            'rank',
            'phone',
            'password',
        ]
