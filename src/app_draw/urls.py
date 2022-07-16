from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    re_path("winners/(?P<draw_id>[-\w]+)", views.GetDraw.as_view(), name="winners"),
]
