from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from .forms import (CustomUserCreationForm, CreatGameForm)
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
import datetime
from .models import (CustomUser, Game, Transaction)
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import *
from rest_framework import generics
import pyrebase
import pytz
from django.utils.timezone import make_aware



def Signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm
    return render(request, 'signup.html', {'form':form})




def Login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("home")
		
	form = AuthenticationForm()
    
    

	return render(request,"login.html",{"form":form})


def Logout(request):
    logout(request)
    return redirect("home")

config = {
    "apiKey": "AIzaSyCgEyXK-YyH-OUonAjL3PLTlJOK06vl7NM",
    "authDomain": "assignment-4343b.firebaseapp.com",
    "databaseURL" : "https://assignment-4343b-default-rtdb.firebaseio.com/",
    "projectId": "assignment-4343b",
    "storageBucket": "assignment-4343b.appspot.com",
    "messagingSenderId": "504991185585",
    "appId": "1:504991185585:web:b322e120cd490b0c6e4090",
    "measurementId": "G-L8WW8Q5XT6",
   
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def Home(request):
    day = database.child('User').get()
    st = datetime.datetime.now()
    st.tzinfo
    obj = Game.objects.exclude(end_date__lt=st)
    return render(request, 'home.html',{'obj':obj, 'base':day})



def CreateGame(request):
    if request.method == 'POST':
        form = CreatGameForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            obj.active = True
            form.save()
            return redirect('home')
    else:
        form = CreatGameForm()
    
    return render(request, "creategame.html", {"form":form})


def Play(request, pk):
    obj = get_object_or_404(Game,pk=pk)
    print(obj.title)

    
    Transaction.objects.create(user = request.user, game = obj, start_date = datetime.datetime.now())
    return redirect("home")

class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url = "login"))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)



class UserView(LoginRequiredMixin,generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserViewDetail(LoginRequiredMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset =  CustomUser.objects.all()
    serializer_class = UserSerializer
    

class CategoryList(LoginRequiredMixin,generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(LoginRequiredMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




class GameList(LoginRequiredMixin,generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(LoginRequiredMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer



class TransactionList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer



