from django import forms
from .models import UserInfo

class SurveyForm(forms.Form):
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"(세)", "id":"age", "name":"age"}), error_messages={'required' : '나이를 입력해 주세요.'})
    height = forms.FloatField(widget=forms.NumberInput(attrs={"placeholder":"(cm)", "id":"height", "name":"height"}), error_messages={'required' : '키를 입력해 주세요.'})
    weight = forms.FloatField(widget=forms.NumberInput(attrs={"placeholder":"(kg)", "id":"weight", "name":"weight"}), error_messages={'required' : '몸무게를 입력해 주세요.'})
    waist_circumference = forms.FloatField(widget=forms.NumberInput(attrs={"placeholder":"(cm)", "id":"waist_circumference", "name":"waist_circumference"}), error_messages={'required' : '허리둘레를 입력해 주세요.'})

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        height = cleaned_data.get('height')
        weight = cleaned_data.get('weight')
        waist_circumference = cleaned_data.get('waist_circumference')


