from django.urls import path
from apps.users import views as users


urlpatterns = [
    path('', users.index, name="index"),
    path('/register/', users.register, name="register"),
    path('/login/', users.user_login, name="user_login"),
    path('/profile/<int:id>/', users.profile, name="profile")
]