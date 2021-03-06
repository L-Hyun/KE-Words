from django.urls import path
from. import views

urlpatterns = [
    path('register/', views.Register.as_view()),
    path('superuser/', views.SuperUser.as_view()),
    path('login/', views.Login.as_view()),
    path('logout', views.Logout.as_view()),
    path('chngePW/', views.ChangePassword.as_view()),
    path('user/<int:usernumber>', views.GetUser.as_view()),
    path('userchk', views.Userchk.as_view())
]
