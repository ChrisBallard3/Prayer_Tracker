from .models import Prayer
from django.shortcuts import render, redirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class SignIn(LoginView):
    context_object_name = 'signin'
    template_name = 'base/signin.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class Register(FormView):
    form_class = UserCreationForm
    template_name = 'base/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(Register, self).get(*args, **kwargs)


class PrayerList(LoginRequiredMixin, ListView):
    model = Prayer
    context_object_name = 'home'
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = context['home'].filter(user=self.request.user)
        context['count'] = context['home'].filter(answered=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['home'] = context['home'].filter(
                prayer__icontains=search_input)

        context['search_input'] = search_input

        return context


class PrayerDetail(LoginRequiredMixin, DetailView):
    model = Prayer
    context_object_name = 'prayer'
    template_name = 'base/prayer.html'

class PriorityPrayer(LoginRequiredMixin, DetailView):
    model = Prayer
    context_object_name = 'priority'
    template_name = 'base/prayer.html'

class PrayerCreate(LoginRequiredMixin, CreateView):
    model = Prayer
    context_object_name = 'create'
    template_name = 'base/create.html'
    fields = ['prayer', 'description', 'priority']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PrayerCreate, self).form_valid(form)


class PrayerUpdate(LoginRequiredMixin, UpdateView):
    model = Prayer
    context_object_name = 'create'
    template_name = 'base/create.html'
    fields = ['prayer', 'description', 'answered', 'priority']
    success_url = reverse_lazy('home')


class PrayerDelete(LoginRequiredMixin, DeleteView):
    model = Prayer
    context_object_name = 'prayer'
    template_name = 'base/delete.html'
    success_url = reverse_lazy('home')
