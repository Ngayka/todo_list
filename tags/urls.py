from django.urls import path
from .views import TagListView, TagCreateView, TagDeleteView, TagUpdateView


app_name = 'tags'

urlpatterns = [
    path("", TagListView.as_view(), name='tag_list'),
    path("create/", TagCreateView.as_view(), name="tag_create"),
    path('<int:pk>/delete', TagDeleteView.as_view(), name="tag_delete"),
    path('<int:pk>/update', TagUpdateView.as_view(), name="tag_update"),
]