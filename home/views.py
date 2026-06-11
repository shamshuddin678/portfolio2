from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

# Home Page
def home(request):
    context = {
        'name': 'shamshu',
        'course': 'Django'
    }
    return render(request, 'home.html', context)

# About Page
def about(request):
    return render(request, 'about.html')

# Projects Page
def projects(request):
    return render(request, 'projects.html')

# Contact Page
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            desc=desc
        )

        messages.success(request, "Your message has been sent successfully!")

    return render(request, 'contact.html')