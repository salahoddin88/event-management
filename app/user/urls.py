from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('token', views.LoginAPIView.as_view(), name='token'),
    path('delete-token', views.LogoutAPIView.as_view(), name='delete_token')
]
