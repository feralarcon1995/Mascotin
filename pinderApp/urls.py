from django.urls import path
from pinderApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.landing, name="Inicio"),
    path('feed', views.feed, name="Feed"),
    path('profile', views.profile, name="Profile"),
    path('register', views.register, name="register"),
    path('login',LoginView.as_view(template_name="pinderApp/login.html"), name="login"),
    path('logout',LogoutView.as_view(template_name="pinderApp/logout.html"), name="logout"),

 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

