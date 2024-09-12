from django import forms

from . models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        return new_slug
