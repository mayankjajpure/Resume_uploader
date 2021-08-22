# Generated by Django 3.2 on 2021-08-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='job_city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='locality',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='mobile',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='my_file',
            field=models.FileField(upload_to='doc'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profileimg'),
        ),
    ]
