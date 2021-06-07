from django.urls import path
from . import views

urlpatterns = [
    path("projects", views.ProjectList.as_view()),
    path("projects/<int:pk>", views.ProjectDetail.as_view()),
    path("projects/<int:pk>/measurements", views.MeasurementList.as_view()),
    path("projects/<int:project>/measurements/<int:pk>", views.MeasurementDetail.as_view()),
    path("projects/<int:project>/section", views.SectionList.as_view()),
]
