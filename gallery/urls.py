from django.conf.urls import url, include
from . import views

app_name = 'gallery'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_image, name='addImage'),
]
