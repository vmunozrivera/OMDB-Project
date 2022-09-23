
from django.contrib import admin
from django.urls import path

import gh.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", gh.views.index)
]
