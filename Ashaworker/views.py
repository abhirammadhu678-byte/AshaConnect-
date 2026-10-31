from django.shortcuts import render ,redirect
from User.models import *
from Guest.models import *
from Admin.models import *
from django.contrib.auth import logout
from Ashaworker.models import *

def home(request):
        return render(request,'Ashaworker/Homepage.html',{'home':home})

def profile(request):
        user=tbl_asha.objects.get(id=request.session['asid'])
        return render(request,'Ashaworker/Myprofile.html',{'Ashaworker':user})

def editprofile(request):
    b=tbl_asha.objects.get(id=request.session['asid'])
    if request.method=="POST":
        b.asha_name=request.POST.get("txt_name")
        b.asha_email=request.POST.get("txt_email")
        b.asha_contact=request.POST.get("txt_contact")
        
        b.save()
        
        return redirect("Ashaworker:profile")
    else:
        return render(request,"Ashaworker/Editprofile.html",{'user':b})

def changepassword(request):
     error1="Your Password does'nt match"
     error2="Your old password  does'nt match"
     b=tbl_asha.objects.get(id=request.session['asid'])
     olda=b.asha_password
     oldb= new=request.POST.get("asha_old_pasword")
     new=request.POST.get("asha_new_password")
     re=request.POST.get("re_type_password")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.asha_password=request.POST.get("re_type_password")
                b.save()
                return redirect("Ashaworker:profile")
            else:
                return render(request,"Ashaworker/Changepassword.html",{'error1':error1})
        else:
            return render(request,"Ashaworker/Changepassword.html",{'error2':error2})
     else:
         return render(request,"Ashaworker/Changepassword.html")

def house(request):
     pan=tbl_house.objects.filter(asha=request.session['asid'])
     if request.method=="POST":
         house=request.POST.get("txt_house")
         address=request.POST.get("txt_address")
         count=request.POST.get("txt_count")
         asha=request.session['asid']
         tbl_house.objects.create(house_number=house,house_address=address,house_count=count,asha_id=asha)
         return render(request,'Ashaworker/House.html',{'result':pan})
     else:
         return render(request,'Ashaworker/House.html',{'result':pan})
def addmem(request,id):
    house=tbl_house.objects.get(id=id)
    mem=tbl_member.objects.filter(house=house)
    if request.method=="POST":
         name=request.POST.get("txt_name")
         age=request.POST.get("txt_age")
         job=request.POST.get("txt_job")
         health=request.POST.get("txt_health")
         gender=request.POST.get("txt_gender")
         email=request.POST.get("txt_email")
         asha=request.session['asid']
         tbl_member.objects.create(house=house,member_name=name,member_age=age,member_job=job,member_health=health,member_gender=gender,member_email=email,asha_id=asha)
         return render(request,'Ashaworker/Familymember.html',{'result':mem})  
    else:
        return render(request,'Ashaworker/Familymember.html',{'result':mem})

def report(request):
     pan=tbl_report.objects.filter(asha=request.session['asid'])
     if request.method=="POST":
         report=request.POST.get("txt_des")
         asha=request.session['asid']
         tbl_report.objects.create(report_des=report,asha_id=asha)
         return render(request,'Ashaworker/Report.html',{'result':pan})
     else:
         return render(request,'Ashaworker/Report.html',{'result':pan})
def delreport(request,id):
      tbl_report.objects.get(id=id).delete()
      return redirect("Ashaworker:report")

def feedback(request):
     pan=tbl_feedback.objects.all()
     if request.method=="POST":
         report=request.POST.get("txt_des")
         asha=request.session['asid']
         tbl_feedback.objects.create(feedback_content=report,asha_id=asha)
         return render(request,'Ashaworker/Feedback.html',{'result':pan})
     else:
         return render(request,'Ashaworker/Feedback.html',{'result':pan})

def delfeedback(request,id):
      tbl_feedback.objects.get(id=id).delete()
      return redirect("Ashaworker:feedback")

def viewnotification(request):
    
    notification=tbl_notification.objects.all()
    return render(request,'Ashaworker/Viewnotification.html',{'result':notification})

def viewwork(request):  
    work=tbl_work.objects.filter(asha=request.session['asid'])
    return render(request,'Ashaworker/ViewWork.html',{'result':work})

def marriedmembers(request):
    marriedmembers = tbl_marriedmembers.objects.filter(asha=request.session['asid'])
    house=tbl_house.objects.filter(asha=request.session['asid'])
    if request.method == "POST":
        # house = tbl_house.objects.get(id=request.POST.get("sel_house"))
        mem = tbl_member.objects.get(id=request.POST.get("sel_husband"))
        mem2 = tbl_member.objects.get(id=request.POST.get("sel_wife"))
        asha=request.session['asid']
        tbl_marriedmembers.objects.create(member_husband=mem,member_wife=mem2,asha_id=asha)
        return render(request, 'Ashaworker/Addmembers.html', {'result': marriedmembers,'house':house})
    else:
        return render(request, 'Ashaworker/Addmembers.html', {'result': marriedmembers,'house':house})
