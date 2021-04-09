from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def home(request):
    return HttpResponse('BONJOUR PHINEHAS !')

def home(request):
    return render(request, 'website/index.html')

def contact(request):
    return render(request, 'website/contact.html')

def about(request):
    return render(request, 'website/about.html')

def login(request):
    return render(request, 'website/login.html')

def services(request):
    #service = ServiceModel.objects.all()
    return (request, 'website/services.html'
            #,{"data":service}
)

def produits(request):
    #produit = ProduitModel.objects.all()
    return render(request, 'website/produits.html'
                  #,{"data":produit}
                  )

def candidature(request):
    return render(request, 'website/candidature.html')

def postuler(request):
    return render(request, 'website/postuler.html')

def message(request):
    return render(request, 'website/message.html')


