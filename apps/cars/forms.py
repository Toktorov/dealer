from django import forms
from apps.cars.models import Test_drive


class Test_drive_form(forms.ModelForm):



    class Meta:
        model = Test_drive
        fields = ('name','email','phone','date','car')
