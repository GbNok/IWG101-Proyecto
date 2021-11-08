from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:subject_id>/", views.study, name="study"),
    path("<int:subject_id>/problems/<int:problem_id>/", views.problem, name="problem")
]