from django.urls import path,include
from Ashaworker import views
app_name="Ashaworker"

urlpatterns=[
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name="profile"),
    path('editprofile/',views.editprofile,name='editprofile'),    
    path('changepassword/',views.changepassword,name='changepassword'),
    path('house/',views.house,name='house'),
    path('addmem/<int:id>',views.addmem,name='addmem'),
    path('report/',views.report,name='report'),
    path('delreport/<int:id>',views.delreport,name='delreport'),
    path('feedback/',views.feedback,name='feedback'),
    path('delfeedback/<int:id>',views.delfeedback,name='delfeedback'),
    path('viewnotification/',views.viewnotification,name='viewnotification'),
    path('viewwork/',views.viewwork,name='viewwork'),

    path('marriedmembers/',views.marriedmembers,name='marriedmembers'),
    path('ajaxhusband/',views.ajaxhusband,name='ajaxhusband'),
    path('ajaxwife/',views.ajaxwife,name='ajaxwife'),
    path('delmem/<int:id>',views.delmem,name='delmem'),
    path('pregnant/',views.pregnant,name='pregnant'),
    path('addvaccine/<int:id>',views.addvaccine,name='addvaccine'),
    path('newbornkid/',views.newbornkid,name='newbornkid'),
    path('addvaccination/<int:id>',views.addvaccination,name='addvaccination'),
    path('ajaxmember/',views.ajaxmember,name='ajaxmember'),
    path('complaint/',views.complaint,name='complaint'),
    path('delcomplaint/<int:id>',views.delcomplaint,name='delcomplaint'),
    path('customlogout/',views.customlogout,name='customlogout'),

    ]