from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .serializers import (
    RegisterUserSerializer, UserInfoSerializer
)


class BaseAPIView(GenericAPIView):
    pass


class BaseUserView(BaseAPIView):
    swagger_tags = ['user']

    def get_serializer_context(self):
        context = super(BaseUserView, self).get_serializer_context()
        context['user'] = self.request.user
        return context


class UserRegisterView(BaseUserView, CreateAPIView):
    serializer_class = RegisterUserSerializer


class UserMeInfoView(BaseUserView, RetrieveUpdateAPIView):
    serializer_class = UserInfoSerializer

    def get_object(self):
        return self.request.user


class UserLoginView(TokenObtainPairView):
    swagger_tags = ['user']


class UserRefreshTokenView(TokenRefreshView):
    swagger_tags = ['user']
