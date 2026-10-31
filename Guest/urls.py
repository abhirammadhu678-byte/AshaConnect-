from django.urls import path,include
from Guest import views
app_name="Guest"

urlpatterns=[
    path('Login/',views.login,name='Login'),
    path('Registration/',views.registration,name='Registration'),
    path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
    path('',views.index,name='index'),
]