from django.conf.urls import url
from . import views

#template tagging
app_name ='basic_app'#django is automatically look for this allow us to use template tagging


urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'other/$',views.other,name='other'),
    ]
