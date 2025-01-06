from django.urls import path

from . import views

urlpatterns = [
    path("google-auth/", views.GoogleAuth.as_view(), name="google-auth"),
    path("reports/", views.ReportsView.as_view(), name="report-view"),
]
