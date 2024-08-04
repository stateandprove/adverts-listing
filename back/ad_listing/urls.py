from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("advert-list", views.AdvertListViewSet, basename="advert-list")
router.register("advert", views.AdvertRetrieveViewSet, basename="advert-retrieve")

urlpatterns = [path("", include(router.urls))]
