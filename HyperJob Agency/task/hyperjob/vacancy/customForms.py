from django import forms


class VacancyForm(forms.Form):
    description = forms.CharField(max_length=1024, required=True)


class ResumeForm(forms.Form):
    description = forms.CharField(max_length=1024, required=True)
