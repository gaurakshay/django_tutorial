from django.urls import path
from students import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    path('depts/', views.DeptListView.as_view(), name='dept_list'),
    path('depts/<str:pk>/details/', views.DeptDetailView.as_view(), name='dept_details'),
    path('students/', views.StudentListView.as_view(), name='stud_list'),
    path('students/<int:pk>/details/', views.StudentDetailView.as_view(), name='stud_details'),
    path('students/add/', views.StudentAddView.as_view(), name='stud_add'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='stud_update'),
]
