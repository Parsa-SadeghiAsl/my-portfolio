from django.shortcuts import render, redirect
from .models import Home, About, Profile, Category, Portfolio, Contact
from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
    
        home = Home.objects.latest('updated')
        
        about = About.objects.latest('updated')
        profiles = Profile.objects.filter(about= about)

        
        categories = Category.objects.all()
        
        portfolios = Portfolio.objects.all()
        
        context = {
            'home': home, 
            'about': about, 
            'profiles': profiles, 
            'categories': categories, 
            'portfolios': portfolios,
            'form': ContactForm(),
        }
        
        
        return render(request,'index.html',context)

