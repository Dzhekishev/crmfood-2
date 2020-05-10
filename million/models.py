from django.db import models
from django.conf import settings
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver










class Table(models.Model):
	name=models.CharField('name',max_length=20)
	def __str__(self):
		return self.name
	owner=models.ForeignKey('auth.User',related_name='owner', on_delete=models.CASCADE, default='')

class Roles(models.Model):
	name=models.CharField('name',max_length=20,default='')
	def __str__(self):
		return self.name
	owner2=models.ForeignKey('auth.User',related_name='owner2', on_delete=models.CASCADE, default='')


class Get_User_Token(models.Model):
	roleid=models.ForeignKey(Roles,related_name='Roles',on_delete=models.CASCADE) 
	token=models.CharField('token',max_length=20)           
	owner3=models.ForeignKey('auth.User',related_name='owner3', on_delete=models.CASCADE, default='')

class Departments(models.Model):
	name=models.CharField('name',max_length=20)	
	def __str__(self):
		return self.name
	owner4=models.ForeignKey('auth.User',related_name='owner4', on_delete=models.CASCADE, default='')
	


class Users(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',default='')
	surname=models.CharField('surname',max_length=20)
	login=models.CharField('login',max_length=20)
	password=models.CharField('password',max_length=20)
	email_confirmed = models.BooleanField(default=False)
	roleid=models.ForeignKey(Roles,on_delete=models.CASCADE)
	date=models.DateTimeField(auto_now_add=True)
	phone=models.PositiveIntegerField('phone')
	owner5=models.ForeignKey('auth.User',related_name='owner5', on_delete=models.CASCADE, default='')













class Meal_Categories(models.Model):
	name=models.CharField('name',max_length=20)
	departmentid=models.ForeignKey(Departments,on_delete=models.CASCADE)	
	def __str__(self):
		return self.name
	owner6=models.ForeignKey('auth.User',related_name='owner6', on_delete=models.CASCADE, default='')


class Statuses(models.Model):
	name=models.CharField('name',max_length=20,default='')
	owner7=models.ForeignKey('auth.User',related_name='owner7', on_delete=models.CASCADE, default='')

class ServicePercentage(models.Model):
	percentage=models.ForeignKey(Statuses,related_name='Statuses',on_delete=models.CASCADE)

class Meals(models.Model):
	name=models.CharField('name',max_length=20)
	categoryid=models.ForeignKey(Meal_Categories,on_delete=models.CASCADE)
	price=models.PositiveIntegerField('price')
	description=models.TextField('description')
	owner=models.ForeignKey('auth.User',related_name='owner1', on_delete=models.CASCADE)
	def __str__(self):
		return f'{self.name}-{self.price}-{self.description}'

class Orders(models.Model):
	tableid=models.ForeignKey(Table,on_delete=models.CASCADE)
	waiterid=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='orders',on_delete=models.CASCADE)
	isitopen=models.BooleanField('isitopen')
	date=models.DateTimeField(verbose_name=True)
	meals=models.ManyToManyField(Meals)



class Checks(models.Model):
	orderid=models.ForeignKey(Orders,on_delete=models.CASCADE)
	date=models.DateField('date',max_length=20)
	servicefee=models.PositiveIntegerField('servicefee')
	totalsum=models.PositiveIntegerField('totalsum')
	meals=models.ManyToManyField(Meals)

class Meals_to_order(models.Model):
	orderid=models.ForeignKey(Orders,on_delete=models.CASCADE)
	meals=models.ManyToManyField(Meals)



class Change_Password(models.Model):
	oldpassword=models.CharField('oldpassword',max_length=20)
	newpassword=models.CharField('newpassword',max_length=20)
