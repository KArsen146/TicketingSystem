from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.permissions import IsAuthenticatedWithoutCreate
from user.serializers import UserSerializer


class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticatedWithoutCreate,)
