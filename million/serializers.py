from rest_framework import serializers
from million.models import *#импорт звездочка импортируют все файлы
from django.contrib.auth.models import User
class Table_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Table
		fields=('id','name')
class Roles_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Roles
		fields=('id','name')
class Departments_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Departments
		fields=('id','name')
class Users_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Users
		fields=('id','name','surname','login','password','email','roleid','date','phone','owner')
class MealCategories_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Meal_Categories
		fields=('id','name','departmentid')
class Statuses_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Statuses
		fields=('id','name')
class ServicePercentage_Serializers(serializers.ModelSerializer):
	class Meta:
		model=ServicePercentage
		fields=('id','percentage')
class Meals_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Meals
		fields=('id','name','categoryid','price','description','owner')
class Orders_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Orders
		fields=('id','tableid','meals')
class Checks_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Checks
		fields=('id','orderid')
class Meals_to_order_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Meals_to_order
		fields=('oderid','meals')

class GYT_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Get_User_Token
		fields=('id','roleid','token')
class CP_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Change_Password
		fields=('id','oldpassword','newpassword')
class UserSerializers(serializers.ModelSerializer):
	Table = serializers.PrimaryKeyRelatedField(many=True, queryset=Table.objects.all())
	class Meta:
		model=User
		fields=('id','username','Table')
class User2Serializers(serializers.ModelSerializer):
	Roles = serializers.PrimaryKeyRelatedField(many=True, queryset=Roles.objects.all())
	class Meta:
		model=User
		fields=('id','username','Roles')
class User2Serializers(serializers.ModelSerializer):
	Departments = serializers.PrimaryKeyRelatedField(many=True, queryset=Departments.objects.all())
	class Meta:
		model=User
		fields=('id','username','Departments')
class User3Serializers(serializers.ModelSerializer):
	Users = serializers.PrimaryKeyRelatedField(many=True, queryset=Users.objects.all())
	class Meta:
		model=User
		fields=('id','username','Users')
class User4Serializers(serializers.ModelSerializer):
	MealCategories_Serializers = serializers.PrimaryKeyRelatedField(many=True, queryset=Meal_Categories.objects.all())
	class Meta:
		model=User
		fields=('id','username','Meal Categories')
class User5Serializers(serializers.ModelSerializer):
	Statuses = serializers.PrimaryKeyRelatedField(many=True, queryset=Statuses.objects.all())
	class Meta:
		model=User
		fields=('id','username','Statuses')

class User7Serializers(serializers.ModelSerializer):
	Meals = serializers.PrimaryKeyRelatedField(many=True, queryset=Meals.objects.all())
	class Meta:
		model=User
		fields=('id','username','Meals')
class User8Serializers(serializers.ModelSerializer):
	ServicePercentage = serializers.PrimaryKeyRelatedField(many=True, queryset=ServicePercentage.objects.all())
	class Meta:
		model=User
		fields=('id','username','percentage')
class User7Serializers(serializers.ModelSerializer):
	Orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Orders.objects.all())
	class Meta:
		model=User
		fields=('id','username','Orders')
class User8Serializers(serializers.ModelSerializer):
	Checks = serializers.PrimaryKeyRelatedField(many=True, queryset=Checks.objects.all())
	class Meta:
		model=User
		fields=('id','username','Checks')
class User9Serializers(serializers.ModelSerializer):
	Meals_to_order = serializers.PrimaryKeyRelatedField(many=True, queryset=Meals_to_order.objects.all())
	class Meta:
		model=User
		fields=('id','username','Meals_to_order')
class User10Serializers(serializers.ModelSerializer):
	Get_User_Token = serializers.PrimaryKeyRelatedField(many=True, queryset=Get_User_Token.objects.all())
	class Meta:
		model=User
		fields=('id','username','Get_User_Token')

class User11Serializers(serializers.ModelSerializer):
	Change_Password = serializers.PrimaryKeyRelatedField(many=True, queryset=Change_Password.objects.all())
	class Meta:
		model=User
		fields=('id','username','Change_Password')