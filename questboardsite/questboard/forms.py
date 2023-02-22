from django import forms
from django.forms import Textarea

from .models import Questboard, Quest


class QuestboardForm(forms.ModelForm):
    class Meta:
        model = Questboard
        fields = ['name', 'description', 'required_stars']
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 5}),
        }


class AddQuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = [
            'name', 'description', 'star_count', 'is_for_everyone',
            'student_1', 'student_2', 'student_3'
        ]
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 5}),
        }


class DibsQuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = [
            'student_1', 'student_2', 'student_3'
        ]
