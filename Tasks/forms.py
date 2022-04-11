from xml.dom.minidom import Attr
from .models import TasksList
from django.forms import ModelForm, widgets
from django import forms

class TasksListForm(forms.ModelForm):
    class Meta:
        model = TasksList
        fields = [ 'title', 'description','rand_tags', 'complete',]

        widgets = {
            #'rand_tags':forms.ChoiceField(),
            
        }
    def __init__(self, *args, **kwargs):
        super(TasksListForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == 'complete' or field =='complete':
                continue    
            field.widget.attrs.update({'class':'form-control','placeholder':name})
