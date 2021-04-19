from django.shortcuts import render, redirect
from .models import User, Challenge
import bcrypt
from django.contrib import messages
from django.db.models import Count

def index(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def create_user(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/users/register')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password=pw_hash,
            )
            request.session['user_id'] = user.id 
            return redirect('/main_page')
    return redirect('/')

def main_page(request):
    if 'user_id' not in request.session: 
        return redirect('/')
    context={
        'current_user' : User.objects.get(id=request.session['user_id']),
        'all_challenges': Challenge.objects.all(),
    }
    return render(request, "main_page.html", context)

def login(request):
    if request.method == "POST":
        user_with_email = User.objects.filter(email = request.POST['email']) 
        if user_with_email:
            user = user_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id 
                return redirect('/main_page')
        messages.error(request, "Email or password are not correct.")
    return redirect('/')

def user_profile(request, user_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    context={
        'current_user' : User.objects.get(id = request.session['user_id']),
        # 'all_challenges': Challenge.objects.all(),
    }
    return render(request, "user_profile.html", context)

def edit_profile(request, user_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    else: 
        context={
            'current_user' : User.objects.get(id=user_id),
        }
        return render(request, "edit_profile.html", context)  

def checked_box(request):
    return render (request, "checked_box.html")
    
def update_profile(request, user_id): 
    if request.method =="POST":
        errors = User.objects.edit_validator(request.POST, user_id)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/users/profile/{user_id}/edit')    
            # instead of redirect, I want to extract form data into dictionary, send through context via render
        else:
            current_user = User.objects.get(id=user_id)
            current_user.first_name=request.POST['first_name']
            current_user.last_name=request.POST['last_name']
            current_user.email=request.POST['email']
            current_user.age=request.POST['age']
            current_user.location=request.POST['location']
            current_user.goals=request.POST['goals']
            current_user.quote=request.POST['quote']
            current_user.save()
            messages.success(request, "You successfully updated your account.")    
        return redirect(f'/users/profile/{user_id}')


def challenges(request):
    context={
        'all_challenges': Challenge.objects.all(),
        'current_user' : User.objects.get(id = request.session['user_id']),
    }
    return render(request, "challenges.html", context)

def accept_challenge(request, challenge_id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        current_user = User.objects.get(id = request.session['user_id'])
        one_challenge = Challenge.objects.get(id = challenge_id)
        current_user.challenges_accepted.add(one_challenge)
    return redirect(f'/users/profile/{current_user.id}')

def remove_accepted_challenge(request, challenge_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    if request.method == "POST":
        current_user = User.objects.get(id=request.session['user_id'])
        remove_challenge = Challenge.objects.get(id=challenge_id)
        current_user.challenges_accepted.remove(remove_challenge)
    return redirect(f'/users/profile/{current_user.id}')

def remove_completed_challenge(request, challenge_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    if request.method == "POST":
        current_user = User.objects.get(id=request.session['user_id'])
        remove_challenge = Challenge.objects.get(id=challenge_id)
        current_user.challenges_completed.remove(remove_challenge)
    return redirect(f'/users/profile/{current_user.id}')

def challenge_complete(request, challenge_id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        current_user = User.objects.get(id = request.session['user_id'])
        one_challenge = Challenge.objects.get(id = challenge_id)
        current_user.challenges_completed.add(one_challenge)
        if one_challenge in current_user.challenges_completed.all():
            remove_challenge = Challenge.objects.get(id=challenge_id)
            current_user.challenges_accepted.remove(remove_challenge)
    return redirect(f'/users/profile/{current_user.id}')

def challenge_details(request, challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    count = challenge.starting_at
    data = []
    for idx in range (1, 31, 1):
        data.append(count)
        count+=challenge.daily_increase
    context={
        'current_user' : User.objects.get(id = request.session['user_id']),
        'one_challenge': Challenge.objects.get(id=challenge_id),
        'data': data,
    }
    return render(request, "challenge_details.html", context)

def challenge_search(request):
    challenge_search = request.POST['challenge_search']
    if len(challenge_search) == 0:
        return render(request, "blank.html")
    if len(Challenge.objects.filter(name__startswith = request.POST['challenge_search'])) == 0:
            return render(request, "no_results.html")
    else:
        context = {
            'results': Challenge.objects.filter(name__startswith = request.POST['challenge_search'])
        }
    return render(request, "search_results.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')