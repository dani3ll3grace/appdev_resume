from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='project_images/')
    extended_description = models.TextField(blank=True, null=True)
    additional_images = models.ManyToManyField('ProjectImage', related_name='projects', blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.caption if self.caption else f'Image for project'
