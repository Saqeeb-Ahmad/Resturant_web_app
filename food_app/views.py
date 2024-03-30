from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from .models import AboutItems
from .models import About_ourstory
from .models import ServicesItem
from .models import ServicesItem_desc
from .models import Feedback_from
from .forms import Createuserform
from django.contrib import messages
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login/')
def home_page(request):
    return render(request, 'food_app/home.html')
def about_page(request):
    items=AboutItems.objects.all()
    ourstory= About_ourstory.objects.all()
    context = {'items':items,
               'ourstory':ourstory
               }
    return render(request, 'food_app/about.html',context)
@login_required(login_url='/login/')
def services_page(request):
    all_items = ServicesItem.objects.all()
    description = ServicesItem_desc.objects.all()
    context = {
        'all_items':all_items,
        'description': description
         }
    return render(request, 'food_app/services..html',context)

@login_required(login_url='/login/')
def feedback_view(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        rating = request.POST.get('rating')
        
        Feedback_obj = Feedback_from(
            name=name,
            email=email,
            feedback=feedback,
            rating=rating,
        )
        Feedback_obj.save()
    return render(request, 'food_app/feedback.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        form = Createuserform()
        if request.method == 'POST':
            form = Createuserform(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account successfully created')
                return redirect('/login/')
        context = {'form':form }
        
        return render(request, 'food_app/register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method == 'POST':
            username = request.POST.get('Username')
            password = request.POST.get('Password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/')
            else:
                messages.info(request, 'Invalid username or password')
        return render(request, 'food_app/login.html')

@login_required(login_url='/login/')
def logout_page(request):
    logout(request)
    return redirect(reverse('food_app:landing'))


def landing_page(request):
    return render(request, 'food_app/landing.html')

