from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
  
from django.contrib.auth import login, authenticate


from django.urls import reverse, reverse_lazy
from million.models import *
from rest_framework import generics
from rest_framework.response import *
from django.http import Http404
from rest_framework.views import APIView
from million.serializers import *

from rest_framework.permissions import IsAuthenticated

from .permission import IsOwnerProfileOrReadOnly

from million.serializers import UserSerializers
from rest_framework import permissions
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.contrib.auth.views import LoginView
from rest_framework.authtoken.views import ObtainAuthToken



class UserloginView(ObtainAuthToken): 
	def post(self,request,*args,**kwargs):
		password = request.data['password'] 
		try:
			user = CustomUser.objects.get(password=password) 
			print(password) 
			print(user.id) 
			token, 
			created = Token.objects.get_or_create(user=user)
			user.is_active = True 
			user.save() 
			return Response(data={'user_id':user.id, 'token':token.key },status=status.HTTP_200_OK) 
		except CustomUser.DoesNotExist: 
			return Response(data={'Error': 'User not found'},status=status.HTTP_404_NOT_FOUND)








class UsersView(generics.ListCreateAPIView):
	queryset=Users.objects.all()
	serializer_class=Users_Serializers
	permission_classes = [permissions.IsAuthenticated]


	def perform_create(self,serializer):
		user=self.request.user
		serializer.save(user=user)


class Usersdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Users.objects.all()
	serializer_class=Users_Serializers
#	permission_classes = [IsOwnerProfileOrReadOnly,IsAuthenticated]







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
	

class OrdersView(generics.ListCreateAPIView):
	queryset=Orders.objects.all()
	serializer_class=Orders_Serializers
	

class ChecksView(generics.ListCreateAPIView):
	queryset=Checks.objects.all()
	serializer_class=Checks_Serializers
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Meals_to_orderView(generics.ListCreateAPIView):
	queryset=Meals_to_order.objects.all()
	serializer_class=Meals_to_order_Serializers
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GYT_View(generics.ListCreateAPIView):
	queryset=Get_User_Token.objects.all()
	serializer_class=GYT_Serializers
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CP_View(generics.ListCreateAPIView):
	queryset=Change_Password.objects.all()
	serializers_class=CP_Serializers
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]






class Tabledetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Table.objects.all()
	serializer_class=Table_Serializers

class Rolesdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Roles.objects.all()
	serializer_class=Roles_Serializers

class Departmentsdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Departments.objects.all()
	serializer_class=Departments_Serializers


class Meal_Categoriesdetails(generics.RetrieveUpdateDestroyAPIView):
	serializer_class=MealCategories_Serializers


	def get_queryset(self):
		department = self.kwargs['departmentid']
		return MealCategories.objects.filter(departmentid=department)

class Statusesdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Statuses.objects.all()
	serializer_class=Statuses_Serializers

class ServicePercentagedetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=ServicePercentage.objects.all()
	serializer_class=ServicePercentage_Serializers

class Mealsdetails(generics.RetrieveUpdateDestroyAPIView):
	serializer_class=Meals_Serializers
	


	def get_queryset(self):
		category = self.kwargs['categoryid']
		return Meals.objects.filter(categoryid=category)

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



class ActiveOrders(generics.ListAPIView):
    serializer_class = Orders_Serializers

    def get_queryset(self):
        return Orders.objects.filter(isitopen=True)

class MealsCountView(generics.ListAPIView):
	serializer_class=MealsCountSerializer
	queryset=MealsCount.objects.all()
	