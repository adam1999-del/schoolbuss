"""
URL configuration for schoolbuss project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

app_name="school"

urlpatterns = [
    
      path('', school_login, name='user_login'),
      path('logout/', logout, name="logout"),
      path('site/', admin_home , name="home"),
      path('route/', route, name="route"),
      path('students/' , students , name="students"),
      path('student_profile/<int:student_id>/', student_profile , name="student_profile"),
      path('update_student_profile/', update_student_profile , name="update_student_profile"),
      path('patron_profile/<int:patron_id>/', patron_profile , name="patron_profile"),
      path('update_patron_profile/', update_patron_profile , name="update_patron_profile"),
      path('delete_student/', delete_student, name="delete_student"),
      path('delete_patron/', delete_patron, name="delete_patron"),
      path('supervisor/', supervisor , name="supervisor"),
      path('buss/', buss , name="buss"),
      path('delete_bus/',delete_bus , name="delete_bus"),
      path('delete_route/', delete_route , name="delete_route"),
      path('management/', management , name="management"),
      
      path('profile/<int:user_id>/', profile , name="profile"),
      path('update_driver_profile/', update_driver_profile , name="update_driver_profile"),
      path('delete_driver/', delete_driver , name="delete_driver"),
      
      path("fetch_groups/", fetch_groups , name="fetch_groups"),
      path('register_users/', register_users , name="register_users"),
      path('register_bus/', register_bus , name="register_bus"),
      path('register_route/', register_route , name="register_route"),
      path('fetch_drivers/', fetch_drivers , name="fetch_drivers"),
      path('fetch_buss/', fetch_buss , name="fetch_buss"),
    
    
]
