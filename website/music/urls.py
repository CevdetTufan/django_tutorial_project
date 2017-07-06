from django.conf.urls import url
from . import views

urlpatterns=[
    #/music/
    url(r'^$',views.index,name='index'),

    #/music/1
    url(r'^(?P<albume_id>[0-9]+)/$',views.detail,name='detail')
]