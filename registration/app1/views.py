from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


# def HomePage(request):
#         # username = request.user.username
#         # email = request.user.email
#         # context={'username':username,'email':email}

         
         
#     return render(request,'home.html')
@login_required(login_url='login')
def HomePage(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Fetch the username and email of the logged-in user
        username = request.user.username
        email = request.user.email
        # Pass the username and email to the template context
        context = {'username': username, 'email': email}
    else:
        # If the user is not authenticated, set username and email to None
        context = {'username': None, 'email': None}
    # Render the home.html template with the context
    return render(request, 'home.html', context)


def SignupPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not same")
        else:
             my_user= User.objects.create_user(uname,email,pass1)
             my_user.save() 

             # return HttpResponse("User created successfully")
             return redirect('login')

       


    return render(request,'signup.html')    


def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")
   




    return render(request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')