from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home.html')

def register_view(request):
    if request.method == "POST": #? Check if the form method is post or not 
        username = request.POST.get('username','').strip() #? 'username' is from html
        email = request.POST.get('email','').strip() #? .strip is used to remove extra spaces from start and end

        password = request.POST.get('password','').strip()
        confirm_password = request.POST.get('confirm_password','').strip()

        if not username or not email or not password:
            messages.error (request,"All feilds are required.")
            return redirect("register") 

        # if User.objects.filter(username = username).exists():
        #     messages.error(request,"Username Already Exists")
        #     return redirect("register")

        if User.objects.filter(email = email).exists(): #? User is library which we have imported and this line is checking whether this email is already save
            messages.error(request,"Email Already Exists")
            return redirect("register")

        if password != confirm_password:
            messages.error(request,"Password Don't Match.")
            return redirect("register")

        if len(password) < 8:
            messages.error(request,"Password must be greater than 8 characters")
            return redirect("register")
        
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        ) #? if everything is good the user get saved
        messages.success(request,"Registration successful. please log in")
        return redirect("home")
    
    return render(request,'register.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username","").strip()
        password = request.POST.get("password","")

        user = authenticate(
            request,
            username = username,
            password = password
            )

        if user is not None:
            login(request,user)
            return redirect("home")

        messages.error(request,"Invalid username or password")
    return render(request,"login.html")

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return redirect("home")