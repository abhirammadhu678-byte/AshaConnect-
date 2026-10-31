from django.shortcuts import render ,redirect
from User.models import *
from Guest.models import *
from Admin.models import *
from Ashaworker.models import *

def home(request):
        return render(request,'User/Homepage.html',{'home':home})

def profile(request):
        user=tbl_user.objects.get(id=request.session['uid'])
        return render(request,'User/Myprofile.html',{'user':user})

def editprofile(request):
    b=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        b.user_name=request.POST.get("user_name")
        b.user_email=request.POST.get("user_email")
        b.user_contact=request.POST.get("user_contact")
        b.user_address=request.POST.get("user_address")
        b.save()
        return render(request,"User/Myprofile.html",{'user':b})
    else:
        return render(request,"User/Editprofile.html",{'user':b})

def changepassword(request):
     error1="Your Password does'nt match"
     error2="Your old password  does'nt match"
     b=tbl_user.objects.get(id=request.session['uid'])
     olda=b.user_password
     oldb= new=request.POST.get("user_old_pasword")
     new=request.POST.get("user_new_password")
     re=request.POST.get("re_type_password")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.user_password=request.POST.get("re_type_password")
                b.save()
                return redirect("User:profile")
            else:
                return render(request,"User/Changepassword.html",{'error1':error1})
        else:
            return render(request,"User/Changepassword.html",{'error2':error2})
     else:
         return render(request,"User/Changepassword.html")

def viewvaccine(request):    
    vaccine=tbl_vaccinedetails.objects.all
    return render(request,'User/Viewpregvaccine.html',{'result':vaccine})

def viewnewbornvaccine(request):    
    vaccine=tbl_newbornvaccine.objects.all
    return render(request,'User/Viewnewbornvaccine.html',{'result':vaccine})

# Create your views here.
