from django.urls import path
from .views import map_view, reservoir_search

urlpatterns = [
    path('', map_view, name='map'),
    path('api/reservoirs/', reservoir_search, name='reservoir-search'),
]
