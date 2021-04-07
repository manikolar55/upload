
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import server_loogin,Foo,country_name,city_names
from .forms import edit_cityy

# Create your views here.
def signup(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                print('user created')
                return render(request,'login.html')
        else:
            messages.info(request,'password is not matching')
            return redirect('signup')
    else:
        return render(request,'signup.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'wrong information')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
        auth.logout(request)
        return redirect("/")
def server_reg(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if server_loogin.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('server_reg')
            elif server_loogin.objects.filter(email=email).exists():
                messages.info(request, 'email is already taken')
                return redirect('server_reg')
            else:
                user = server_loogin(first_name=first_name, last_name=last_name, username=username,
                                                email=email, password1=password1)
                user.save()
                print('user created')
                return render(request, 'index.html')
        else:
            messages.info(request, 'password is not matching')
            return redirect('server_reg')
    else:
        return render(request, 'server_registration.html')
def server_login(request):
        if request.method == 'POST':
            username=request.POST['username']
            password1=request.POST['password']
            if server_loogin.objects.filter(username=username).exists() & server_loogin.objects.filter(password1=password1).exists():
                return redirect('server_page')
            else:
                messages.info(request,'Wrong Information')
                return redirect('server_login')
        else:
            return render(request,'serverlogin.html')
def server_page(request):
        all_countries=country_name.objects.all()

        return render(request,'server_page.html',{'all_countries':all_countries})

def countries(request):
    if request.method == 'POST':
        value=request.POST['country_name']
        if city_names.objects.filter(countryname_id=value).exists():
            all_cities=city_names.objects.filter(countryname_id=value)
            return render(request,'server_page.html',{'country_id':value, 'all_cities': all_cities})
    else:
        return render(request,'server_page.html')

def enter_city(request):
    if request.method == 'POST':
        name=request.POST['name']
        country = request.POST['country']
        if city_names.objects.filter(cityname=name).exists():
            messages.info(request,'city name is already enter')
            return redirect('enter_city')
        else:
            user=city_names(cityname=name,countryname_id=country)
            user.save()
            return redirect('server_page')
    else:
        return render(request,'enter_city.html')
def city(request):
    return render(request,'enter_city.html')
def edit_city(request,id):
    edit_cit=city_names.objects.filter(id=id)
    return render(request,'edit_city.html',{'edit_cit':edit_cit})
def update_city(request,id):
    updatecity = city_names.objects.get(id=id)
    form=edit_cityy(instance=updatecity)
    if request.method == 'POST':

        form=edit_cityy(request.POST,instance=updatecity)
        if form.is_valid():
            form.save()
        return redirect('server_page')
    else:
        context={'form':form}
        return render(request,'edit_city.html',{'students':form})


def delete_city(request,id):
    delcity=city_names.objects.get(id=id)
    delcity.delete()
    return redirect('server_page')