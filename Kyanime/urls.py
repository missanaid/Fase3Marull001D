
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('anime.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('contact/', include('contact.urls')),
    path('accounts/', include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social'))

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Kyanime"
admin.site.index_title = "Panel de Administrador"
admin.site.site_title = "Kyanime, tu página"
