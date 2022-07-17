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
    path("edit", views.editProfile, name="update_profile"),
    path("post", views.post, name="post"),
    path("post/<int:pk>", views.postDetail, name="post-detail"),
    path('register', views.register, name="register"),
    path('gatos', views.gatos, name="gatos"),
    path('perros', views.perros, name="perros"),
    path('login',LoginView.as_view(template_name="pinderApp/login.html"), name="login"),
    path('logout',LogoutView.as_view(template_name="pinderApp/logout.html"), name="logout"),

 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

