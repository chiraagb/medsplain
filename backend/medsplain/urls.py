# from django.urls import path

# from . import views

# urlpatterns = [
#     path("home/", views.HomeView.as_view(), name="home"),
# ]

from rest_framework.routers import DefaultRouter

from medsplain.views import HomeViewSet

router = DefaultRouter()
router.register(r"medications", HomeViewSet, basename="medication")

urlpatterns = router.urls
