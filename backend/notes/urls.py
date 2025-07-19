from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NoteViewset, TagViewset

notes_router = DefaultRouter()
notes_router.register(r'notes', NoteViewset)

tags_router = DefaultRouter()
tags_router.register(r"tags", TagViewset)

urlpatterns = [
    path("", include(notes_router.urls)),
    path("", include(tags_router.urls))
]
