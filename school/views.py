
from django.shortcuts import render ,redirect ,get_object_or_404
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from django.contrib.auth.models import User ,Group, auth
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from .utils import *
import json

# Create your views here.
def school_login(request):
    
    if request.method=="POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
            
                return redirect('school:home')
            else:
                messages.error(request, "Your account is not active. Please activate your account.")
        else:
            messages.error(request, "Invalid Username or Password ")   
    
    title="login"
    
    context={
        
        'title':title
    }
    
    return render(request, 'auth/base.html', context)

@login_required(login_url='')
def admin_home(request):
    
    driver_group = Group.objects.get(name='driver')
    drivers = driver_group.user_set.all()
    
    student_group = Group.objects.get(name='students')
    students =student_group.user_set.all()
    
    matron_group = Group.objects.get(name='Matrons')
    matrons = matron_group.user_set.all()
    
    all_users = User.objects.all()
    buss = Bus.objects.all()
    
    
    title="Dashboard"
    
    context ={
        'title':title,
        'drivers':drivers,
        'buss':buss,
        "all_drivers":drivers.count(),
        'students':students,
        'all_student':students.count(),
        'matrons':matrons,
        'all_matrons':matrons.count(),
        "all_user":all_users.count()
        
    }
    
    return render(request , 'admin/home.html', context)



@login_required(login_url='')
def buss(request):
    
    context ={
        
        
    }
    
    return render(request , 'admin/buss.html', context)



@login_required(login_url='')
def route(request ):
    
    routes = Route.objects.all()
    
    context ={
        'routes':routes
        
    }
    
    return render(request , 'admin/route.html', context)



@login_required(login_url='')
def students(request):
    
    student_group = Group.objects.get(name='students')
    students =student_group.user_set.all()
    
    context ={
        "students":students,
        "all_students":students.count()
        
     }
    
    return render(request , 'admin/students.html', context)



@login_required(login_url='')
def buss(request):
    
    buss = Bus.objects.all()
    route = Route.objects.all()
    
   
    context ={
        
        'buss':buss,
        'route':route,
    }
    
    return render(request ,'admin/buss.html', context)


@login_required(login_url='')
def supervisor(request):
    
    matron_group = Group.objects.get(name='Matrons')
    matrons = matron_group.user_set.all()
    
    context ={
        
        "matrons":matrons,
        "all_matrons":matrons.count()
    }
    
    return render(request ,'admin/supervisor.html', context)


@login_required(login_url='')
def management(request):
    

    users = User.objects.all()
    
    context={
        'users':users
    }
    
    return render(request , 'admin/management.html', context)


@login_required(login_url='')
def register_users(request):
    
    if request.method == 'POST':
        try:
            email = request.POST.get('email').lower()
            first_name = request.POST.get('firstname').capitalize()
            last_name = request.POST.get('lastname').capitalize()
            password = last_name.upper()  # Capitalize last name for password
            username = email  # Username will be the email

            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Email alredy in Use , Change Email !'})
            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already exists'})

            # Create the user with first name, last name, email, and password
            user = User.objects.create_user(username=username, email=email, password=password,
                                             first_name=first_name, last_name=last_name)

            # Assign user to the specified group
            group_name = request.POST.get('group')  # Group name from the request
            group = Group.objects.get(name=group_name)
            user.groups.add(group)

            
            return JsonResponse({'message': 'User registered successfully.'})
        except Exception as e:
            return JsonResponse({'error': 'Failed to register user.', 'details': str(e)})
    else:
        return JsonResponse({'error': 'Invalid method request.'})



@login_required(login_url='')
def register_bus(request):
    
    if request.method == 'POST':
        try:
            number = request.POST.get('number').upper()
            driver_id = request.POST.get('driver')
            
            # Check if bus number already exists
            if Bus.objects.filter(number=number).exists():
                return JsonResponse({'error': 'Bus already registered. Check the number!'})

            # Check if the driver is already assigned to another bus
            driver = get_object_or_404(User, pk=driver_id)
            if Bus.objects.exclude(driver=None).filter(driver=driver).exists():
                return JsonResponse({'error': 'This driver is already assigned to another bus.'})
            
            # Create the bus with number and driver
            bus = Bus.objects.create(number=number, driver=driver)
            bus.save()
            
            first_name = driver.first_name
            last_name = driver.last_name
            
            sms_message = f'Dear {first_name} {last_name}, you have been assigned to drive the bus with number: {number}'
            send_sms(driver.driver.contact_number, sms_message)
            
            return JsonResponse({'message': 'Bus registered successfully.'})
        except Exception as e:
            return JsonResponse({'error': 'Failed to register bus.', 'details': str(e)})
    else:
        return JsonResponse({'error': 'Invalid method request.'})
    
    
