from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=150)
    icon = models.CharField(max_length=50)
    description = RichTextField(default = "no description")

    def __str__(self) -> str:
        return self.title

class Specialism(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=150)
    icon = models.CharField(max_length=50)
    description = RichTextField(default = "no description")

    def __str__(self) -> str:
        return self.title

class Job(models.Model):
    JOB_TYPE = [
        ('FT', 'Full time'),
        ('PT', 'Part time'),
        ('I', 'Internship')
    ]

    job_title = models.CharField(max_length=50)
    job_description = RichTextField(default= "no description")
    job_specialism = models.ForeignKey(Specialism, on_delete=models.CASCADE)
    job_type = models.CharField(choices=JOB_TYPE, max_length=20)

    def __str__(self) -> str:
        return self.job_title

class Job_Requirement(models.Model):
    EXPERIENCE = [
        ('B', 'Beginner'),
        ('J', 'Junior'),
        ('S', 'Senior'),
        ('P', 'Pro Expert')
    ]

    QUALIFICATION = [
        ('G', 'Graduation'),
        ('M', 'Master Degree'),
        ('BP', 'BPharma'),
        ('PHD', 'P.H.D'),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    experience = models.CharField(choices=EXPERIENCE, max_length=20)
    qualification = models.CharField(choices=QUALIFICATION, max_length=20)

    def __str__(self) -> str:
        return self.job

