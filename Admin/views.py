from django.shortcuts import render,redirect
from Admin.models import *
from Ashaworker.models import *
from django.contrib.auth import logout


def home(request):
        return render(request,'Admin/Homepage.html',{'home':home})

def add(request):
    if request.method=="POST":
        a=int(request.POST.get("txt_num1"))
        b=int(request.POST.get("txt_num2"))
        c=a+b
        return render(request,'Admin/Add.html',{'result':c})
    else:
         return render(request,'Admin/Add.html')

def largest(request):
    if request.method=="POST":
        a=int(request.POST.get("txt_num1"))
        b=int(request.POST.get("txt_num2"))
        if a>b:
           return render(request,'Admin/Largest.html',{'result':a})
        else:
           return render(request,'Admin/Largest.html',{'result':b})
    else:
         return render(request,'Admin/Largest.html')

def calculator(request):
    if request.method=="POST":
        a=int(request.POST.get("txt_num1"))
        b=int(request.POST.get("txt_num2"))
        btn=request.POST.get("button")
        if btn=='+':
            
            return render(request,'Admin/Calculator.html',{'result':a+b})
        elif btn=='-':
            
            return render(request,'Admin/Calculator.html',{'result':a-b})
        elif btn=='*':
          
            return render(request,'Admin/Calculator.html',{'result':a*b})
        elif btn=="/":
           
            return render(request,'Admin/Calculator.html',{'result':a/b})
    else:
         return render(request,'Admin/Calculator.html')

def district(request):
     dis=tbl_district.objects.all()
     if request.method=="POST":
         district=request.POST.get("txt_dis")
         tbl_district.objects.create(district_name=district)
         return render(request,'Admin/District.html',{'result':dis})
     else:
         return render(request,'Admin/District.html',{'result':dis})
def deldis(request,id):
      tbl_district.objects.get(id=id).delete()
      return redirect("Admin:district")

def category(request):
     cat=tbl_category.objects.all()
     if request.method=="POST":
         category=request.POST.get("txt_cat")
         tbl_category.objects.create(category_name=category)
         return render(request,'Admin/Category.html',{'result':cat})
     else:
         return render(request,'Admin/Category.html',{'result':cat})
def delcat(request,id):
      tbl_category.objects.get(id=id).delete()
      return redirect("Admin:category")

def adminreg(request):
     admin=tbl_adminreg.objects.all()
     if request.method=="POST":
         name=request.POST.get("txt_name")
         email=request.POST.get("txt_email")
         password=request.POST.get("txt_password")
         tbl_adminreg.objects.create(adminreg_name=name,adminreg_email=email,adminreg_password=password)
         
         return render(request,'Admin/AdminReg.html',{'result':admin})
     else:
         return render(request,'Admin/AdminReg.html',{'result':admin})
def deladmin(request,id):
       tbl_adminreg.objects.get(id=id).delete()
       return redirect("Admin:adminreg")
        
def place(request):
    dis=tbl_district.objects.all()
    pl=tbl_place.objects.all()
    if request.method=="POST":
         dist=tbl_district.objects.get(id=request.POST.get("sel_district"))
         tbl_place.objects.create(place_name=request.POST.get("txt_place"),district=dist)
         return redirect("Admin:place")
    else:
         return render(request,'Admin/place.html',{'result':dis,'r':pl})
def delplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:place")
def editplace(request,id):
    p=tbl_place.objects.get(id=id)
    p1=tbl_place.objects.all()   
    if request.method=="POST":
        p.place_name=request.POST.get("place_name")
        p.save()
        return redirect("Admin:place")
    else:
        return render(request,'Admin/place.html',{'rr':p,'r':p1})
         

def brand(request):
     bran=tbl_brand.objects.all()
     if request.method=="POST":
         brand=request.POST.get("txt_dis")
         tbl_brand.objects.create(brand_name=brand)
         return render(request,'Admin/Brand.html',{'result':bran})
     else:
         return render(request,'Admin/Brand.html',{'result':bran})
