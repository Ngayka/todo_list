from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Tag


class TagListView(ListView):
    model = Tag
    queryset = Tag.objects.all()
    template_name = "tags/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tags/tag_form.html"
    success_url = reverse_lazy("tags:tag_list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tags/tag_delete.html"
    success_url = reverse_lazy("tags:tag_list")


class TagUpdateView(UpdateView):
    model = Tag
    template_name = "tags/tag_update.html"
    success_url = reverse_lazy("tags:tag_list")
