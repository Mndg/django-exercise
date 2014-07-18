from django.conf.urls import *
from view import hello, current_datetime, hours_ahead

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    ('another-time-page/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