@login_required(login_url='')
def delete_bus(request):
    data = json.loads(request.body)
    busId = data['busId']
    
    if request.method=='POST' or request.method=='DELETE':
        
        if Bus.objects.filter(id=busId).exists():
            bus = get_object_or_404(Bus, pk=busId)
            bus.delete()
            if bus:
                 return JsonResponse({'message': 'Bus Removed successfully.'})
            else:
               return JsonResponse({'error':' Failed to Detelete bus !'})
        else:
            return JsonResponse({'error': 'Bus does not exist , Refrresh page'})
    else:
        return JsonResponse({'error': 'Invalid request method !.'}, status=400)


    
@login_required(login_url='')
def profile(request, user_id):
    # Fetch the user profile
    user_profile = get_object_or_404(User, pk=user_id)
    
    # Assuming you need to retrieve or create a Driver instance associated with this user
    # Replace this with your actual logic to retrieve or create a Driver instance
    driver_instance, created = Driver.objects.get_or_create(user=user_profile)
    
    context = {
        'user_profile': user_profile,
        'driver_instance': driver_instance  # Pass the Driver instance to the template if needed
    }
    
    return render(request, 'admin/profile.html', context)



@login_required(login_url='')
def update_driver_profile(request ):
    
    if request.method == 'POST':
        # Get form data
        number = request.POST.get('lisence')
        title = request.POST.get('title')
        gender = request.POST.get('gender')
        contact_number = request.POST.get('phone')
        address = request.POST.get('address')
        location = request.POST.get('location')
        user_id = request.POST.get('user_id')

        driver_profile, created = Driver.objects.get_or_create(user=user_id)
        # Update the driver profile
        driver_profile.gender = gender
        driver_profile.title = title
        driver_profile.contact_number = contact_number
        driver_profile.address = address
        driver_profile.location = location

        # Save the profile
        driver_profile.save()

        return JsonResponse({'message': 'Profile updated successfully.'})
    


@login_required(login_url="")
def student_profile(request, student_id):
    
    user_profile = get_object_or_404(User, pk=student_id)

    context = {
        
        'user_profile': user_profile,
          
     }
    
    return render(request, 'admin/student_profile.html', context)


@login_required(login_url='')
def update_student_profile(request):
    if request.method == 'POST':
        # Get form data
        parent_name = request.POST.get('parent_name')
        gender = request.POST.get('gender')
        phone = request.POST.get('parent_phone_number')
        address = request.POST.get('address')
        location = request.POST.get('location')
        student_id = request.POST.get('student_id')

        # Get the user instance
        user_instance = get_object_or_404(User, pk=student_id)

        # Get or create student profile
        student_profile, created = Student.objects.get_or_create(user=user_instance)

        # Update student profile fields
        student_profile.parent_name = parent_name
        student_profile.parent_phone_number = phone
        student_profile.gender = gender
        student_profile.address = address
        student_profile.location = location

        # Save the student profile
        student_profile.save()

        return JsonResponse({'message': 'Profile updated successfully.'})
    
#  ============ PATRON PROFILE ===============#

@login_required(login_url="")
def patron_profile(request, patron_id):
    
    user_profile = get_object_or_404(User, pk=patron_id)

    context = {
        
        'user_profile': user_profile,
          
     }
    
    return render(request, 'admin/patron_profile.html', context)


@login_required(login_url='')
def update_patron_profile(request):
   if request.method == 'POST':
        # Get form data
        region = request.POST.get('region')
        phone_number = request.POST.get('phone_number')
        street = request.POST.get('street')
        address = request.POST.get('address')
        patron_id = request.POST.get('patron_id')
        
        
        user_instance = get_object_or_404(User, pk=patron_id)

        # Get or create patron profile
        patron_profile, created = Patron.objects.get_or_create(user=user_instance)

        # Update patron profile fields
        patron_profile.region = region
        patron_profile.phone_number = phone_number
        patron_profile.street = street
        patron_profile.address = address

        # Save the patron profile
        patron_profile.save()

        return JsonResponse({'message': 'Profile updated successfully.'})
 
@login_required(login_url="")
def delete_patron(request):
    data = json.loads(request.body)
    patronId = data['patronId']
    
    if request.method=='POST' or request.method=='DELETE':
        
        if User.objects.filter(id=patronId).exists():
            patron = get_object_or_404(User, pk=patronId)
            patron.delete()
            if patron:
                 return JsonResponse({'message': 'Patron Removed successfully.'})
            else:
               return JsonResponse({'error':' Failed to Delete Patron...!'})
        else:
            return JsonResponse({'error': 'Patron does not exist , Refrresh page'})
    else:
        return JsonResponse({'error': 'Invalid request method !.'}, status=400)
    
       

