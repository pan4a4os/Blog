from .models import Post
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput, Textarea, Select


class PostsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['owner', 'phone_number', 'title', 'text', 'type', 'price', 'status', 'created', 'image']

        widgets = {
            "owner": TextInput(attrs={'class': 'form-control'}),
            "phone_number": NumberInput(attrs={'class': 'form-control'}),
            "title": TextInput(attrs={'class': 'form-control'}),
            "text": Textarea(attrs={'class': 'form-control'}),
            "type": Select(attrs={'class': 'form-control'}),
            "price": NumberInput(attrs={'class': 'form-control'}),
            "status": Select(attrs={'class': 'form-control'}),
            "created": DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
        }
