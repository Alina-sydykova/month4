from django import forms
from posts.models import Category, Post, Tag

class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if (title and content) and (title.lower() == content.lower()):
            raise forms.ValidationError("Title and content should not be the same.")
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError("Title can't be 'python'")
        return 
    
    class PostForm2(forms.ModelForm):
        class Meta:
            model = Post
            fields = ["title", "content", "category", "tags"]



class SearchForm(forms.Form):
    search_q = forms.CharField(required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

    orderings = (
        ("title", "title"),
        ("-title", "-title"),
        ("rate", "rate"),
        ("-rate", "-rate"),
        ("created_at", "created_at"),
        ("-created_at", "-created_at"),
        ("updated_at", "updated_at"),
        ("-updated_at", "-updated_at"),
        (None, None)
    )

    ordering = forms.ChoiceField(choices=orderings, required=False)
