from django.shortcuts import render, redirect
from .models import Register_User
from django.contrib.auth import authenticate, login
from app import models
from django.http import JsonResponse

def login_page(request):
    return render(request, 'login.html')

def teacher_Lpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')  # Redirect to home page after login
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'teacher_login.html', {'error_message': error_message})
    return render(request, 'teacher_login.html')

def administrator_Lpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')  # Redirect to home page after login
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'administrator_login.html', {'error_message': error_message})
    return render(request, 'administrator_login.html')

def home_page(request):
    return render(request, 'home.html')

def register_page(request):
    #vakhar banako user ko details database batw leko
    stdData = Register_User.objects.all()
    print(f'std data {stdData}')
    context = {'stdData': stdData}
    if request.method == "POST":
        # Assuming the form fields match the model fields
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        contact_no = request.POST.get('contact_no')
        course = request.POST.get('course')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        year = request.POST.get('year')
        print(f'{student_id} and name is {name}')
        # Creating a new instance of Registers
        Register_User.objects.create(
            student_id=student_id,
            name=name,
            address=address,
            gender=gender,
            contact_no=contact_no,
            course=course,
            date_of_birth=date_of_birth,
            email=email,
            year=year
        )
        # Redirect to register page after successful registration
    
        # return redirect('register_page', context)

    return render(request, 'register.html', context)

def displayStudent(request):
    # Fetch all registered students
    register_page = Register_User.objects.all()
    context = {
        'register_page': register_page
    }
    return render(request, 'register.html', context)

def delete_register(request, id):
    # Get the instance of Registers to be deleted
    queryset = Register_User.objects.get(id=id)
    queryset.delete()
    return redirect('register_page')  # Redirect to register page after deletion


def update_register(request, id):
    queryset = Register_User.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        student_id = data.get("student_id")
        name = data.get("name")
        address =data.get("address")
        gender = data.get("gender")
        contact_no =data.get("contact_no")
        course =data.get("course")
        date_of_birth =data.get("date_of_birth")
        email =data.get("email")
        year =data.get("year")

        queryset.student_id = student_id
        queryset.name = name
        queryset.address = address
        queryset.gender = gender
        queryset.contact_no = contact_no
        queryset.course = course
        queryset.date_of_birth = date_of_birth
        queryset.email = email
        queryset.year = year
        
        queryset.save()
        return redirect('/Register')

    context = {'register': queryset}

    return render(request, 'update.html', context)

def select_page(request):
    return render(request, 'selectclass.html')

def course_page(request):
    return render(request, 'course.html')

def choose_year_bba_page(request):
    return render(request, 'chooseyearbba.html')

def choose_year_bit_page(request):
    return render(request, 'chooseyearbit.html')

def year_1_bba_page(request):
    return render(request, 'year1bba.html')

def year_2_bba_page(request):
    return render(request, 'year2bba.html')

def year_3_bba_page(request):
    return render(request, 'year3bba.html')

def year_4_bba_page(request):
    return render(request, 'year4bba.html')

def year_1_bit_page(request):
    return render(request, 'year1bit.html')

def year_2_bit_page(request):
    return render(request, 'year2bit.html')

def year_3_bit_page(request):
    return render(request, 'year3bit.html')





def display_bba_students(request):
    bba_students = Register_User.objects.filter(course='BBA')
    context = {'students': bba_students, 'course_name': 'BBA'}
    return render(request, 'year1bba.html', context)

def display_bit_students(request):
    bit_students = Register_User.objects.filter(course='BIT')
    context = {'students': bit_students, 'course_name': 'BIT'}
    return render(request, 'year1bit.html', context)

def display_bba_students(request):
    bba_students = Register_User.objects.filter(course='BBA')
    context = {'students': bba_students}
    return render(request, 'year1bba.html', context)

def calculate_attendance(request):
    if request.method == 'POST':
        # Process form submission
        attendance_data = {}
        for key in request.POST:
            print(key)
            if key.endswith('_attendance'):
                student_id = key.split('_')[0]
                value = request.POST[key]
                if student_id not in attendance_data:
                    attendance_data[student_id] = {'P': 0, 'A': 0}
                attendance_data[student_id][value] += 1

        return JsonResponse(attendance_data)
    else:
        return redirect('display_bba_students')