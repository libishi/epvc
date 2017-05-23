from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^$', views.home, name ='home'),
    url(r'^departments', views.departments, name ='departments'),
    url(r'^pv', views.pv, name ='pv'),
    url(r'^departments/md', views.md, name ='md'),
    url(r'^departments/bc', views.bc, name ='bc'),
    url(r'^adr', views.adr, name ='adr'),
    url(r'^contactus', views.contactus, name ='contactus'),
    url(r'^mindec', views.mindec, name ='mindec'),
    url(r'^faqs', views.faqs, name ='faqs'),
    url(r'^pv/newsletters/(\d+)', views.pvnewsletters, name ='pvnewsletters'),
    url(r'^pv/ddl', views.pvddl, name ='ddl'),
    
    url(r'^test', views.cn, name ='cn'),
    url(r'^pv/rmp', views.rmp, name ='rmp'),
    url(r'^complains', views.complains, name ='complains'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)