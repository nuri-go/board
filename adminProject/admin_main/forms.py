from django import forms
from .models import Client_list
import datetime

class DateTimeField(forms.DateInput):
    day = forms.DateField(initial=datetime.date.today)
    input_type = 'date'



class ListForm(forms.ModelForm):
    class Meta:
        model = Client_list
        fields = ('voc_date','voc_method','client_number','client_name','voc_number','voc_title','voc_content','voc_comment','voc_manger','report','partner')
        #('voc_method',)
        #,'voc_date','client_number','client_name','voc_number','voc_title','voc_content','voc_comment','voc_manger','report','partner')
        widgets = {
            'voc_date': forms.TextInput(attrs={'class': 'form-control','rows':2}),
            'voc_method': forms.TextInput(attrs={'class': 'form-control','rows':2}),
            'client_number' : forms.TextInput(attrs={'class': 'form-control','lows':2}),
            'client_name' : forms.TextInput(attrs={'class': 'form-control','lows':2}),
            'voc_number' : forms.TextInput(attrs={'class': 'form-control','lows':2}),
            'voc_title' : forms.TextInput(attrs={'class': 'form-control','lows':2}),
            'voc_content' : forms.Textarea(attrs={'class': 'form-control'}),
            'voc_comment' : forms.TextInput(attrs={'class': 'form-control','lows':2}),
            'voc_manger' : forms.TextInput(attrs={'class': 'form-control','lows':2}),
            'report' : forms.TextInput(attrs={'class': 'form-control'}),
            'partner' : forms.TextInput(attrs={'class': 'form-control','lows':2}),
        }
