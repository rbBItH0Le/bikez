from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns= [
    path("details",views.details,name="details"),
    path("track",views.track,name="track"),
    path("repair",views.repair,name="repair"),
    path("repairstatus",views.repairstatus,name="repairstatus"),
    path("move",views.move,name="move"),
    path("add",views.add,name="add"),
    path("delete",views.delete,name="delete"),
    path("show",views.show,name="show"),
    path("report",views.report,name="report"),
    path("rent",views.rent,name="rent")
]
