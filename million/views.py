from django.shortcuts import render

from million.models import *
from million.serializers import *
from rest_framework import generics
from rest_framework.response import *
from django.http import Http404
from rest_framework.views import APIView
from million.serializers import *
from django.contrib.auth.models import User
from million.serializers import UserSerializers
from rest_framework import permissions

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
class ServicepercentageView(generics.ListCreateAPIView):
	queryset=Servicepercentage.objects.all()
	serializer_class=Servicepercentage_Serializers
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





class Tabledetails(generics.RetrieveUpdateDestroyAPIViewCreateAPIView):
	queryset=Table.objects.all()
	serializer_class=Table_Serializers

class Rolesdetails(generics.RetrieveUpdateDestroyAPIViewCreateAPIView):
	queryset=Roles.objects.all()
	serializer_class=Roles_Serializers


class Departmentsdetails(generics.RetrieveUpdateDestroyAPIViewCreateAPIView):
	queryset=Departments.objects.all()
	serializer_class=Departments_Serializers


class Usersdetails(generics.RetrieveUpdateDestroyAPIViewCreateAPIView):
	queryset=Users.objects.all()
	serializer_class=Users_Serializers

class Meal_Categoriesdetails(generics.RetrieveUpdateDestroyAPIViewCreateAPIView):
	queryset=Meal_Categories.objects.all()
	serializer_class=MealCategories_Serializers

class Statusesdetails(generics.RetrieveUpdateDestroyAPIViewCreateAPIView):
	queryset=Statuses.objects.all()
	serializer_class=Statuses_Serializers

class Mealsdetails(generics.RetrieveUpdateDestroyAPIViewCreateAPIView):
	queryset=Meals.objects.all()
	serializer_class=Meals_Serializers

class Ordersdetails(generics.RetrieveUpdateDestroyAPIViewCreateAPIView):
	queryset=Orders.objects.all()
	serializer_class=Orders_Serializers

class Checksdetails(generics.RetrieveUpdateDestroyAPIViewCreateAPIView):
	queryset=Checks.objects.all()
	serializer_class=Checks_Serializers

class Meals_to_orderdetails(generics.RetrieveUpdateDestroyAPIViewCreateAPIView):
	queryset=Meals_to_order.objects.all()
	serializer_class=Meals_to_order_Serializers


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers