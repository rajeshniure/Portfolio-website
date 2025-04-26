# from django.shortcuts import render
# from .models import Profile

# def home(request):
#     profile = Profile.objects.first()  # or use filter().last(), etc.
    
#     context = {
#         "name": profile.name,
#         "role": profile.role,
#         "description": profile.description,
#         "cv_link": profile.cv.url,
#         "instagram": profile.instagram,
#         "linkedin": profile.linkedin,
#         "github": profile.github,
#         "avatar_url": profile.avatar.url
#     }
#     return render(request, 'index.html', context)


from django.shortcuts import render
from .models import Profile, Skill,ContactInfo, ContactMessage, Project,Certification
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import redirect





def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    
    projects = Project.objects.all()
    
    contact_info = ContactInfo.objects.first()
    
    certifications = Certification.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            # Save the message to DB
            ContactMessage.objects.create(name=name, email=email, message=message)

            # Compose the email
            subject = f"New Contact Message from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            email_msg = EmailMessage(
                subject,
                body,
                to=['rajeshniure567@gmail.com'],  
            )
            email_msg.send()

            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')
    

    context = {
        "name": profile.name,
        "role": profile.role,
        "description": profile.description,
        "about_description": profile.aboutDescription,
        "cv_link": profile.cv.url,
        "avatar_url": profile.avatar.url,
        "about_image": profile.about_image.url,
        "instagram": profile.instagram,
        "linkedin": profile.linkedin,
        "github": profile.github,
        "skills": skills,
        "contact_info": contact_info,
        "projects": projects, 
        "certifications": certifications,
    }
    return render(request, 'index.html', context)











# def home(request):
#     contact_info = ContactInfo.objects.first()

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         if name and email and message:
#             # Save the message to DB
#             ContactMessage.objects.create(name=name, email=email, message=message)

#             # Compose the email
#             subject = f"New Contact Message from {name}"
#             body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

#             email_msg = EmailMessage(
#                 subject,
#                 body,
#                 to=['rajeshniure567@gmail.com'],  # Replace with your receiving email
#             )
#             email_msg.send()

#             messages.success(request, "Your message has been sent successfully!")
#             return redirect('home')

#     context = {
#         "contact_info": contact_info,
#     }
#     return render(request, 'index.html', context)
