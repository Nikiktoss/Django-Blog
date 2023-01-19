from django import forms
from .models import Note


class NoteForm(forms.Form):
    title = forms.CharField(label="Название", max_length=150, widget=forms.TextInput(
        attrs={'class': 'text_input_field'}))
    content = forms.CharField(label="Контент", widget=forms.Textarea(
        attrs={'cols': 60, 'rows': 10, 'class': 'text_area_field'}))
    slug = forms.SlugField(label="URL", widget=forms.TextInput(attrs={'class': 'text_input_field'}))

    required_css_class = "field_label"


class NoteUpDateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title", "content", "slug")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'text_input_field'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'text_area_field'}),
            'slug': forms.TextInput(attrs={'class': 'text_input_field'})
        }
        labels = {
            'title': 'Название',
        }
