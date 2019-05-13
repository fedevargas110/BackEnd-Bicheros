from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from FGZ.views import *

router = SimpleRouter()
router.register(r'animals', AnimalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
