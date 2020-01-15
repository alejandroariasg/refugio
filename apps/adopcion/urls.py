from django.conf.urls import url
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate

urlpatterns = [
    url(r'^index$', index_adopcion, name="index"),
    url(r'^listar$', SolicitudList.as_view(), name="solicitud_listar"),
    url(r'^nuevo$', SolicitudCreate.as_view(), name="solicitud_crear"),
]
