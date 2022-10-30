from django.contrib import admin  
from django.urls import path  
from employeeapp import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('',views.show),
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  