from django.urls import path
from million import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.conf.urls import url
urlpatterns=[
	path('table',views.TableView.as_view()),


	path('roles',views.RolesView.as_view()),


	path('deparments',views.DepartmentsView.as_view()),


	path('profiles',views.UsersView.as_view()),


	path('meal_categories',views.Meal_CategoriesView.as_view()),


	path('statuses',views.StatusesView.as_view()),	
	

	path('servicepercentage',views.ServicePercentageView.as_view()),
	

	path('meals',views.MealsView.as_view()),
	

	path('orders',views.OrdersView.as_view()),
	

	path('checks',views.ChecksView.as_view()),	


	path('mealscount',views.MealsCountView.as_view()),
	

	path('meals_to_order',views.Meals_to_orderView.as_view()),
	

	path('get_user_token',views.GYT_View.as_view()),
	

	path('change_password',views.CP_View.as_view()),
	

	path('table/<int:pk>',views.Tabledetails.as_view()),
	

	path('roles/<int:pk>',views.Rolesdetails.as_view()),
	

	path('departments/<int:pk>',views.Departmentsdetails.as_view()),
	

	path('all_profiles/<int:pk>',views.Usersdetails.as_view()),
	

	path('meal_categories/<int:pk>',views.Meal_Categoriesdetails.as_view()),
	

	path('statuses/<int:pk>',views.Statusesdetails.as_view()),
	

	path('servicepercentage/<int:pk>',views.ServicePercentagedetails.as_view()),
	

	path('meals/<int:pk>',views.Mealsdetails.as_view()),
	

	path('orders/<int:pk>',views.Ordersdetails.as_view()),
	

	path('checks/<int:pk>',views.Checksdetails.as_view()),
	

	path('meals_to_order/<int:pk>',views.Meals_to_orderdetails.as_view()),
	

	path('get_user_token/<int:pk>',views.GYT_details.as_view()),
	

	path('change_password/<int:pk>',views.CP_details.as_view()),
	

	path('activeorders/', views.ActiveOrders.as_view(), name='active_orders'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns=format_suffix_patterns(urlpatterns)
