from django.conf.urls.static import static
from django.urls import path

from familysite import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("card/<int:man_id>/", views.card, name="card"),
    path("updateData", views.updateData, name="updateData"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)