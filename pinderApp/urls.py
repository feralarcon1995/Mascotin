from django.urls import path
from pinderApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.landing, name="inicio"),
    path("about", views.about, name="about"),
    path('feed', views.feed, name="feed"),
    path('profile/', views.profile, name='profile'),
	path('profile/<str:username>', views.profile, name='profile'),
    path("post", views.post, name="post"),
    path('register', views.register, name="register"),
    path('login',LoginView.as_view(template_name="pinderApp/login.html"), name="login"),
    path('logout',LogoutView.as_view(template_name="pinderApp/logout.html"), name="logout"),

 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

