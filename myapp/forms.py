from django import forms
from .models import resume

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]
JOB_CITY_CHOICE=[
    ('inodre','inodre'),
    ('Mumbai','Mumbai'),
    ('surat','surat'),
    ('bhuj','bhuj'),
    ('luknow','luknow'),
    ('banglore','banglore'),
    ('ahemdabad','ahemdabad')

]

class resumeform(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES)
    job_city=forms.MultipleChoiceField(label='prefred job locations',choices=JOB_CITY_CHOICE,required=False,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=resume
        fields=['name','dob','gender','locality','pin','state','mobile','email','job_city']
