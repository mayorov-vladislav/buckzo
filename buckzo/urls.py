"""
URL configuration for buckzo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework import routers
from mainapp.views import *
from about.views import *
from services.views import *
from work.views import *

# ---------------ROUTER API SETTINGS---------------
# ---------------MAIN APP---------------
router = routers.DefaultRouter()
router.register(r'api/header', HeaderApi),
router.register(r'api/main-info', MainInfoApi),
router.register(r'api/work-category', WorkCategoryApi),
router.register(r'api/work', WorkApi),
router.register(r'api/footer', FooterApi),
# ---------------ABOUT---------------
router.register(r'api/about-header', MainAboutApi),
router.register(r'api/client', ClientApi),
router.register(r'api/team', TeamApi),
router.register(r'api/main-about-info', MainAboutInfoApi),
# ---------------SERVICES---------------
router.register(r'api/services-header', HeaderApi),
router.register(r'api/services-info', ServiceInfoApi),
router.register(r'api/services-client', ServicesClientApi),
# ---------------WORK---------------
router.register(r'api/work-work', HeaderWorkApi),
router.register(r'api/work-category', WorkCategoryWorkApi),
router.register(r'api/work-work', WorkWorkApi),
# ---------------ROUTER API SETTINGS---------------


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('about/', include('about.urls')),
    path('services/', include('services.urls')),
    path('works/', include('work.urls')),
    path('contact-us/', include('contact.urls')),
    path('', include(router.urls))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)