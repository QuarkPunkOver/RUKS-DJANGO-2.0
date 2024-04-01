"""cinema_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views

from web_site.forms import ResetPasswordForm, SetNewPasswordForm
from web_site.views import MovieInfoView, all_movies, delete_movie
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('api-auth/', include('rest_framework.urls')),
    path('RestAPI/', include('RestAPI.urls')),
    path('API/', all_movies, name='all_movies'), #All movies(for RUKSwatch)
    path('API/<movie_id>', MovieInfoView.as_view(), name='movie-info'),
    path('API/<movie_id>/write_data', MovieInfoView.as_view(), name='write_data'),
    path('API/<movie_id>/delete', delete_movie, name='delete_movie'),

]

urlpatterns += [
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='reset_password/password_reset.html', form_class=ResetPasswordForm), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='reset_password/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='reset_password/password_reset_confirm.html', form_class=SetNewPasswordForm),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='reset_password/password_reset_complete.html'),
         name='password_reset_complete'),
    path("", include("web_site.urls")),
]

handler404 = 'web_site.views.handle_not_found'

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
