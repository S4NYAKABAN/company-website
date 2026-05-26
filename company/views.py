from django.shortcuts import render, redirect
from .models import Service, Client

def home(request):
    services = Service.objects.all()
    return render(request, 'company/home.html', {'services': services})

def services(request):
    services = Service.objects.all()
    return render(request, 'company/services.html', {'services': services})

def clients(request):
    clients = Client.objects.all()
    return render(request, 'company/clients.html', {'clients': clients})

def contact(request):
    if request.method == 'POST':
        from .models import ContactMessage
        ContactMessage.objects.create(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            message=request.POST.get('message', ''),
        )
        return redirect('contact_success')
    return render(request, 'company/contact.html')

def contact_success(request):
    return render(request, 'company/contact_success.html')
