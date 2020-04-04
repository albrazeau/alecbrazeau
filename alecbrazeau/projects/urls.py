from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectsList.as_view(), name='home'),
    path('<slug:slug>/', views.ProjectDetail.as_view(), name='project_detail')
]