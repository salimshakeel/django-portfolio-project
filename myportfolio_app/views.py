from django.shortcuts import render
from .models import Home ,About,Porfile,Skill,Portfolio,Category

# Create your views here.
def index(request):
    #HOME
    home=Home.objects.latest("updated")
      # About
    about=About.objects.latest("updated")
    profiles = Porfile.objects.filter(about=about)
    #skill
    categories=Category.objects.all()
    #portfolio
    portfolios= Portfolio.objects.all()
    
    
    
    context={ 
        "home":home,
        "about":about,
        "profile":profiles,
        'categories': categories,
        'portfolios':portfolios,
        
        
        
    }

  
    
    return render(request, 'index.html',context)