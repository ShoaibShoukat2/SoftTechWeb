from django.shortcuts import render,redirect
from .models import UserProfile
import bcrypt
from django.contrib.auth.hashers import check_password,make_password

# Create your views here.




def index(request):
    return render(request,'index.html')


def signup(request):
    error_messages = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        image = request.FILES.get('image', None)
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Basic validation (you may want to add more checks)
        if not username:
            error_messages['username'] = "Username is required."
        if not phone:
            error_messages['phone'] = "Phone is required."
        if not address:
            error_messages['address'] = "Address is required."
        if not email:
            error_messages['email'] = "Email is required."
        if not password or password != confirm_password:
            error_messages['password'] = "Passwords do not match or password is missing."

        # Check if user with the provided email already exists
        if UserProfile.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error_messages': 'User Already exists'})

        if error_messages:
            return render(request, 'signup.html', {'error_messages': error_messages})

        # Hash the password using make_password
        hashed_password = make_password(password)

        # Save data to the database
        user_profile = UserProfile(username=username, phone=phone, address=address, email=email, image=image, password=hashed_password)
        user_profile.save()

        return redirect('/success')

    return render(request, 'signup.html', {'error_messages': error_messages})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Retrieve user with the provided username
        user_profile = UserProfile.objects.filter(username=username).first()

        if not user_profile:
            return render(request, 'login.html', {'error_messages': 'Invalid username or password'})

        # Check if the provided password is correct using check_password
        if check_password(password, user_profile.password):
            # Passwords match, log in the user and store username in session
            request.session['user_id'] = user_profile.id
            request.session['username'] = user_profile.username

            return redirect('/')  # Redirect to the dashboard or any other page upon successful login
        else:
            return render(request, 'login.html', {'error_messages': 'Invalid username or password'})

    return render(request, 'login.html')

def logout(request):
    # Clear the session data
    request.session.clear()

    # Redirect to the login page or any other page after logout
    return redirect('/login')

def success(request):
    return render(request,'success.html')


def Profile(request):
    # Check if the user is authenticated
    if 'user_id' in request.session:
        user_id = request.session['user_id']

        try:
            # Try to get the UserProfile for the authenticated user
            user_profile = UserProfile.objects.get(id=user_id)

            # If the request is a POST request, process the form data
            if request.method == 'POST':
                # Update individual fields
                user_profile.username = request.POST.get('username')
                user_profile.phone = request.POST.get('phone')
                user_profile.address = request.POST.get('address')
                user_profile.email = request.POST.get('email')
                
                # Check if an image file was uploaded
                if 'image' in request.FILES:
                    user_profile.image = request.FILES['image']

                user_profile.save()
                success_message = "Profile updated successfully."
                return render(request, 'Profile.html', {'user_profile': user_profile, 'success_message': success_message})

            else:
                # If the request is a GET request, display the profile with the form
                return render(request, 'Profile.html', {'user_profile': user_profile})

        except UserProfile.DoesNotExist:
            error_message = "User profile not found."
            return render(request, 'Profile.html', {'error_message': error_message})

    else:
        error_message = "Please login first."
        return render(request, 'Profile.html', {'error_message': error_message})
    


def LahoreFort(request):
    return render(request,'LahoreFort.html')


def Mohnjo(request):
    return render(request,'Mohnjo.html')


def Sheesh(request):
    return render(request,'Sheesh.html')