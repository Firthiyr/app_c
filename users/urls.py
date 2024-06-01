from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("sign_in/", views.sign_in, name="sign_in"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
    path("users_cart/", views.users_cart, name="users_cart"),
]
