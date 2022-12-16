from django.urls import include, path

from rest_framework import routers

from my_project_api.views import CountriesViewSet

router = routers.DefaultRouter()
router.register(r'country', CountriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]