from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name='admin_main'

urlpatterns=[
    url(r'^$', views.ClientList.as_view(), name='client_list'),
    url(r'^index/$', views.downolad_excel, name='index'),
    url(r'^insert/$', views.check_post, name='client_list_insert'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.ClientList_detail.as_view(), name='client_list_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.ClientList_update.as_view(), name='client_list_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ClientList_delete.as_view(), name='client_list_delete'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
