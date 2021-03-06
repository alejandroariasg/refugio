from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.usuario.forms import RegistroForm

class RegistroUsuario(CreateView):
	print("registro usuarios....")
	model = User
	template_name = 'usuario/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:mascota_listar')
