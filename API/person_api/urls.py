from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'universities', views.UniversityViewSet, basename='universities')
# router.register(r'universities/search', views.UniversitySearchView, basename='search')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]
