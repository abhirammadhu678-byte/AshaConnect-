from django.db import models

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)

class tbl_adminreg(models.Model):
    adminreg_name=models.CharField(max_length=50)
    adminreg_email=models.CharField(max_length=50)
    adminreg_password=models.CharField(max_length=50)

class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)    

class tbl_panchayath(models.Model):
    panchayath_name=models.CharField(max_length=50)

class tbl_ward(models.Model):
    ward_number=models.CharField(max_length=50)
    panchayath = models.ForeignKey(tbl_panchayath,on_delete=models.CASCADE)

class tbl_asha(models.Model):
    ward_number=models.CharField(max_length=50)
    asha_name=models.CharField(max_length=50)
    asha_contact=models.CharField(max_length=50)
    asha_email=models.CharField(max_length=50)
    asha_password=models.CharField(max_length=50)
    # panchayath_name=models.CharField(max_length=50)
    # panchayath = models.ForeignKey(tbl_panchayath,on_delete=models.CASCADE)

class tbl_notification(models.Model):
    notification_des=models.CharField(max_length=50)
    panchayath = models.ForeignKey(tbl_panchayath,on_delete=models.CASCADE)

class tbl_work(models.Model):
    work_des=models.CharField(max_length=50)
    asha=models.ForeignKey(tbl_asha,on_delete=models.CASCADE)

class tbl_reply(models.Model):
    reply_content=models.CharField(max_length=50)

class tbl_vaccine(models.Model):
    vaccine_name=models.CharField(max_length=50)
    vaccine_type=models.CharField(max_length=50)
    

# Create your models here.
