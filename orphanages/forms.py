from django import forms
from orphanages.models import Birthdaysponsor,Orphanage

class BirthdayForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput())
    orphanage = forms.ModelChoiceField(queryset = Orphanage.objects.filter(donation_link=""))
    class Meta:
        model = Birthdaysponsor
        fields = ('donators_name','birthday_person_name')
