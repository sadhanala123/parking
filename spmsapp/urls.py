from django.urls import path

from . import views

urlpatterns=[
    path('',views.dashboard, name='dashboard'),
    path('category/',views.Cat, name='category'),
    path('managevehicle/',views.add,name='managevehicle'),
    path('reports', views.Reports, name='reports'),
    path('vehicleentry/',views.vehicleentry ,name='vehicleentry'),
    path('Accountsettings/', views.Accountsettings, name='accountsettings'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('deactive/<int:pk>', views.deactive, name='deactive'),
    path('activated/<int:pk>', views.activated, name='activated'),
    path('Leaved/<int:pk>', views.Leaved, name='Leaved'),
    path('Done/<int:pk>', views.Done, name='Done'),
    path('categarysearch/', views.CategarySearch, name='categarysearch'),
    path('managesearch/', views.ManageSearch, name='managesearch'),
    path('search/',views.search,name='search'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register')
]
