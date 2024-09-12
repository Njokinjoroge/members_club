from django import forms
from . models import Tag,Newslink,Startup
from django.core.exceptions import ValidationError
    


class SlugCleanMixing:
    def clean_slug(self):
        new_slug =(self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError( 'Slug may not be "create".')
        return new_slug


class TagForm(SlugCleanMixing(forms.ModelForm)):
    
    class Meta:
        model = Tag
        fields = ['name', 'slug']

    def clean_name(self):
        return self.cleaned_data['name'].lower()
    
class NewslinkForm(forms.ModelForm):
    class Meta:
        model = Newslink
        fields = '__all__'

    


class StartUpForm(SlugCleanMixing(forms.ModelForm)):
    class Meta:
        model = Startup
        fields = '__all__'  # For all fields, you can also specify a list of

    