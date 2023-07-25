"""wasteManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from .views import(
    user_or_admin,
    logout_view,
    admin_home_page,
    adminEmployee_view,
    map_location,
    smart_bin_ajax,
    user_smart_bin_ajax,
    employee_smart_bin_ajax,
    
)
from users.views import(
    signup_view,
    user_login_view,
    user_logout_view,
    user_home_view,
    user_feedback,
    user_log_out,
)
from smartbins.views import(
    smartbin_view,
    # update,
    get_smartbin_data,
) 
from admins.views import(
    admin_login_view,
    admin_employee,
    admin_add_employee,
    # admin_remove_employee,
    adminRemoveEmployee,
    admin_add_smartbin,
    admin_edit_smartbin,
    admin_edit_employee,

    # admin_remove_smartbin,
    adminRemoveSmartbin,
    admin_smartbin,
    admin_log_out,
    admin_feedback,
    remove_feedback,

    employee_home_page,
    employee_feedbacks,
    employee_log_out,
    
)

urlpatterns = [
    path('admin/', admin.site.urls),


#----------------------------- Common ------------------------------
    path('',user_or_admin),
    path('map_location/<int:id>/',map_location),


#--------------------------- Admin ----------------------------------
    path('admin_login/',admin_login_view),
    path('admin_home_page/',admin_home_page),

    path('admin_employee/',admin_employee),
    path('add_employee/',admin_add_employee),
    path('adminRemoveEmployee/<int:id>/',adminRemoveEmployee),
    path('admin_edit_employee/<int:id>/',admin_edit_employee),

    path('admin_smartbin/',admin_smartbin),
    path('add_smartbin/',admin_add_smartbin),
    path('adminRemoveSmartbin/<int:id>/',adminRemoveSmartbin),
    path('admin_edit_smartbin/<int:id>/',admin_edit_smartbin),

    path('smart_bin_ajax/',smart_bin_ajax),#user

    path('admin_feedback/',admin_feedback),

    

    path('admin_Logout/',admin_log_out),
    path('remove_feedback/',remove_feedback),


#---------------------------User--------------------------------
    path('user_login/',user_login_view),
    path('user_signup/',signup_view),
    path('user_home/',user_home_view),
    path('user_home_page/',user_home_view),
    path('user_logout/',user_logout_view),
    path('user_smart_bin_ajax/',user_smart_bin_ajax),
    path('user_feedback/',user_feedback),
    path('user_Logout/',user_log_out),

    



#---------------------------Employee----------------------------
    path('adminEmployee/',adminEmployee_view),#for employee
    path('Employee_home_page/',employee_home_page),
    path('employee_smart_bin_ajax/',employee_smart_bin_ajax),
    path('employee_feedbacks/',employee_feedbacks),
    path('employee_home_page/',employee_home_page),
    path('employee_Logout/',employee_log_out),


    
    


    


#-----------------------smartbin--------------------------------
    path('smartbin/',smartbin_view),
    # path('update/',update), 
    path('get_smartbin_data/',get_smartbin_data),    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )
