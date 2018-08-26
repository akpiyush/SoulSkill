from django.conf.urls import url

from . import views

app_name = 'tenants'


urlpatterns = [
    #print("111111111111111111111111111111111111111")
    url(r'^adduser/$',views.AddUser.as_view()),
    url(r'^addtenant/$',views.AddTenant.as_view())
]
