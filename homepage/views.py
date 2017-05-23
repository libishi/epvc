from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from .models import Faqs, Logo, Centernewsmain, Centernews1, Centernews2, Centernews3, Contactus, Pvnewsletters, Pvddl, Rmp, Legislation, Guideline, Subscribe, Regionalcenters, Adr, Psur, Images
#from django.views import views
# Create your views here.

def cn(request):
    #template = loader.get_template('homepage.html')
    logo = Logo.objects.all()
    centernewsmain = Centernewsmain.objects.all()
    centernews1 = Centernews1.objects.all()
    centernews2 = Centernews2.objects.all()
    centernews3 = Centernews2.objects.all()
    context= {
        'centernewsmain':centernewsmain[0],
        'centernews1':centernews1[0],
        'centernews2':centernews2[0],
        'centernews3':centernews3[0],
        'logo':logo[0],
    }

    return render(request, "test/index.html", context)

#######################################################################
def rmp(request):
    logo = Logo.objects.all()
    rmp = Rmp.objects.all()
    context= {
        'rmp':rmp,
        'logo':logo,
    }
    return render(request, "test/rmp.html", context)

def departments(request):
    logo = Logo.objects.all()
    #template = loader.get_template('homepage.html')
    return render(request, "departments/departments.html", {})

def pv(request):
    logo = Logo.objects.all()
    images = Images.objects.all()
    context= {
        'logo':logo,
        'images':images,
    }
    return render(request, "test/pv.html", context)

def md(request):
    logo = Logo.objects.all()
    #template = loader.get_template('homepage.html')
    return render(request, "departments/md.html", {})

def bc(request):
    logo = Logo.objects.all()
    #template = loader.get_template('homepage.html')
    return render(request, "departments/bc.html", {})
#########################################################
def adr(request):
    logo = Logo.objects.all()
    #template = loader.get_template('homepage.html')
    return render(request, "adr/adr.html", {})

def contactus(request):
    logo = Logo.objects.all()
    contacts = Contactus.objects.all()
    context= {
        'contacts':contacts,
        'logo':logo,
    }
    return render(request, "test/contactus.html", context)

def faqs(request):
    logo = Logo.objects.all()
    faqs = Faqs.objects.all()
    context= {
        'faqs':faqs,
        'logo':logo,
    }
    return render(request, "test/faqs.html", context)

def mindec(request):
    logo = Logo.objects.all()
    #template = loader.get_template('homepage.html')
    return render(request, "mindec/mindec.html", {})

def unsubscribe(request):
    logo = Logo.objects.all()
    #template = loader.get_template('homepage.html')
    return render(request, "unsubscribe/unsubscribe.html", {})
###############################################
    
def complains(request):
    logo = Logo.objects.all()
    context= {
        'logo':logo,
    }
    return render(request, "test/complains.html", context)
    
##############################   PV   ###################################
def pvnewsletters(request,year):
    logo = Logo.objects.all()
    years = year
    nl = Pvnewsletters.objects.all()
    context= {
        'nl':nl,
        'years':years,
        'logo':logo,
    }
    return render(request, "test/pvnewsletters.html", context)

def pvddl(request):
    logo = Logo.objects.all()
    pvddl = Pvddl.objects.all()
    context= {
        'pvddl':pvddl,
        'logo':logo,
    }
    return render(request, "pv/pvddl.html", context)



###############    test   ################  test ##################

def index(request):
    logo = Logo.objects.all()
    all_centernews = Centernews.objects.all()
    context= {
        'all_centernews':all_centernews,
        'logo':logo,
    }
    return render(request, "test/index.html", context)



