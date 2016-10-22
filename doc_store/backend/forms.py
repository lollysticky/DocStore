from django import forms
from .utils import get_project_choices


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    project_field = forms.TypedChoiceField(empty_value=None, choices=get_project_choices(), initial=None, required=False,
                                           widget=forms.Select(attrs={'class': 'selector', 'title': 'Project'}))
