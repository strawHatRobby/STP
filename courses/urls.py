from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.courses,name='course'),
    url(r'^assignment/$',views.assignments,name='assignment'),
    url(r'^assignment/(?P<pk>\d+)/$',views.assignment_details),
    ]