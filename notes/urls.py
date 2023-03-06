"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from Note.views import home_page_view, create_note_view, edit_note_view, searchbar_view, delete_note_view
from User.views import login_view, logout_view, profile_view, alter_profile_view, UserAPIView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='home'),
    path('sign-in/', login_view, name='signin'),
    path('log-out/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/alter/', alter_profile_view, name='alter_profile'),
    path('create-note/', create_note_view, name='create_note'),
    path(r'^edit-note/(?P<id>[0-9]+)$', edit_note_view, name='edit_note'),
    path(r'^delete-note/(?P<id>[0-9]+)$', delete_note_view, name='delete_note'),
    path('searchbar/', searchbar_view, name='searchbar'),

    #Auth
    path('accounts/', include('allauth.urls')),

    #Django REST framework
    path('api/v1/userlist/', UserAPIView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
