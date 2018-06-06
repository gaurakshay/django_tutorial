from django.urls import path
from students import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    path('depts/', views.DeptListView.as_view(), name='dept_list'),
    path('depts/<str:pk>/', views.DeptDetailView.as_view(), name='dept_details'),
]