def delbran(request,id):
      tbl_brand.objects.get(id=id).delete()
      return redirect("Admin:brand")
def editbran(request,id):
      bran=tbl_brand.objects.get(id=id)
      bran1=tbl_brand.objects.all()   
      if request.method=="POST":
         bran.brand_name=request.POST.get("txt_dis")
         bran.save()
         return redirect("Admin:brand")
      else:
          return render(request,'Admin/Brand.html',{'r':bran,'result':bran1})

def subcategory(request):
    cat=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    if request.method=="POST":
        sub=tbl_category.objects.get(id=request.POST.get("sel_category"))
        tbl_subcategory.objects.create(subcategory_name=request.POST.get("subcategory_name"),category=sub)
        return redirect("Admin:subcategory")
    else:
        return render(request,'Admin/Subcategory.html',{'result':cat,'r':subcategory})
def delsubcategory(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:subcategory")
def editsub(request,id):
    b=tbl_subcategory.objects.get(id=id)
    b1=tbl_category.objects.all()
    if request.method=="POST":
        b.subcategory_name=request.POST.get("subcategory_name")
        b.save()
        return redirect("Admin:subcategory")
    else:
        return render(request,'Admin/Subcategory.html',{'rr':b,'r':b1})

def panchayath(request):
     pan=tbl_panchayath.objects.all()
     if request.method=="POST":
         panchayath=request.POST.get("txt_dis")
         tbl_panchayath.objects.create(panchayath_name=panchayath)
         return render(request,'Admin/Panchayath.html',{'result':pan})
     else:
         return render(request,'Admin/Panchayath.html',{'result':pan})
def delpan(request,id):
      tbl_panchayath.objects.get(id=id).delete()
      return redirect("Admin:panchayath")

from django.contrib import messages  # For displaying messages

def ward(request):
    pan = tbl_panchayath.objects.all()
    pl = tbl_ward.objects.all()

    if request.method == "POST":
        pan_id = request.POST.get("sel_panchayath")
        ward_number = request.POST.get("txt_place")

        pan_obj = tbl_panchayath.objects.get(id=pan_id)

        # Check if the ward already exists
        if tbl_ward.objects.filter(ward_number=ward_number, panchayath=pan_obj).exists():
            messages.error(request, "Ward already exists for the selected Panchayath.")
        else:
            tbl_ward.objects.create(ward_number=ward_number, panchayath=pan_obj)
            messages.success(request, "Ward added successfully.")

        return redirect("Admin:ward")

    return render(request, 'Admin/Ward.html', {'result': pan, 'r': pl})

def delward(request,id):
    tbl_ward.objects.get(id=id).delete()
    return redirect("Admin:ward")
def editward(request,id):
    p=tbl_ward.objects.get(id=id)
    p1=tbl_ward.objects.all()   
    if request.method=="POST":
        p.ward_number=request.POST.get("ward_number")
        p.save()
        return redirect("Admin:ward")
    else:
        return render(request,'Admin/Ward.html',{'rr':p,'r':p1})

def asha(request):
    pan=tbl_asha.objects.all()
    pl=tbl_ward.objects.all()
    # p=tbl_ward.objects.all()
    # panchayath=tbl_panchayath.objects.all()
    if request.method=="POST":
        #  pan=tbl_ward.objects.filter(id=request.POST.get("sel_ward"))
         name=request.POST.get("txt_name")
         contact=request.POST.get("txt_contact")
         email=request.POST.get("txt_email")
         password=request.POST.get("txt_pass")
         tbl_asha.objects.create(ward_number=request.POST.get("sel_ward"),asha_name=name,asha_contact=contact,asha_email=email,asha_password=password)
         return render(request,'Admin/Ashaworker.html',{'result':pan,'r':pl})
    else:
         return render(request,'Admin/Ashaworker.html',{'result':pan,'r':pl})
def delasha(request,id):
    tbl_asha.objects.get(id=id).delete()
    return redirect("Admin:asha")
def editasha(request,id):
    p=tbl_asha.objects.get(id=id)
    p1=tbl_asha.objects.all()   
    if request.method=="POST":
        p.asha_name=request.POST.get("asha_name")
        p.asha_contact=request.POST.get("asha_contact")
        p.asha_email=request.POST.get("asha_email")
        p.save()
        return redirect("Admin:asha")
    else:
        return render(request,'Admin/Ashaworker.html',{'rr':p,'r':p1})

def notification(request):
    pan=tbl_panchayath.objects.all()
    pl=tbl_notification.objects.all()
    if request.method=="POST":
         pan=tbl_panchayath.objects.get(id=request.POST.get("sel_panchayath"))
         tbl_notification.objects.create(notification_des=request.POST.get("txt_des"),panchayath=pan)
         return redirect("Admin:notification")
    else:
         return render(request,'Admin/Notification.html',{'result':pan,'r':pl})
def delnoti(request,id):
    tbl_notification.objects.get(id=id).delete()
    return redirect("Admin:notification")
def editnoti(request,id):
    p=tbl_notification.objects.get(id=id)
    p1=tbl_notification.objects.all()   
    if request.method=="POST":
        p.notification_des=request.POST.get("notification_des")
        p.save()
        return redirect("Admin:notification")
    else:
        return render(request,'Admin/Notification.html',{'rr':p,'r':p1})

# def work(request,id):
#      asha=tbl_asha.objects.get(id=id)
#      pan=tbl_work.objects.filter(asha=id)
#      if request.method=="POST":
#          work=request.POST.get("txt_work")
#          tbl_work.objects.create(asha=asha,work_des=work)
#          return render(request,'Admin/Work.html',{'result':pan})
#      else:
#          return render(request,'Admin/Work.html',{'result':pan})


def addwork(request,id):
    asha=tbl_asha.objects.get(id=id)
    work=tbl_work.objects.filter(asha=asha)
    if request.method=="POST":
         work=request.POST.get("txt_work")
         tbl_work.objects.create(asha=asha,work_des=work)
         return redirect("Admin:work",id)
    else:
        return render(request,'Admin/Work.html',{'result':work,'id':id})
    
def delwork(request,did,id):

    tbl_work.objects.get(id=did).delete()
    return redirect("Admin:addwork",id)

def viewfeedback(request):
    feedback=tbl_feedback.objects.all()
    return render(request,'Admin/Viewfeedback.html',{'result':feedback})

def viewreports(request):
    reports=tbl_report.objects.all()
    return render(request,'Admin/Viewreports.html',{'result':reports})

def viewcomplaint(request):
    complaint=tbl_complaint.objects.all()
    return render(request,'Admin/ViewComplaints.html',{'result':complaint})

def reply(request,id):
     pan=tbl_complaint.objects.get(id=id)
     if request.method=="POST":
         report=request.POST.get("reply")
         pan.complaint_reply=report
         pan.save()
         return redirect("Admin:viewcomplaint")
     else:
         return render(request,'Admin/Reply.html')

def vaccine(request):
    pan=tbl_vaccine.objects.all()
    if request.method=='POST':
        vaccinetype=request.POST.get("vaccine_type")
        vaccinename=request.POST.get("vaccine_name")
        tbl_vaccine.objects.create(vaccine_type=vaccinetype,vaccine_name=vaccinename)
        return render(request,'Admin/Vaccine.html',{'result':pan})
    else:
        return render(request,'Admin/Vaccine.html',{'result':pan})
    
def delvaccine(request,id):
      tbl_vaccine.objects.get(id=id).delete()
      return redirect("Admin:vaccine")

def customlogout(request):
    logout(request)
    return redirect('Guest:index')
# Create your views here.
