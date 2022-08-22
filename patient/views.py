
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from patient.models import Feedback,Appointment
from doctor.models import UpdateForm
import pandas as pd
from .ml_model import predect
from patient.models import Symptom_Description,Symptom_Precaution


def patient_dashboard(request):
    if request.user.is_authenticated:
        return render(request,'patient/patient.html',{'username':request.user})
    else:
        return HttpResponseRedirect('/login/')     

def feedback(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user=request.POST['username']
            feedback=request.POST['message']
            us=Feedback(username=user,message=feedback)
            us.save()
            messages.success(request,'Send Successfully!!')
            return HttpResponseRedirect('/user/feedback_form/')
        else:    
            return render(request,'patient/feedback.html',{'username':request.user})
    else:
        return HttpResponseRedirect('/login/')    

def doctorlist(request):
    if request.user.is_authenticated:
        fm= UpdateForm.objects.all()
        return render(request,'patient/doctorlist.html',{'username':request.user,'fm':fm})
    else:
        return HttpResponseRedirect('/login/')     

def appointment(request,id):
  if request.user.is_authenticated:
    if request.method == 'POST':
        da=UpdateForm.objects.get(pk=id)
        print(da)
        fname = request.POST.get("fullname")
        email = request.POST.get("email")
        mobile = request.POST.get("contact")
        message = request.POST.get("message")

        appointment = Appointment.objects.create(
            full_name=fname,
            email=email,
            contact=mobile,
            request=message,
            doctor_id=da
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {request.user} !! For making an appointment, we will email you ASAP!")
        return HttpResponseRedirect("/user/patient/")     
    else:    
        return render(request,'patient/appointment.html',{'username':request.user,'pk':id})
  else:
    return HttpResponseRedirect('/login/')    



        

def searchdisease(request):
    query = request.GET
    data = pd.read_csv('training_data.csv')
    data.drop(['prognosis','Unnamed: 133'], axis=1,inplace=True)
    data = list(data.columns)
    data1=''
    if query and request.user.is_authenticated:
        print(query.getlist('symptomes'))
        try:
            predicted_value = predect(query.getlist('symptomes'))
            
            data1=predicted_value[0][0]
            print(data1)
            description=Symptom_Description.objects.get(Disease=data1)
            pre=Symptom_Precaution.objects.get(Disease=data1)
            print(pre.Precaution_1)
            return render(request,'patient/SearchDisease.html',{'username':request.user, "prediction":data1
            ,"data":data,"description":description.Description, "precaution":[pre.Precaution_1,pre.Precaution_2,pre.Precaution_3
            ,pre.Precaution_4]}
             
            )
            
        except:
            return render(request,'patient/SearchDisease.html',{'username':request.user, "prediction":"Sorry unable to predict."})
        
    else:
        return render(request,'patient/SearchDisease.html',{'username':request.user,"data":data})

    


       


# Create your views here.