@login_required(login_url="")
def delete_student(request):
    data = json.loads(request.body)
    studentId = data['studentId']
    
    if request.method=='POST' or request.method=='DELETE':
        
        if User.objects.filter(id=studentId).exists():
            student = get_object_or_404(User, pk=studentId)
            student.delete()
            if student:
                 return JsonResponse({'message': 'Student successfully.'})
            else:
               return JsonResponse({'error':' Failed to Student Driver !'})
        else:
            return JsonResponse({'error': 'Student does not exist , Refrresh page'})
    else:
        return JsonResponse({'error': 'Invalid request method !.'}, status=400)
    
    

from django.db.models import Q
@login_required(login_url='')
def register_route(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name').upper()
            start = request.POST.get('start')
            end = request.POST.get('end')
            bus_id = request.POST.get('buss')
            
            # Check if route with the same name already exists
            if Route.objects.filter(name=name).exists():
                return JsonResponse({'error': 'Route already registered.'})
            
            # Check if the bus exists
            bus = get_object_or_404(Bus, pk=bus_id)
            
            # Check if the bus is already assigned to another route
            if Route.objects.filter(Q(bus=bus) | Q(starting_point=start) | Q(ending_point=end)).exists():
                return JsonResponse({'error': 'This bus is already assigned to another route.'})
            
            # Create the route
            route = Route.objects.create(name=name, starting_point=start, ending_point=end, bus=bus)
            
            
            first_name = bus.driver.first_name
            last_name = bus.driver.last_name
            
            recipient = bus.driver.driver.contact_number
            # Send SMS notification to the driver
            
            sms_message = f'Dear {first_name} {last_name}, you have been assigned to drive the bus with number: {bus.number} on route: {start} to {end}.'
            send_sms(recipient, sms_message)
            
        
            return JsonResponse({'message': 'Route registered successfully.'})
        except Exception as e:
            return JsonResponse({'error': 'Failed to register Route.', 'details': str(e)})
    else:
        return JsonResponse({'error': 'Invalid method request.'})
    
    

@login_required(login_url='')
def delete_route(request):
    data = json.loads(request.body)
    routeId = data['routeId']
    
    if request.method=='POST' or request.method=='DELETE':
        
        if Route.objects.filter(id=routeId).exists():
            route = get_object_or_404(Route, pk=routeId)
            route.delete()
            if route:
                 return JsonResponse({'message': 'Route Removed successfully.'})
            else:
               return JsonResponse({'error':' Failed to Detelete Route !'})
        else:
            return JsonResponse({'error': 'Route does not exist , Refrresh page'})
    else:
        return JsonResponse({'error': 'Invalid request method !.'}, status=400)




@login_required(login_url="")
def delete_driver(request):
    data = json.loads(request.body)
    driverId = data['driverId']
    
    if request.method=='POST' or request.method=='DELETE':
        
        if User.objects.filter(id=driverId).exists():
            driver = get_object_or_404(User, pk=driverId)
            driver.delete()
            if driver:
                 return JsonResponse({'message': 'Driver successfully.'})
            else:
               return JsonResponse({'error':' Failed to Detelete Driver !'})
        else:
            return JsonResponse({'error': 'Driver does not exist , Refrresh page'})
    else:
        return JsonResponse({'error': 'Invalid request method !.'}, status=400)



# FETCHES DRIVERS 
@login_required(login_url='')
def fetch_drivers(request):
    # Your logic to fetch regions
    driver_group = Group.objects.get(name='driver')
    drivers = driver_group.user_set.all()
    options = '<option value="" selected disabled>Select Driver</option>'  # Default option
    for driver in drivers:
        options += f'<option value="{driver.id}">{driver.username}</option>'
        
    return JsonResponse({'options': options})


# FETCHES BUSS 
def fetch_buss(request):
    # Your logic to fetch regions
    buss = Bus.objects.all()
    
    options = '<option value="" selected disabled>Select Bus</option>'  # Default option
    for bus in  buss:
        options += f'<option value="{bus.id}">{bus.number}</option>'
        
    return JsonResponse({'options': options})





# FETCHES GROUPS FOR USER 
@login_required(login_url='')
def fetch_groups(request):
    # Your logic to fetch regions
    groups = Group.objects.all()
    options = '<option value="" selected disabled>Select Group</option>'  # Default option
    for group in groups:
        options += f'<option value="{group}">{group}</option>'
    return JsonResponse({'options': options})










@login_required(login_url='')
def logout(request):
    auth.logout(request)
    return redirect('school:user_login')
 


