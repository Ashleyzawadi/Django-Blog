from django.conf.urls import url
from . import views #from this directory import views.py
from django.conf.urls.static import static
from django.conf import settings

# app_name = arcade
#create views here
urlpatterns=[
    url(r'^$', views.article_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)