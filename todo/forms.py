from django import forms
from .models import Branch, Todo
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


class BranchForm(forms.ModelForm):

    class Meta:
        model = Branch
        fields = ['name']


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class ToDoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'content', 'importance', 'finish_date', 'finish_time']
        widgets = {
            'finish_date': DateInput(),
            'finish_time': TimeInput(),
        }

class FullToDoForm(forms.ModelForm):


    class Meta:
        model = Todo
        fields = ['branch','title', 'content', 'importance', 'finish_date', 'finish_time']
        widgets = {
            'finish_date': DateInput(),
            'finish_time': TimeInput(),
        }