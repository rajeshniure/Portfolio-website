from django.shortcuts import render
# from django.views.generic import TemplateView
from .models import Profile
# Create your views here.

# class HomePageView(TemplateView):
#     template_name = 'index.html'
    
    

def home(request):
    profile = Profile.objects.first()  # or use filter().last(), etc.
    
    context = {
        "name": profile.name,
        "role": profile.role,
        "description": profile.description,
        "cv_link": profile.cv.url,
        "instagram": profile.instagram,
        "linkedin": profile.linkedin,
        "github": profile.github,
        "avatar_url": profile.avatar.url
    }
    return render(request, 'index.html', context)