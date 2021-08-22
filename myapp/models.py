from django.db import models

STATE_CHOICE=(
    (
        ('Aasam','Aasam'),
        ('bihar','bihar'),
        ('up','up')
    )
)

# Create your models here.
class resume(models.Model):
    name=models.CharField(max_length=50)
    dob=models.CharField(max_length=10)
    gender=models.CharField(max_length=50)
    locality=models.CharField(max_length=50)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE, max_length=50)
    mobile=models.PositiveIntegerField()
    email=models.EmailField(max_length=254)
    job_city=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)
