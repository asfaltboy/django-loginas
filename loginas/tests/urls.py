from django.conf.urls import include, url
from django.contrib import admin
from loginas.tests import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.index, name="index"),
    url(r"^current_user/$", views.current_user, name="current_user"),
    url(r"^", include("loginas.urls")),
]
