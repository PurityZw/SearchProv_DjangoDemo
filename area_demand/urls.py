from django.conf.urls import url
from area_demand import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),  # 首页
    url(r'^areas$', views.areas, name='area'),  # 地址首页
    url(r'^prov$', views.prov),  # 获取所有身份的信息
    url(r'^city/(?P<id>\d+)$', views.city),  # 获取所有城市
    url(r'^dis/(?P<id>\d+)$', views.city),  # 获取所有城市
]