from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Add_vehicle
from .models import Category
from .forms import CategoryForm,VehicleForm
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    # box=Add_vehicle.object.filter(status=True).count()
    # context={'box': box}

    return render(request,'Dashbord.html')
def Cat(request):
    display = Category.objects.all()
    form = CategoryForm()
    page_num = request.GET.get("page")  # Total number of pages reqired
    paginator = Paginator(display, 2)  # (8,2)

    try:
        display = paginator.page(page_num)  # If there is no pags not found in the page_num
    except PageNotAnInteger:
        display = paginator.page(1)  # It shows the first page of only which is : 127.0.0.1:8000
    except EmptyPage:  # If the page is empty(there no products then this except block will execute)
        display = paginator.page(paginator.num_pages)


    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category')
    context = {'display':display,'form':form}
    return render(request,'category.html',context)

def add(request):
    displays=Add_vehicle.objects.all()
    page_num = request.GET.get("page")  # Total number of pages reqired
    paginator=Paginator(displays,2)  # (8,2)

    try:
        displays =paginator.page(page_num) # If there is no pags not found in the page_num
    except PageNotAnInteger:
        displays =paginator.page(1) # It shows the first page of only which is : 127.0.0.1:8000
    except EmptyPage: # If the page is empty(there no products then this except block will execute)
        displays =paginator.page(paginator.num_pages)

    context={'displays':displays}
    return render(request,'managevehicle.html',context)
def vehicleentry(request):
    displays=Add_vehicle.objects.all()
    form=VehicleForm()
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vehicleentry')
    context = {'form': form,'displays':displays}
    return render(request,'Vechicleentry.html', context )
@login_required(login_url='dashboard')
def Reports(request):
    return render(request,'Reports.html')
def Accountsettings(request):

    return render(request,'Accountsettings.html')
def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query:  # condition is True
            vehicle = Add_vehicle.objects.filter(vehicle_no__contains=query)
            return render(request, 'Search.html',{'vehicle':vehicle})
        else:
            print("....No Vehicles is there....")
            return render(request, 'Search.html', {})

    return render(request,'Search.html')



def activated(request,pk):
    category = Category.objects.get(id=pk)
    category.status = True
    category.save()
    return redirect('category')

def deactive(request,pk):
    category = Category.objects.get(id=pk)
    category.status = False
    category.save()
    return redirect('category')

def Leaved(request,pk):
    displays = Add_vehicle.objects.get(id=pk)
    displays.status = False
    displays.save()
    return redirect('managevehicle')

def Done(request,pk):
    displays = Add_vehicle.objects.get(id=pk)
    displays.status = True
    displays.save()
    return redirect('managevehicle')

def CategarySearch(request):
    if request.method == 'GET':
        query=request.GET.get('query')

        if query: # condition is True
            category=Category.objects.filter(parking_area_no__contains=query)
            return render(request,'catogary.html',{'catogary':category})
        else:
            print("....No Vehicles is there....")
            return render(request,'category.html')

def ManageSearch(request):
    if request.method == 'GET':
        query=request.GET.get('query')

        if query: # condition is True
            displays=Add_vehicle.objects.filter(vehicle_no__contains=query)
            return render(request,'managevehicle.html',{'displays':displays})
        else:
            print("....No Vehicles is there....")
            return render(request, 'managevehicle.html')
def delete(request, pk):
    display = Category.objects.get(id=pk)
    display.delete()
    return redirect(request,'category')
def update(request, pk):
    display = Category.objects.get(id=pk)
    form = VehicleForm(instance=display)

    if request.method == "POST":
        form =VehicleForm(request.POST, request.FILES, instance=display)
        if form.is_valid():
            form.save()

            return redirect('category')

    context = {'form': form}

    return render(request, 'category.html', context)
def register(request):
    if request.method=="POST":
        username= request.POST['username']#Username=Prasanna(is coming from register table input => name='username')
        email= request.POST['email'] #prasanna@gmail.com
        password1 = request.POST['password1']#snlp@123
        password2 = request.POST['password2']#snlp@123
        if password1 == password2: #snlp@123==#snlp@123(TRUE)
            if User.objects.filter(username=username).exists():#prasanna(Database)=prasanna
                print("User Name exist! Try another username ")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print("email is already taken try another one")
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password1)
                    user.save()
                    return redirect('login')
        else:
            print('password did not match')
            return redirect('register')
    else:
        return render(request,'Registrationform.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('Login Successfully')
            return redirect('dashboard')
        else:
            print('YouInvalidProvided  Credential ')
            return redirect('login')
    else:
        return render(request,'Login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        print('Logged out from websites')
        return redirect('login')
