from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect

from .models import Movie, Review, Category

from .forms import MovieForm, ReviewForm

from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email ID already exists!')
            return redirect('register')

        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                            password=password)

            messages.success(request, 'registered successfully')

            user.save()

            return redirect('login')

    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')

            return redirect('finalapp:index')

        else:
            messages.info(request, 'invalid credentials')
            return redirect('finalapp:login')

    return render(request, 'login.html')


def index(request):
    movies = Movie.objects.all()
    reviews = Review.objects.all()
    genres = Category.objects.all()

    context = {
        'movies': movies,
        'reviews': reviews,
        'genres': genres,
    }

    return render(request, 'index.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.date_of_birth = request.POST.get('date_of_birth')
        request.user.save()
        return redirect('finalapp:index')
    return render(request, 'profile.html')


def add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('finalapp:index')
    else:
        form = MovieForm()
    return render(request, 'add.html', {'form': form})


def detail(request, movie_id):
    # movie = Movie.objects.get(pk=movie_id)
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('finalapp:detail', movie_id=movie_id)
    else:
        form = MovieForm(instance=movie)

    return render(request, 'detail.html', {'movie': movie, 'form': form})


def delete(request, movie_id):
    print("Delete view called with ID:", movie_id)
    # movie = get_object_or_404(Movie, pk=movie_id)
    #
    # if movie.added_by != request.user:
    #     raise Http404("You are not authorized to delete this movie.")

    if request.method == "POST":
        movie = Movie.objects.get(pk=movie_id)
        movie.delete()
        messages.success(request, "Movie deleted successfully")
        return redirect('finalapp:index')
    return render(request, 'delete.html')


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('finalapp:index')
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})


def category(request, genre):
    genres = get_object_or_404(Category, name=genre)

    # genres = Category.objects.get(name=genre)

    movies = Movie.objects.filter(category=genres)

    return render(request, 'category.html', {'genres': genres, 'movies': movies})


def search(request):
    q = request.GET.get('q', '')
    movies = []
    if q:
        movies = Movie.objects.filter(name__icontains=q)
    context = {'movies': movies, 'query': q}

    return render(request, 'search.html', context)


# def dashboard(request):
#     movies = Movie.objects.all()
#     reviews = Review.objects.all()
#     genres = Category.objects.all()
#
#     context = {
#         'movies': movies,
#         'reviews': reviews,
#         'genres': genres,
#     }
#     return render(request, 'admin.html', context)

def dashboard(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            auth.login(request, user)
            messages.success(request, 'Login successful')

            return redirect('/admin/')

        else:
            messages.info(request, 'Invalid credentials')
            return redirect('finalapp:dashboard')

    return render(request, 'admin.html')


@login_required
def add_category(request):
    if request.method == 'POST':
        # Logic to handle form submission and add a new category
        pass
    else:
        # Render the form to add a new category
        return render(request, 'adminaddcategory.html')


@login_required
@permission_required('app.add_movie', raise_exception=True)
def add_or_delete_movie(request):
    if request.method == 'POST':
        # Logic to handle form submission and add or delete a movie
        pass
    else:
        # Render the form to add or delete a movie
        return render(request, 'admindeletemovie.html')


@login_required
@permission_required('auth.view_user', raise_exception=True)
def view_users(request):
    # Logic to retrieve and display a list of users
    users = User.objects.all()
    return render(request, 'adminviewusers.html', {'users': users})


@login_required
@permission_required('auth.delete_user', raise_exception=True)
def delete_user(request, user_id):
    # Logic to delete a user
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('adminuserdeletion')
