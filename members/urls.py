"""members URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.static import serve
from django.conf.urls import url
from django.contrib import admin
from members import settings
from subscribers.views import (GetSubsByAccountId, GetSubById, GetSubByPhoneNumber, GetSubByClientMemberId,
    CreateMember, SubscriberBatchProcess)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/get_members_by_acc_id/(?P<account_id>\w+)/$', GetSubsByAccountId.as_view(),
        name='get_members_by_acc_id'),
    url(r'^api/get_member_by_id/(?P<id>\w+)/$', GetSubById.as_view(),
        name='get_member_by_id'),
    url(r'^api/get_member_by_phone/(?P<phone_number>\w+)/$', GetSubByPhoneNumber.as_view(),
        name='get_member_by_phone'),
    url(r'^api/get_member_by_client_id/(?P<client_member_id>\w+)/$', GetSubByClientMemberId.as_view(),
        name='get_member_by_client_id'),
    url(r'^api/create_member/', CreateMember.as_view(),
        name='create_member'),
    url(r'^api/generate_sub_batch/', SubscriberBatchProcess.as_view(),
        name='generate'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
