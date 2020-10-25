from django import forms

from .models import BlogPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "text"]
        labels = {"tile": "", "text": "Entry:"}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}


# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ["text"]
#         lables = {"text": "Entry:"}
#         widgets = {"text": forms.Textarea(attrs={"cols": 80})}