def delmem(request,id):
    tbl_marriedmembers.objects.get(id=id).delete()
    return redirect("Ashaworker:marriedmembers")
         
def ajaxhusband(request):
    husband=tbl_member.objects.filter(house=request.GET.get("did"),member_gender="Male")
    return render(request,'Ashaworker/Ajaxhusband.html',{'husband':husband})  

def ajaxwife(request):
    wife=tbl_member.objects.filter(house=request.GET.get("did"),member_gender="Female")
    return render(request,'Ashaworker/Ajaxwife.html',{'wife':wife})      
def ajaxmember(request):
    member=tbl_member.objects.filter(house=request.GET.get("did"))
    return render(request,'Ashaworker/Ajaxmember.html',{'member':member})      

def pregnant(request):
    pregnantwomen = tbl_pregnantwomen.objects.filter(asha=request.session['asid'])
    house=tbl_house.objects.filter(asha=request.session['asid'])
    if request.method == "POST":
        # house = tbl_house.objects.get(id=request.POST.get("sel_house"))
        mem = tbl_member.objects.get(id=request.POST.get("sel_member"))
        asha=request.session['asid']
        tbl_pregnantwomen.objects.create(member_wife=mem,asha_id=asha)
        
        return render(request, 'Ashaworker/Addpregnantwomen.html', {'result': pregnantwomen,'house':house})
    else:
        return render(request, 'Ashaworker/Addpregnantwomen.html', {'result': pregnantwomen,'house':house})
def addvaccine(request,id):
    vaccinedetails=tbl_vaccinedetails.objects.filter(pregnantwomen=id)
    vaccine=tbl_vaccine.objects.filter(vaccine_type="PregnantWomen")
    if request.method=="POST":
        vaccine=tbl_vaccine.objects.get(id=request.POST.get("sel_vaccine"))
        vaccinedate=request.POST.get("vaccine_date")
        tbl_vaccinedetails.objects.create(vaccine=vaccine,vaccine_date=vaccinedate,pregnantwomen=tbl_pregnantwomen.objects.get(id=id))
        return redirect("Ashaworker:addvaccine",id)  
    else:
        return render(request,'Ashaworker/Vaccinedetails.html',{'vaccine':vaccine,'vaccinedetails':vaccinedetails})

def newbornkid(request):
    newbornkid = tbl_newbornkids.objects.all()
    house=tbl_house.objects.filter(asha=request.session['asid'])
    if request.method == "POST":
        # house = tbl_house.objects.get(id=request.POST.get("sel_house"))
        mem = tbl_member.objects.get(id=request.POST.get("sel_member"))
        mem2 = tbl_member.objects.get(id=request.POST.get("sel_parent"))
        asha=request.session['asid']

        tbl_newbornkids.objects.create(member_kid=mem,member_parent=mem2,asha_id=asha)
        return render(request, 'Ashaworker/Addnewbornkid.html', {'result': newbornkid,'house':house})
    else:
        return render(request, 'Ashaworker/Addnewbornkid.html', {'result': newbornkid,'house':house})
def addvaccination(request,id):
    newbornvaccine=tbl_newbornvaccine.objects.filter(newbornkid=id)
    vaccine=tbl_vaccine.objects.filter(vaccine_type="Newborn")
    if request.method=="POST":
        vaccine=tbl_vaccine.objects.get(id=request.POST.get("sel_vaccine"))
        vaccinedate=request.POST.get("vaccine_date")
        tbl_newbornvaccine.objects.create(vaccine=vaccine,vaccine_date=vaccinedate,newbornkid=tbl_newbornkids.objects.get(id=id))
        return redirect("Ashaworker:addvaccination",id)  
    else:
        return render(request,'Ashaworker/NewbornVaccine.html',{'vaccine':vaccine,'vaccinedetails':newbornvaccine})

def complaint(request):
    comp=tbl_complaint.objects.all()
    if request.method=='POST':
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        asha_id = request.session.get('asid')
        asha = tbl_asha.objects.get(id=asha_id)
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,asha=asha)       
        return render(request,'Ashaworker/Complaint.html',{'result':comp})
    else:
        return render(request,'Ashaworker/Complaint.html',{'result':comp})

def delcomplaint(request,id):
    tbl_complaint.objects.get(id=id).delete()
    return redirect("Ashaworker:complaint")

def customlogout(request):
    logout(request)
    return redirect('Guest:index')