from django import forms
from orphanages.models import Birthdaysponsor,Orphanage

class BirthdayForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}))
    orphanage = forms.ModelChoiceField(queryset = Orphanage.objects.exclude(donation_link=""))
    class Meta:
        model = Birthdaysponsor
        fields = ('donators_name','birthday_person_name','birthday_person_email')
