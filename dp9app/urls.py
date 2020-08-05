from django.urls import path
from dp9app import views

app_name="dp9app"


urlpatterns=[
    path('trial/',views.trial,name="trial"),
    path('profile/',views.profile,name="profile"),
]