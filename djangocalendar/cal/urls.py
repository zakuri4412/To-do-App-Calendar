from django.urls import re_path
from . import views

app_name = 'cal'
urlpatterns = [
    re_path(r'^$', views.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', views.event, name='event_new'),
	re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    re_path(r'^event/delete/(?P<event_id>\d+)/$',views.event_delete,name='event_delete')
]