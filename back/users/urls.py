from django.urls import path

from users.views import UsersLoginViews
from django.urls import path

urlpatterns = [
    path("users/login/", UsersLoginViews.as_view() , name="login")
]
