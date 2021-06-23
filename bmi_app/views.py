from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def calsi(request):
    return render(request,"bmi_app/calsi.html")

@csrf_exempt
def bmi_calculations(request):
    data = request.POST
    person_name = data.get('name')
    Height =float (data.get('height'))
    Weight =float (data.get('weight'))
    Height_to_me= (Height/100)
    
    bmi = Weight / (Height_to_me**2)

    if (bmi <= 18.5):
        classification = "underweight"
    elif(bmi >18.5 and bmi <= 24.9):
        classification = "Normal weight"
    elif(bmi > 24.9 and bmi <= 29.9):
        classification = "overweight"
    else:
        classification = "obisity"
        
    return render(request,"bmi_app/result.html",{"form_data":request.POST,"result":classification,"bmi":round(bmi,2)})