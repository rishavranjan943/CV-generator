from django.shortcuts import render
from .models import *
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def accept(request):
    if request.method == 'POST':
        user=request.user
        if user.is_authenticated:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            summary = request.POST.get('summary')
            degree = request.POST.get('degree')
            school = request.POST.get('school')
            college = request.POST.get('college')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')
            profile=Profile(user=user,name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,college=college,experience=experience,skills=skills)
            profile.save()
        else:
            messages.error(request, 'Please login to continue')
    return render(request,'index.html')

def view(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'view.html', {'profile':profile})


def resume(request, id):
    profile = Profile.objects.get(user=request.user,pk=id)
    return render(request, 'resume.html', {'profile':profile})

def download(request, id):
    profile = Profile.objects.get(user=request.user, pk=id)
    template = loader.get_template('download.html')
    html=template.render({'profile':profile})
    options={
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdf=pdfkit.from_string(html, False, options, configuration=pdf_config)
    response=HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename='resume.pdf'
    return response