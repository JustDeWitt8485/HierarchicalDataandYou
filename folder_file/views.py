from django.shortcuts import HttpResponseRedirect, render, reverse

from django.views.generic import TemplateView, View

from folder_file.forms import AddFilesForm

from folder_file.models import File
# Create your views here.


class IndexView(View):
    def get(self, request):
        html = 'index.html'
        files = File.objects.all()
        context = {'files': files}
        return render(request, html, context)


class AddFile(View):

    form_class = AddFilesForm

    def get(self, request):
        html = 'generic_form.html'
        form = self.form_class
        context = {'form': form}
        return render(request, html, context)

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name=data['name'],
                parent=data['parent']
            )
            return HttpResponseRedirect(reverse('homepage'))

