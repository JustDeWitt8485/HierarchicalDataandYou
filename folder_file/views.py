from django.shortcuts import render

from django.views.generic import TemplateView, View

from folder_file.models import File

# Create your views here.


class IndexView(View):
    def get(self, request):
        html = 'index.html'
        files = File.objects.all()
        context = {'files': files}
        return render(request, html, context)
