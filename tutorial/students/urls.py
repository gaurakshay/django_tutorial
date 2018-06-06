from django.urls import path
from students import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
]
