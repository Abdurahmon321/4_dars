from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Region


class IndexView(TemplateView):
    template_name = 'app/index.html'


class RegionDetailViews(View):
    def get(self, request, id):
        region = Region.objects.get(pk=id)
        return render(request, "app/index.html", {"region": region})
