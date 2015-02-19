from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from users import api as users_api

urlpatterns = format_suffix_patterns(patterns('',
    # Examples:
    # url(r'^$', 'Meetup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/users/get_user_by_id/(?P<id>[0-9]+)/$', users_api.UserDetails.as_view()),
    url(r'^api/users/get_friends/(?P<id>[0-9]+)/$', users_api.GetFriends.as_view()),
    url(r'^api/users/delete_user/(?P<id>[0-9]+)/$', users_api.DeleteUser.as_view()),
    url(r'^api/users/delete_friend/(?P<id>[0-9]+)/?(?P<friend_id>[0-9]+)/$', users_api.DeleteFriend.as_view()),
    url(r'^api/users/create_user/$', users_api.CreateUser.as_view()),
    url(r'^api/users/add_friends/(?P<id>[0-9]+)/$', users_api.AddFriends.as_view()),
))

