from django.shortcuts import render
from .models import UserInfo
from .forms import SurveyForm
import pickle
import os 

print(os.getcwd())
with open('./model/classifier.pkl', 'rb') as f:
    clf = pickle.load(f)
with open('./model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

def diabetes_screening(age, bmi, waist, family_diabetes, smoking):
    input = scaler.transform([[age, bmi, waist, family_diabetes, smoking]])
    predict = clf.predict(input)
    return predict[0]

def make_korean_diabetes_index(age, waist_circumference, gender, tobacco, drink, family_diabetes, hypertension):
    risk_score = 0
    if age < 35:
        pass
    elif age < 45:
        risk_score += 2
    else:
        risk_score += 3
    if family_diabetes == 1:
        risk_score += 1
    if hypertension == 1:
        risk_score += 1
    if gender == 0:
        if waist_circumference < 84:
            pass
        elif waist_circumference < 90:
            risk_score += 2 
        else:
            risk_score += 3
    else:
        if waist_circumference < 77:
            pass
        elif waist_circumference < 84:
            risk_score += 2 
        else:
            risk_score += 3

    if tobacco == 1:
        risk_score += 1
    if drink == 1:
        risk_score += 1
    elif drink == 2:
        risk_score += 2

    return risk_score

def Get_data_with_null_check(data, dtype='int'):
    if data == "":
        return 1 
    else:
        if dtype == 'int':
            return int(data)
        else:
            return float(data)
    
# Create your views here.
def index(request):
    form = SurveyForm()
    if request.method == 'GET':
        
        return render(request, 'index.html', {'form': form})

    if request.method == 'POST':
        age = Get_data_with_null_check(request.POST.get('age'))
        height = Get_data_with_null_check(request.POST.get('height'),'float')
        weight = Get_data_with_null_check(request.POST.get('weight'),'float')
        waist_circumference = Get_data_with_null_check(request.POST.get('waist_circumference'),'float')

        gender = Get_data_with_null_check(request.POST.get('gender'))
        drink = Get_data_with_null_check(request.POST.get('drink'))
        tobacco = Get_data_with_null_check(request.POST.get('tobacco'))
        family_diabetes = Get_data_with_null_check(request.POST.get('family_diabetes'))
        gestational = Get_data_with_null_check(request.POST.get('gestational'))
        exercise = Get_data_with_null_check(request.POST.get('exercise'))
        hypertension = Get_data_with_null_check(request.POST.get('hypertension'))

        

        risk_score = make_korean_diabetes_index(age, waist_circumference, gender, tobacco, drink, family_diabetes, hypertension)
        
        bmi = float(weight) / (float(height)/100)**2
        AI_risk_score = diabetes_screening(age, bmi, waist_circumference, family_diabetes, tobacco )

        # 
        ## 위험지수 저장하기 
        userinfo = {
            'age' : age,
            'height' : height,
            'weight' : weight,
            'waist_circumference' : waist_circumference,
            'bmi' : bmi,
            'gender' : gender,
            'drink' : drink,
            'tobacco' : tobacco,
            'family_diabetes' : family_diabetes,
            'gestational' : gestational,
            'exercise' : exercise,
            'hypertension' : hypertension,
            'risk_score' : risk_score,
            'AI_risk_score' : AI_risk_score,
            'form' : form
        }

        return render(request, 'index.html', userinfo)
    else:
        return render(request, 'index.html')