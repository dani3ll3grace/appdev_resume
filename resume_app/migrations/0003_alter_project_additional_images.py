# Generated by Django 5.0.8 on 2024-08-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0002_projectimage_project_extended_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='additional_images',
            field=models.ManyToManyField(blank=True, related_name='projects', to='resume_app.projectimage'),
        ),
    ]
