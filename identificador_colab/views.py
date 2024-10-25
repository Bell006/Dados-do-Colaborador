from django.shortcuts import render, redirect
from .models import Colab
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')

        if not email or not name:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return render(request, 'index.html') 
        
        if Colab.objects.filter(email=email).exists():
            return redirect('https://drive.google.com/file/d/1GnjnNrRUGHJ9UtEOQO-sUB69KemfUGl4/view?usp=sharing')

        new_colab = Colab(email=email, name=name)
        new_colab.save()

        return redirect('https://drive.google.com/file/d/1GnjnNrRUGHJ9UtEOQO-sUB69KemfUGl4/view?usp=sharing')
    
    return render(request, 'index.html')