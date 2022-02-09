from django.contrib import admin  
from django.urls import path  
from employee import views  

urlpatterns = [  
    path("", views.show),
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('show',views.show),  
    path('employee/edit/<int:id>', views.edit),  
    path('employee/update/<int:id>', views.update),  
    path('employee/delete/<int:id>', views.destroy),  
    path('company/emp', views.companyemp),  
    path('company/show',views.companyshow),
    path('company/edit/<int:id>', views.companyedit),  
    path('company/update/<int:id>', views.companyupdate),  
    path('company/delete/<int:id>', views.companydestroy),
]  