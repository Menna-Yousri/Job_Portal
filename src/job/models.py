from django.db import models
from django.core.validators import MinValueValidator

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance, filename):
    imagename, extention= filename.split('.')
    return f"jobs/{instance.id}.{extention}"

class Job(models.Model):
    title= models.CharField(max_length=100)
    job_type= models.CharField(max_length=15, choices=JOB_TYPE)
    description= models.TextField(max_length=1000)
    published_at= models.DateField(auto_now=True)
    vacancy= models.IntegerField(default=1, validators=[MinValueValidator(0)]) #number of available places
    salary= models.IntegerField(default=0, validators=[MinValueValidator(0)])
    experience= models.IntegerField(default=0, validators=[MinValueValidator(0)])
    category= models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)      # The '' for the Category because it comes later, if it was before we needn't the ''
    image= models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.title


class Category(models.Model):
    name= models.CharField(max_length=25)

    def __str__(self):
        return self.name
