from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'caption')
    #readonly_fields = ('image',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    filter_horizontal = ('additional_images',)  # Use this to manage ManyToManyField
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project_url', 'image', 'extended_description', 'additional_images')
        }),
    )

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
