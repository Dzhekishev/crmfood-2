from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
  
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from million.tokens import account_activation_token
from million.forms import SignUpForm
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode


from django.urls import reverse, reverse_lazy
from million.models import *
from million.serializers import *
from rest_framework import generics
from rest_framework.response import *
from django.http import Http404
from rest_framework.views import APIView
from million.serializers import *


from million.serializers import UserSerializers
from rest_framework import permissions
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.contrib.auth.views import LoginView




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')
'''from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
)
from .forms import UserLoginForm,UserRegisterForm

def login_view(request):
	next=request.GET.get('next')
	form=UserLoginForm(request.POST or None)
	if form.is_valid():
		username=forms.cleaned_data.get('username')
		password=forms.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		login(request,user)
		if next:
			return redirect(next)
		return redirect('/')

	
	context={
		'form':form,
	}	
	return render(request,'login.html',context)



def register_view(request):
	next=request.GET.get('next')
	form=UserRegisterForm(request.POST or None)
	if form.is_valid():
		user=form.save(commit=False)
		password=forms.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user=authenticate(username=user.username,password=password)
		login(request,new_user)
		if next:
			return redirect(next)
		return redirect('/')

	
	context={
		'form':form,
	}	
	return render(request,'signup.html',context)

def logout_view(request):
	logout(request)
	return redirect('/')

'''

class TableView(generics.ListCreateAPIView):
	queryset=Table.objects.all()
	serializer_class=Table_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RolesView(generics.ListCreateAPIView):
	queryset=Roles.objects.all()
	serializer_class=Roles_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DepartmentsView(generics.ListCreateAPIView):
	queryset=Departments.objects.all()
	serializer_class=Departments_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UsersView(generics.ListCreateAPIView):
	queryset=Users.objects.all()
	serializer_class=Users_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Meal_CategoriesView(generics.ListCreateAPIView):
	queryset=Meal_Categories.objects.all()
	serializer_class=MealCategories_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StatusesView(generics.ListCreateAPIView):
	queryset=Statuses.objects.all()
	serializer_class=Statuses_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ServicePercentageView(generics.ListCreateAPIView):
	queryset=ServicePercentage.objects.all()
	serializer_class=ServicePercentage_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MealsView(generics.ListCreateAPIView):
	queryset=Meals.objects.all()
	serializer_class=Meals_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrdersView(generics.ListCreateAPIView):
	queryset=Orders.objects.all()
	serializer_class=Orders_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ChecksView(generics.ListCreateAPIView):
	queryset=Checks.objects.all()
	serializer_class=Checks_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Meals_to_orderView(generics.ListCreateAPIView):
	queryset=Meals_to_order.objects.all()
	serializer_class=Meals_to_order_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GYT_View(generics.ListCreateAPIView):
	queryset=Get_User_Token.objects.all()
	serializer_class=GYT_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CP_View(generics.ListCreateAPIView):
	queryset=Change_Password.objects.all()
	serializers_class=CP_Serializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]






class Tabledetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Table.objects.all()
	serializer_class=Table_Serializers

class Rolesdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Roles.objects.all()
	serializer_class=Roles_Serializers

class Departmentsdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Departments.objects.all()
	serializer_class=Departments_Serializers

class Usersdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Users.objects.all()
	serializer_class=Users_Serializers

class Meal_Categoriesdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Meal_Categories.objects.all()
	serializer_class=MealCategories_Serializers

class Statusesdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Statuses.objects.all()
	serializer_class=Statuses_Serializers

class ServicePercentagedetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=ServicePercentage.objects.all()
	serializer_class=ServicePercentage_Serializers

class Mealsdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Meals.objects.all()
	serializer_class=Meals_Serializers

class Ordersdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Orders.objects.all()
	serializer_class=Orders_Serializers

class Checksdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Checks.objects.all()
	serializer_class=Checks_Serializers

class Meals_to_orderdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Meals_to_order.objects.all()
	serializer_class=Meals_to_order_Serializers

class GYT_details(generics.RetrieveUpdateDestroyAPIView):
	queryset=Get_User_Token.objects.all()
	serializer_class=GYT_Serializers

class CP_details(generics.RetrieveUpdateDestroyAPIView):
	queryset=Change_Password.objects.all()
	serializers_class=CP_Serializers

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializers

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializers

