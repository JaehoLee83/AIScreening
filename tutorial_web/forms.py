from django import forms
from .models import UserInfo, EventInfo

class SurveyForm(forms.Form):
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"(Tuổi)", "id":"age", "name":"age"}), error_messages={'required' : 'Please write your age'})
    height = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"(cm)", "id":"height", "name":"height"}), error_messages={'required' : 'Please write your height'})
    weight = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"(kg)", "id":"weight", "name":"weight"}), error_messages={'required' : 'Please write your weight'})
    waist_circumference = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"(cm)", "id":"waist_circumference", "name":"waist_circumference"}), error_messages={'required' : 'please write your waist circumference'})

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        height = cleaned_data.get('height')
        weight = cleaned_data.get('weight')
        waist_circumference = cleaned_data.get('waist_circumference')


class EventForm(forms.Form):
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"(đồng)", "id":"price", "name":"price"}), error_messages={'required' : 'Please write your estimated price'})

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
