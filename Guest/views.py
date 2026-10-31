from django.shortcuts import render,redirect

from Guest.models import *
from Admin.models import *
# Create your views here.
def index(request):
    return render(request,"Guest/index.html")

def registration(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        contact=request.POST.get("contact")
        password=request.POST.get("password")
        repassword=request.POST.get("txt_repass")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        photo=request.FILES.get("user_photo")
        tbl_user.objects.create(user_name=name,user_email=email,user_address=address,user_contact=contact,user_password=password,place=place,user_photo=photo)
    return render(request,'Guest/Registration.html',{'result':dis})
    #else:
    #   return render(request,'Guest/Registration.html')
    
def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place})       

def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        admin_count=tbl_adminreg.objects.filter(adminreg_email=email,adminreg_password=password).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        ashacount=tbl_asha.objects.filter(asha_email=email,asha_password=password).count()
        if admin_count>0:
            admin=tbl_adminreg.objects.get(adminreg_email=email,adminreg_password=password)
            request.session['aid']=admin.id
            return redirect("Admin:home")
        elif usercount > 0:
            user=tbl_user.objects.get(user_email=email,user_password=password)
            request.session["uid"]=user.id
            return redirect("User:home")
        elif ashacount > 0:
            asha=tbl_asha.objects.get(asha_email=email,asha_password=password)
            request.session["asid"]=asha.id
            return redirect("Ashaworker:home")
        else:
            return render(request,'Guest/Login.html')

    else:
        return render(request,'Guest/Login.html')
