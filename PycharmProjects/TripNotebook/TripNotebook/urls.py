"""TripNotebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from Trip.views import indexPage,about,trip,tripDetails,codes,contact,\
                       gallery,services,costlist,presentlist,travellist,fullPlan,printPdf,test,\
                       createTripMain,createPlan


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', indexPage),
    url(r'^about/$', about),
    url(r'^trip/$', trip),
    url(r'^single/(?P<pk>\d+)/$',tripDetails),
    url(r'^codes/$',codes),
    url(r'^contact/$',contact),
    url(r'^gallery/$',gallery),
    url(r'^services/$',services),
    url(r'^costlist/$',costlist),
    url(r'^presentlist/$',presentlist),
    url(r'^travellist/$',travellist),
    url(r'^fullPlan/(?P<pk>\d+)/$',fullPlan),
    url(r'^printPdf/(?P<pk>\d+)/$',printPdf),
    url(r'^createMain/$', createTripMain),
    url(r'^createPlan/(?P<pk>\d+)/$', createPlan),
]
