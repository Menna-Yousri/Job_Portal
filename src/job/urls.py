from django.urls import path, include
from .views import job_list, job_detail

app_name= 'job'

urlpatterns = [
    path('', job_list),
    path('<int:id>', job_detail, name='job_detail'),
]