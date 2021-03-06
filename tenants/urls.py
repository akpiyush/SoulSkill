from django.conf.urls import url

from . import views

app_name = 'tenants'


urlpatterns = [
    url(r'^adduser/$',views.AddUser.as_view()),
    url(r'^edituser/$',views.EditUser.as_view()),
    url(r'^deleteuser/$',views.DeleteUser.as_view()),
    url(r'^viewtenentuser/$',views.ViewTenentUser.as_view()),
    url(r'^addtenant/$',views.AddTenant.as_view()),
]
