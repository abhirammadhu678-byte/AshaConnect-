from django.urls import path,include
from Admin import views
app_name="Admin"

urlpatterns = [
    path('add/',views.add,name='add'),
    path('largest/',views.largest,name='largest'),
    path('calculator/',views.calculator,name='calculator'),
    path('category/',views.category,name='category'),
    path('subcategory/',views.subcategory,name='subcategory'),
    path('delsubcategory/<int:id>',views.delsubcategory,name='delsubcategory'),
    path('editsub/<int:id>',views.editsub,name='editsub'),
#home
    path('home/',views.home,name='home'),

#admin
     path('adminreg/',views.adminreg,name='adminreg'),
     path('deladmin/<int:id>',views.deladmin,name='deladmin'),
     path('delcat/<int:id>',views.delcat,name='delcat'),
#district
     path('district/',views.district,name='district'),
     path('deldis/<int:id>',views.deldis,name='deldis'),

#place
     path('place/',views.place,name='place'),
     path('delplace/<int:id>',views.delplace,name='delplace'),
     path('editplace/<int:id>',views.editplace,name='editplace'),
      path('brand/',views.brand,name='brand'),
      path('delbran/<int:id>',views.delbran,name='delbran'),
      path('editbran/<int:id>',views.editbran,name='editbran'),
#panchayath
      path('panchayath/',views.panchayath,name='panchayath'),
      path('delpan/<int:id>',views.delpan,name='delpan'),
#ward
      path('ward/',views.ward,name='ward'),
      path('delward/<int:id>',views.delward,name='delward'),
      path('editward/<int:id>',views.editward,name='editward'),
#asha
      path('asha/',views.asha,name='asha'),
      path('delasha/<int:id>',views.delasha,name='delasha'),
      path('editasha/<int:id>',views.editasha,name='editasha'),
#notification
      path('notification/',views.notification,name='notification'),
      path('delnoti/<int:id>',views.delnoti,name='delnoti'),
      path('editnoti/<int:id>',views.editnoti,name='editnoti'),
#work
      path('work/<int:id>',views.addwork,name='work'),
      path('addwork/<int:id>',views.addwork,name='addwork'),
      path('delwork/<int:did>/<int:id>',views.delwork,name='delwork'),

      path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
      path('viewreports/',views.viewreports,name='viewreports'),
      path('viewcomplaint/',views.viewcomplaint,name='viewcomplaint'),
      path('reply/<int:id>',views.reply,name='reply'),
      path('vaccine/',views.vaccine,name='vaccine'),
      path('delvaccine/<int:id>',views.delvaccine,name='delvaccine'),
      path('customlogout/',views.customlogout,name='customlogout'),

]
