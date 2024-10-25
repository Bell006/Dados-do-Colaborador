from django.shortcuts import render, redirect
from .models import Colab
from django.contrib import messages
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')

        url = settings.URL

        if not email or not name:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return render(request, 'index.html') 
        
        if Colab.objects.filter(email=email).exists():
            return redirect(url)

        new_colab = Colab(email=email, name=name)
        new_colab.save()

        return redirect(url)
    
    return render(request, 'index.html')