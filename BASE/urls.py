"""
URL configuration for BASE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include,re_path
from django.conf.urls import handler400,handler403,handler404,handler500

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('db/', admin.site.urls),
    path('',include('Frontpage.urls')),
    path('',include('U_Auth.urls')),
    path('',include('ErrHandler.urls')),
    path('NVA/',include('Core.urls')),
    path('NVA/Accounts/',include('Accounts.urls')),
    path('NVA/Leads/',include('Leads.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'ErrHandler.views.error_400'
handler403 = 'ErrHandler.views.error_403'
handler404 = 'ErrHandler.views.error_404'
handler500 = 'ErrHandler.views.error_500'
