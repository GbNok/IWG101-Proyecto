from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("logged/", views.logged_index, name="logged index"),
    path("<int:subject_id>/", views.study, name="study"),
    path("<int:subject_id>/problems/<int:problem_id>/", views.solutions, name="answers"),
    path("<int:subject_id>/problems/<int:problem_id>/submit/", views.upload_problem, name="problem_upload"),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout"),
]