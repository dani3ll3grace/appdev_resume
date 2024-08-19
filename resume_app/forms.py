from django import forms
from .models import Project, ProjectImage

class ProjectImageInlineForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image', 'caption']

class ProjectAdminForm(forms.ModelForm):
    additional_images = forms.ModelMultipleChoiceField(
        queryset=ProjectImage.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Project
        fields = '__all__'
