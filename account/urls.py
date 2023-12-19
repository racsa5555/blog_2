from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegistration.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]
