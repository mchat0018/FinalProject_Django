from django import forms
from PatientInfo.models import Appointments,Queries,Locations

# class MultipleForm(forms.Form):
#     action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class AppointmentForm(forms.ModelForm):

    class Meta:
        model=Appointments
        fields=['full_name','phone','email','location','query']

class QueryForm(forms.ModelForm):

    class Meta:
        model=Queries
        fields=['name','email','phone','query']