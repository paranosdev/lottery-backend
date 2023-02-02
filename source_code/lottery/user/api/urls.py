from django.urls import path
from .views import (
    UserRegisterView, UserMeInfoView, UserLoginView,
    UserRefreshTokenView
)

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('me/', UserMeInfoView.as_view(), name='update_info'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('refresh/', UserRefreshTokenView.as_view(), name='refresh_token'),
)
