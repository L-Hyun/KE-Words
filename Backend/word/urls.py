from django.urls import path
from. import views

urlpatterns = [
    path('apply/', views.Apply.as_view()),
    path('wordchk/', views.Wordchk.as_view())
]
