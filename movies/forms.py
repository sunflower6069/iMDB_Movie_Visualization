from django import forms

class CalendarForm1(forms.Form):
    date1 = forms.CharField(label='date',max_length=20, widget=forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}))

class CalendarForm2(forms.Form):
    date2 = forms.CharField(label='date',max_length=20, widget=forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}))

class SchForm(forms.Form):
    search = forms.CharField(label='search',max_length=20,widget=forms.Textarea(attrs={'cols':10,'rows':1}))

class CmtForm(forms.Form):
    comment = forms.CharField(label='comment',max_length=200,widget=forms.Textarea(attrs={'cols':35,'rows':2}))

class GForm(forms.Form):
    number = forms.CharField(label='number', max_length=4,widget=forms.TextInput(attrs={'placeholder':'# of movies'}))

class FirstnameForm(forms.Form):
    first = forms.CharField(label='first', max_length=20,widget=forms.TextInput(attrs={'placeholder':'first name'}))

class LastnameForm(forms.Form):
    last = forms.CharField(label='last', max_length=20,widget=forms.TextInput(attrs={'placeholder':'last name'}))
