from django.urls import path
from million import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.conf.urls import url
urlpatterns=[
path('table',views.TableView.as_view()),
path('roles',views.RolesView.as_view()),
path('deparments',views.DepartmentsView.as_view()),
path('users',views.UsersView.as_view()),
path('meal_categories',views.Meal_CategoriesView.as_view()),
path('statuses',views.StatusesView.as_view()),
path('servicepercentage',views.ServicePercentageView.as_view()),
path('meals',views.MealsView.as_view()),
path('orders',views.OrdersView.as_view()),
path('checks',views.ChecksView.as_view()),
path('meals_to_order',views.Meals_to_orderView.as_view()),
path('get_user_token',views.GYT_View.as_view()),
path('change_password',views.CP_View.as_view()),
path('table/<int:pk>',views.Tabledetails.as_view()),
path('roles/<int:pk>',views.Rolesdetails.as_view()),
path('deparments/<int:pk>',views.Departmentsdetails.as_view()),
path('Users/<int:pk>',views.Usersdetails.as_view()),
path('Meal_Categories/<int:pk>',views.Meal_Categoriesdetails.as_view()),
path('Statuses/<int:pk>',views.Statusesdetails.as_view()),
path('ServicePercentage/<int:pk>',views.ServicePercentagedetails.as_view()),
path('Meals/<int:pk>',views.Mealsdetails.as_view()),
path('Orders/<int:pk>',views.Ordersdetails.as_view()),
path('Checks/<int:pk>',views.Checksdetails.as_view()),
path('Meals_to_Order/<int:pk>',views.Meals_to_orderdetails.as_view()),
path('get_user_token/<int:pk>',views.GYT_details.as_view()),
path('change_password/<int:pk>',views.CP_details.as_view()),
path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns=format_suffix_patterns(urlpatterns)
