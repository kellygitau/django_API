from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from core.views import *
from core import views

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),  
]
