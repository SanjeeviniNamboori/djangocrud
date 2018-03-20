#from django.urls import path
from django.conf.urls import include, url
from my_app.views import MyFriend, MyFriendDetail

urlpatterns = [
    url(r'^$', MyFriend.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', MyFriendDetail.as_view()),
]