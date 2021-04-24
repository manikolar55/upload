
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import server_loogin,Foo,country_name,city_names,server_products
from .forms import edit_cityy
from .forms import DocumentForm
from .models import user_signup
dataaa=0

def index(request):
    return render(request,'index.html')

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

 #User signup

def users_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if user_signup.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('users_signup')
            elif user_signup.objects.filter(email=email).exists():
                messages.info(request, 'email is already taken')
                return redirect('users_signup')
            else:
                user = user_signup(first_name=first_name, last_name=last_name, username=username, email=email, password1=password1)
                user.save()
                print('user created')
                return render(request, 'login.html')
        else:
            messages.info(request, 'password is not matching')
            return redirect('users_signup')
    else:
        return render(request, 'user_signup.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

            # user=auth.authenticate(username=username,password=password)
            # if user is not None:
            #     auth.login(request,user)
            #     return redirect('/')
            # else:
            #     messages.info(request,'wrong information')
            #     return redirect('login')
        if username[0] == 's':
            if server_loogin.objects.filter(username=username).exists() & server_loogin.objects.filter(
                    password1=password).exists():
                return redirect('server_page')
            else:
                messages.info(request, 'Wrong Information')
                return redirect('login')
        else:
            if user_signup.objects.filter(username=username).exists() & user_signup.objects.filter(
                    password1=password).exists():
                return redirect('/')
            else:
                messages.info(request, 'Wrong Information')
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
        global dataaa
        dataaa=value


        print(f'that is data {dataaa}')
        all_countries = country_name.objects.all()
        if city_names.objects.filter(countryname_id=value).exists():
            all_cities=city_names.objects.filter(countryname_id=value)
        # return render(request,'enter_city.html',{'values':value})
            return render(request,'server_page.html',{'all_cities':all_cities,'all_countries':all_countries})

        else:
            messages.info(request, 'Cities is not added')
            return redirect('server_page')


    else:
        return render(request,'server_page.html')

def enter_city(request):
    if request.method == 'POST':
        name=request.POST['name']
        country = request.POST['country']
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
        return redirect('countries')
    else:
        context={'form':form}
        return render(request,'edit_city.html',{'students':form})


def delete_city(request,id):
    delcity=city_names.objects.get(id=id)
    delcity.delete()
    return redirect('server_page')
def show_city(request):
    val=dataaa

    print(f'the val is  {val}')
    return render(request,'enter_city.html',{'values':val})
    # all_countries = country_name.objects.all()
    # if city_names.objects.filter(countryname_id=val).exists():
    #     all_cities = city_names.objects.filter(countryname_id=val)
    #     # return render(request,'enter_city.html',{'values':value})
    #     return render(request, 'show_city.html', {'all_cities': all_cities})
    # else:
    #     messages.info(request, 'Cities is not added')
    #     return redirect('server_page')



def add(request,id):
    if request.method == 'POST':
         city_names.objects.get(id=id)
         return render('enter_city.html',{'values':id})
    else:
        return redirect('enter_city')
def server_product(request):
    all=server_products.objects.all()

    return render(request,'server_product.html',{'all':all})
def add_product_server(request):
    return render(request,'add_product_server.html')


# def add_products(request):
#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = HotelForm()
#
#         return render(request, 'add_product_server.html', {'add_product': form})

# def add_products(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'add_product_server.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = HotelForm()
#     return render(request, 'index.html', {'form': form})
# def success(request):
#     return HttpResponse('successfully uploaded')
# def add_products(request):
#     if request.method == 'POST':
#         name=request.POST['name']
#         price=request.POST['price']
#         comment=request.POST['comment']
#         img=request.POST['img']
#
#         user=server_products(name=name,desc=comment,price=price,img=img)
#         user.save()
#         return redirect('server_product')
#     else:
#         return render(request,'add_product_server.html')
def add_products(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('server_product')
    else:
        form = DocumentForm()
    return render(request, 'add_product_server.html', {
        'form': form
    })
def server_delete(request,id):
    delcity = server_products.objects.get(id=id)
    delcity.delete()
    return redirect('server_product')
def server_update(request,id):
    updatecity = server_products.objects.get(id=id)
    form=DocumentForm(instance=updatecity)
    if request.method == 'POST':

        form=DocumentForm(data=request.POST,files=request.FILES,instance=updatecity)
        if form.is_valid():
            form.save()
        return redirect('server_product')
    else:
        context={'form':form}
        return render(request,'edit_products.html',{'students':form})