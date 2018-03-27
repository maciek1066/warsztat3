"""address_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from main_app.views import ShowPeople, ModifyPerson, DeletePerson, ShowPersonDetails, NewPerson, AddAddress, \
                        ModifyAddress, DeleteAddress, AddPhone, ModifyPhone, DeletePhone, AddEmail, ModifyEmail, \
                        DeleteEmail, ShowGroup, NewGroup, ShowGroupDetails, DeleteGroup, GroupSearch, AddToGroup, \
                        RemoveFromGroup

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', ShowPeople.as_view()),
    url(r'^modify/(?P<person_id>(\d)+)/$', ModifyPerson.as_view()),
    url(r'^delete/(?P<person_id>(\d)+)/$', DeletePerson.as_view()),
    url(r'^show/(?P<person_id>(\d)+)/$', ShowPersonDetails.as_view()),
    url(r'^new/$', NewPerson.as_view()),
    url(r'^modify/(?P<person_id>(\d)+)/addAddress/$', AddAddress.as_view()),
    url(r'^modify/(?P<person_id>(\d)+)/modifyAddress/(?P<address_id>(\d)+)/$', ModifyAddress.as_view()),
    url(r'^modify/(?P<person_id>(\d)+)/deleteAddress/(?P<address_id>(\d)+)/$', DeleteAddress.as_view()),
    url(r'^modify/(?P<person_id>(\d)+)/addPhone/$', AddPhone.as_view()),
    url(r'^modify/(?P<person_id>(\d)+)/modifyPhone/(?P<phone_id>(\d)+)/$', ModifyPhone.as_view()),
    url(r'^modify/(?P<person_id>(\d)+)/deletePhone/(?P<phone_id>(\d)+)/$', DeletePhone.as_view()),
    url(r'^modify/(?P<person_id>(\d)+)/addEmail/$', AddEmail.as_view()),
    url(r'^modify/(?P<person_id>(\d)+)/modifyEmail/(?P<email_id>(\d)+)/$', ModifyEmail.as_view()),
    url(r'^modify/(?P<person_id>(\d)+)/deleteEmail/(?P<email_id>(\d)+)/$', DeleteEmail.as_view()),
    url(r'^group/$', ShowGroup.as_view()),
    url(r'^group/new/$', NewGroup.as_view()),
    url(r'^group/(?P<group_id>(\d)+)/$', ShowGroupDetails.as_view()),
    url(r'^group/delete/(?P<group_id>(\d)+)/$', DeleteGroup.as_view()),
    url(r'^group-search/$', GroupSearch.as_view()),
    url(r'^addTo/(?P<person_id>\d+)/$', AddToGroup.as_view()),
    url(r'^removeFrom/(?P<group_id>\d+)/(?P<person_id>\d+)/$', RemoveFromGroup.as_view()),
]
