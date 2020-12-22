from django import forms

from folder_file.models import File
from mptt.forms import TreeNodeChoiceField


class AddFilesForm(forms.Form):
    name = forms.CharField(max_length=50)
    parent = TreeNodeChoiceField(queryset=File.objects.all())

    def __init__(self, *args, **kwargs):
        super(AddFilesForm, self).__init__(*args, **kwargs)
        self.fields['parent'].required = False
