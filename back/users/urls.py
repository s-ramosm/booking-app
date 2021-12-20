from django.urls import path

from users.views import UsersLoginView,UsersSingUpView
from django.urls import path

urlpatterns = [
    path("users/login/", UsersLoginView.as_view() , name="login"),
    path("users/singup/", UsersSingUpView.as_view() , name="singup"),
]
