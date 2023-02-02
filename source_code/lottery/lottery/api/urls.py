from django.urls import path, include

from .views import PingView, TestView

urlpatterns = (
    path('users/', include(('user.api.urls', 'user'), namespace='users'), name='users'),
    path('ping/', PingView.as_view(), name='ping'),
    path('test', TestView.as_view(), name='test')
)
