from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model

from inventario.models import Inventory
from django import forms

# Create your views here.

User = get_user_model()

def index(request):
    return render(request, 'index.html')


class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()



class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('index')


register = RegisterView.as_view()

