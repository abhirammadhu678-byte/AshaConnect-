from django.urls import path,include
from User import views
app_name="User"

urlpatterns=[
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name="profile"),
    path('editprofile/',views.editprofile,name='editprofile'),    
    path('changepassword/',views.changepassword,name='changepassword'),
    path('viewvaccine/',views.viewvaccine,name='viewvaccine'),
    path('viewnewbornvaccine/',views.viewnewbornvaccine,name='viewnewbornvaccine'),

    ]