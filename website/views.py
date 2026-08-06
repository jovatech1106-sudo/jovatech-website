from django.shortcuts import render
from .models import Contact
from .forms import StudentRegistrationForm

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            subject=request.POST["subject"],
            message=request.POST["message"]
        )
        return render(request, "contact.html", {
            "success": "Your message has been sent successfully!"
        })
    return render(request, "contact.html")

# Create your views here.
def student_registration(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(
                request,
                "student_registration.html",
                {
                    "form": StudentRegistrationForm(),
                    "success": "Registration submitted successfully!"
                }
            )
        else:
            print(form.errors)   # This will show the actual errors
    else:
        form = StudentRegistrationForm()
    return render(
        request,
        "student_registration.html",
        {"form": form}
    )

def services(request):
    return render(request, "services.html")

def courses(request):
    return render(request, 'courses.html')

def gallery(request):
    return render(request, 'gallery.html')