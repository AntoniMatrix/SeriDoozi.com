from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Post
        fields = [
            'title', 'slug', 'excerpt', 'thumbnail',
            'meta_title', 'meta_description', 'canonical_url',
            'content','status'
        ]
        widgets = {
            'excerpt': forms.Textarea(attrs={'rows': 3}),
            'meta_description': forms.Textarea(attrs={'rows': 2}),
        }
