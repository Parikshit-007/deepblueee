from django.contrib import admin
from django.urls import path,include
from webapp.views.login import Login, logout
from webapp. views.signup import Signup
from webapp. views.homepage import index
from webapp. views.dashboard import Dashboard, MyVideosView
from django.conf import settings
from django.conf.urls.static import static
from. views.uploads import upload_video
from .views.summary import process_video#, summary_list
from .views.storage import video_list
from .middlewares.auth import  auth_middleware
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", index , name='index'), 
    path("signup/",Signup.as_view(), name='signup'),
    path("login/", Login.as_view(), name='login'),
    path("logout/", logout, name='logout'),
    path("dashboard/", Dashboard.as_view(), name='dashboard'),
    path("upload/", upload_video, name='upload_video'),
    path('summary/<int:video_id>/', process_video , name='summary'),
    #path('summary/<int:video_id>/list/', summary_list, name='summary_list'),
    path("storage/",MyVideosView.as_view(), name='storage'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)