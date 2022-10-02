
# Django
from django.contrib import admin
from django.urls import path

# Views
import gh.views
import movies.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", gh.views.index),
    path("search/", movies.views.search, name="search"),
    path("search-wait/<uuid:result_uuid>/", movies.views.search_wait, name="search_wait"),
    path("search-results/", movies.views.search_results, name="search_results")
]
