from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from users import api as users_api

urlpatterns = format_suffix_patterns(patterns('',
    # Examples:
    # url(r'^$', 'Meetup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/users/get_user_by_id/(?P<pk>[0-9]+)/$', users_api.UserDetails.as_view()),
    url(r'^api/users/get_friends/(?P<pk>[0-9]+)$', users_api.Friends.as_view()),
    url(r'^api/users/delete_user/(?P<pk>[0-9]+)$', users_api.DeleteUser.as_view()),

))

