from django.urls import path

from .views import job_list, job_detail

app_name = "jobs"
urlpatterns = [
    path("", job_list, name="job_list"),
    path("<int:pk>/", job_detail, name="job_detail"),
]
