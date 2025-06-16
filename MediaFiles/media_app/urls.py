from django.urls import path, re_path
from .views import logout_view,register_view
from .views import upload_image, protected_image
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', upload_image, name='upload'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    re_path(r'^secure-media/(?P<path>.*)$', protected_image, name='protected_media'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]