from django.urls import path
from .views import TaskViewSet, TagViewSet


app_name = 'tasks'

urlpatterns = [
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='tasks'),
    path('tasks/<int:pk>/', TaskViewSet.as_view({
         "get": "retrieve",
         "put": "update",
         "patch": "partial_update",
         "delete": "destroy"}),
         name = "task"),
    path('tags/', TagViewSet.as_view({'get': 'list', 'post': 'create'}), name='tags'),
    path('tags/<int:pk>/', TagViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"}),
         name="tag"),
]