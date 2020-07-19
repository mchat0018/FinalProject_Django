from django import forms
from PatientInfo.models import Appointments,Queries,Locations

class AppointmentForm(forms.ModelForm):

    class Meta:
        model=Appointments
        fields=['full_name','phone','email','location','query']

class QueryForm(forms.ModelForm):

    class Meta:
        model=Queries
        fields=['name','email','phone','query']