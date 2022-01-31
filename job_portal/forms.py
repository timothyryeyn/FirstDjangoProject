from django import forms
from job_portal.models import Job, Skill

class JobForm(forms.ModelForm):
  class Meta:
    model = Job
    fields = ['name', 'type', 'salary', 'description']
    widgets = {
      'name': forms.TextInput(attrs={'placeholder': 'Enter name', 'class': 'input-1px w-[250px]'}),
      'salary': forms.NumberInput(attrs={'placeholder': 'Enter salary', 'class': 'input-1px w-[250px]'}),
      'type': forms.Select(attrs={'class': 'select-2 w-[250px]'}),
      'description': forms.Textarea(attrs={'placeholder': 'Enter description', 'class': 'input-1px'}),
    }

  jobskill = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple)
