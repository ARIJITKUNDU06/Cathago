from django.urls import path
from .views import register, user_login, user_logout, request_credits, approve_credits

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('request_credits/', request_credits, name='request_credits'),
    path('approve_credits/<int:request_id>/', approve_credits, name='approve_credits'),
]
