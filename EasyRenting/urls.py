"""EasyRenting URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from users import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Sección para usuarios
    path('admin/', admin.site.urls),
    path('', views.principal),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('index', login_required(views.index)),
    path('dptos', login_required(views.dptos)),
    path('dptos2', login_required(views.dptos2)),
    path('servicios', login_required(views.servicios)),
    path('reset/password_reset', PasswordResetView.as_view(template_name='users/registration/password_reset_forms.html', email_template_name="users/registration/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='users/registration/password_reset_done.html'), name = 'password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='users/registration/password_reset_confirms.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='users/registration/password_reset_complete.html') , name = 'password_reset_complete'),

]


