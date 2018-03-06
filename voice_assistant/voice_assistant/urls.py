from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^api/', views.Answer.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]