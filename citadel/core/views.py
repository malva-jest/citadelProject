from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User 
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView, 
                                  DeleteView
)
from .models import SitePassword
# from django.contrib.auth.decorators import login_required


# I think we need to remove this context from index and just render the basic html
def index(request): 
    # user = get_object_or_404(User, username=self.kwargs.get('username')) 
    current_user = request.user
    # context = { 'sites': SitePassword.objects.all() }
    user_passwords = SitePassword.objects.filter(user=current_user)
    context = { 'sites': user_passwords } 
    return render(request, 'core/index.html', context)
    # return render(request, 'core/index.html', context)

class PasswordListView(ListView):
    model = SitePassword
    template_name = 'core/index.html' 
    context_object_name = 'sites'


class UserPasswordListView(ListView):
    model = SitePassword
    template_name = 'core/user_sitepassword.html' 
    context_object_name = 'sites'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) 
        return SitePassword.objects.filter(user=user)
    # <app>/<model>_<viewtype>.html


class PasswordDetailView(DetailView):
    model = SitePassword

class PasswordCreateView(LoginRequiredMixin, CreateView):
    model = SitePassword
    fields = ['name', 'password']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PasswordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SitePassword
    fields = ['name', 'password']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        sitepassword = self.get_object()
        if self.request.user == sitepassword.user:
            return True
        return False

# Parameters LRM and UPTMixin need to be to the left of DeleteView
class PasswordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = SitePassword
    success_url = '/'

    def test_func(self):
        sitepassword = self.get_object()
        if self.request.user == sitepassword.user:
            return True
        return False


def login(request):
    return render(request, 'core/login.html')
