from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SuccessView(View):
    template_name = 'success.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

