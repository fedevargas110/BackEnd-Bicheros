from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from FGZ.views import *
from django.conf.urls.static import static

router = SimpleRouter()
router.register(r'animals', AnimalViewSet)
router.register(r'ingreso_monto', IngresoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
