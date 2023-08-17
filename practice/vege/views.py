
from django.shortcuts import render,redirect
from vege.models import Receipe_about
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
def solar(request):
    return render(request,"solarsystem.html")

def receipe(request,id):
    user=User.objects.get(id=id)
    first_name=user.first_name

    queryset=Receipe_about.objects.all()
    
    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))
    
    context={'receipes':queryset,
             'first_name':first_name,
             'id':id}
    return render(request,"receipe.html",context)
# Create your views here.
def update(request,id):
    querySet=Receipe_about.objects.get(id=id)

    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('name')
        receipe_discription=data.get('receipe_discription')
        receipe_image=request.FILES['receipe_image']

        querySet.receipe_name=receipe_name
        querySet.receipe_discription=receipe_discription

        if receipe_image:
          querySet.receipe_image=receipe_image

        querySet.save()
        return redirect('/receipe/')        # to return in the same page 
    context={'receipe':querySet}  
    return render(request,"update_receipe.html",context) 

def delete(request,id):
    querySet=Receipe_about.objects.get(id=id)
    querySet.delete()
   
    return redirect('/receipe/')

def register_page(request):
    if request.method=="POST":
       data=request.POST
       first_name=data.get('first_name','')
       last_name=data.get('last_name','')
       email=data.get('email')
       password=data.get('password')

       user=User.objects.filter(email=email)
       if user.exists():
           messages.info(request,"Username already taken")
           
           return redirect('/register_page/')
        
       user=User.objects.create(
          username=email,
          first_name=first_name,
          last_name=last_name,      
       ) 
       user.set_password(password)
       user.save()

       messages.success(request,"Successfully created")
       return redirect('/register_page/')
    return render(request,"register.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        #usern=User.objects.get(username=username)
        # if not usern.exists():
        #     messages.error(request,"Username doesnt exits")
        #     return redirect('/login_page/')
        
        if not user is None:     
             login(request,user)
             return redirect('/receipe/{}/'.format(user.id))
        
        if user is None:       
             messages.error(request," Invalid password ")


             return redirect('/')
        

    return render(request, "login.html")


def addreceipe(request):
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES['recipe_image']
        receipe_name=data.get('name')
        receipe_discription=data.get('recipe_description')
        Receipe_about.objects.create(receipe_name=receipe_name, receipe_discription=receipe_discription, receipe_image=receipe_image) #fiirst one is of model and second one is of html page Name id
        return redirect('/receipe/')        # to return in the same page 
    
    return render(request, "addreceipe.html")


def profile(request,id):
    profile=User.objects.get(id=id)
    first_name=profile.first_name
    last_name=profile.last_name
    username=profile.username  # IN profile.username "username" is from database
   
    context={'first_name':first_name,
             'last_name':last_name,
             'email':username,
             'id':id}
    return render(request,"profile.html",context)