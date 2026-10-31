from django.db import models
from Admin.models import*

class tbl_house(models.Model):
    house_number=models.CharField(max_length=50)
    house_address=models.CharField(max_length=50)
    house_count=models.CharField(max_length=50)
    asha=models.ForeignKey(tbl_asha,on_delete=models.CASCADE)


class tbl_member(models.Model):
    member_name=models.CharField(max_length=50)
    member_age=models.CharField(max_length=50)
    member_job=models.CharField(max_length=50)
    member_health=models.CharField(max_length=50)
    member_gender=models.CharField(max_length=50)
    member_email=models.CharField(max_length=50)
    house=models.ForeignKey(tbl_house,on_delete=models.CASCADE)
    asha=models.ForeignKey(tbl_asha,on_delete=models.CASCADE)


class tbl_report(models.Model):
    report_des=models.CharField(max_length=50)
    report_date=models.DateField(auto_now_add=True)
    asha=models.ForeignKey(tbl_asha,on_delete=models.CASCADE)


class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=50)
    asha=models.ForeignKey(tbl_asha,on_delete=models.CASCADE,null=True)

class tbl_marriedmembers(models.Model):
    house=models.ForeignKey(tbl_house,on_delete=models.CASCADE,null=True)
    member_husband=models.ForeignKey(tbl_member,on_delete=models.CASCADE,null=True,related_name="husband_member")
    member_wife=models.ForeignKey(tbl_member,on_delete=models.CASCADE,null=True,related_name="wife_member")
    asha=models.ForeignKey(tbl_asha,on_delete=models.CASCADE)


class tbl_pregnantwomen(models.Model):
    house=models.ForeignKey(tbl_house,on_delete=models.CASCADE,null=True)
    member_wife=models.ForeignKey(tbl_member,on_delete=models.CASCADE,null=True,related_name="pregnant")
    asha=models.ForeignKey(tbl_asha,on_delete=models.CASCADE)
    
class tbl_newbornkids(models.Model):
    house=models.ForeignKey(tbl_house,on_delete=models.CASCADE,null=True)
    member_kid=models.ForeignKey(tbl_member,on_delete=models.CASCADE,null=True,related_name="member")
    member_parent=models.ForeignKey(tbl_member,on_delete=models.CASCADE,null=True,related_name="parent")
    asha=models.ForeignKey(tbl_asha,on_delete=models.CASCADE)


class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50) 
    complaint_content=models.CharField(max_length=50) 
    complaint_date=models.DateField(auto_now_add=True)  
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=50) 
    asha=models.ForeignKey(tbl_asha,on_delete=models.CASCADE,null=True)

class tbl_vaccinedetails(models.Model):
    vaccine_date=models.CharField(max_length=50)
    pregnantwomen=models.ForeignKey(tbl_pregnantwomen,on_delete=models.CASCADE)
    vaccine=models.ForeignKey(tbl_vaccine,on_delete=models.CASCADE)

class tbl_newbornvaccine(models.Model):
    vaccine_date=models.CharField(max_length=50)
    newbornkid=models.ForeignKey(tbl_newbornkids,on_delete=models.CASCADE)
    vaccine=models.ForeignKey(tbl_vaccine,on_delete=models.CASCADE)
# Create your models here.
