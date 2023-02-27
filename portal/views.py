from django.shortcuts import render, redirect
# from django.http import HttpResponse
from portal.models import Teachers, Sports, Medical
# from django.contrib.auth.hashers import make_password, check_password
from django.contrib import sessions
# Create your views here.
def index(request):
    return render(request, "index.html")

# def sports(request):
#     return render(request, "registration.html")


def create_session(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    request.session['department'] = request.POST['department'].capitalize()

def login(request):
    if request.method == 'POST':
        # name = request.POST['name']
        # enpass = make_password(request.POST['password'])
        # print(enpass)
        # checkpass = check_password(request.POST['password'], enpass)
        # print(checkpass)
        try:
            # Department = request.POST['department'].capitalize()
            # print(Department)
            user = Teachers.objects.get(Email=request.POST['email'], Department=request.POST['department'].capitalize(), Password=request.POST['password'])
            print(user)
            if user is not None:
                # auth.login(request, user)
                # print('this is login')
                create_session(request)
                # dep = request.POST['department'].capitalize()
                return dashboard(request)
                # register = Teachers(Name=name, Email=email, Password=password)
                # register.save()
        except:
            return render(request, 'login.html')
    else:
        return render(request, "login.html")

    # return render(request, 'dashboard.html')

def signup(request):
    # print("this is signup")
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department'].capitalize()
        email = request.POST['email']
        password = request.POST['password']
        # password = make_password(request.POST['password'])
        # print(password)
        register = Teachers(Name=name,Department=department ,Email=email,Password=password)
        register.save()
        return render(request, 'login.html')
    else:
        return render(request, "login.html")


def sports(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Rollno = request.POST['rollno']
        Course = request.POST['course']
        Gender = request.POST['inlineRadioOptions']
        Department = request.POST['department']
        Phone = request.POST['phone']
        Game = request.POST['game']
        Entry = "Open"

        register = Sports(Name=Name,Rollno=Rollno,Course=Course,Gender=Gender,Department=Department,Phonenumber=Phone,Game=Game, Entry=Entry)
        # print(register)
        register.save()
        return render(request, "registration.html")
    else:
        print("error")
        return render(request, "registration.html")

def dashboard(request):
    if request.session.get('email') and request.session.get('password'):
    # print(dep)
        if request.session.get('department') == 'Sports':
            students = Sports.objects.all()
            print('this is sports dashboard')
            return render(request, 'dashboard.html', {'students' : students})
        else:
            students = Medical.objects.all()
            print('this is medical dashboard')
            return render(request, 'medicaldashboard.html', {'students': students})
    else:
        return render(request, 'login.html')

def medical(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Rollno = request.POST['rollno']
        Course = request.POST['course']
        Phonenumber = request.POST['phone']
        Age = request.POST['age']
        Email = request.POST['email']
        MaritalStatus = request.POST['maritalstatus']
        Weight = request.POST['weight']
        Height = request.POST['height']
        Gender = request.POST['gender']
        PatientProblem = request.POST['problem']
        Address = request.POST['address']
        Country = request.POST['country']
        City = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']

        register = Medical(Name=Name, Rollno=Rollno, Course=Course, Phonenumber=Phonenumber, Age=Age, Email=Email, MaritalStatus=MaritalStatus, Weight=Weight, Height=Height, Gender=Gender, PatientProblem=PatientProblem, Address=Address, Country=Country, City=City, state=state, pincode=pincode)
        register.save()
        return render(request, 'medical.html')
    else:
        return render(request, 'medical.html')

def logout(request):
    delete_session(request)
    return render(request, 'login.html')

def update(request, id):
    if request.session.get('department') == 'Sports':
        user = Sports.objects.get(id=id)
        print(user)
        if user is not None:
            Entry = "Closed"
            user.Entry = Entry
            user.save()
            # students = Sports.objects.filter(id=id,Entry=Entry)
            students = Sports.objects.all()
            return render(request, 'dashboard.html', {'students': students})
        else:
            return dashboard(request)
        # else:
        #     user = Medical.objects.get(id=id)
        #     if user is not None:
        #         Entry = "Closed"
        #         user.Entry = Entry
        #         user.save()
        #         students = Medical.objects.filter(id=id,Entry=Entry)
        #         return render(request, 'medicaldashboard.html', {'students': students})

def aboutus(request):
    return render(request, 'about us.html')

def contactus(request):
    return render(request, 'contact us.html')

def delete_session(request):
    try:
        del request.session['email']
        del request.session['password']
    except KeyError:
        pass
    return print('Deleted')