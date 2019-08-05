from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from FGZ.views import *
from django.conf.urls.static import static

router = SimpleRouter()
router.register(r'animals', AnimalViewSet)
router.register(r'monto', MontoViewSet)
router.register(r'cap', CAPViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
