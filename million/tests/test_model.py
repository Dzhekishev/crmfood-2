from django.test import TestCase
from million.models import *



class TableTests(TestCase):

    def create_table(self, name='1'):
        return Table.objects.create(name=name)

    def test_tables_creation(self):
        table = self.create_table()
        self.assertTrue(isinstance(table, Table))
        self.assertEqual(table.__str__(), table.name)

    def create_departments(self, name="Kitchen"):
        return Departments.objects.create(name=name)

    def test_departments_creation(self):
        departments = self.create_departments()
        self.assertTrue(isinstance(departments, Departments))
        self.assertEqual(departments.__str__(), departments.name)

    def create_meal_categories(self, name="salad"):
        department = self.create_departments()
        return Meal_Categories.objects.create(name=name, departmentid=department)

    def test_meal_categories_creation(self):
        meal_categories = self.create_meal_categories()
        self.assertTrue(isinstance(meal_categories, Meal_Categories))
        self.assertEqual(meal_categories.__str__(), meal_categories.name)

    def create_statuses(self, name='to do'):
        return Statuses.objects.create(name=name)

    def test_statuses_creation(self):
        statuses = self.create_statuses()
        self.assertTrue(isinstance(statuses, Statuses))
        self.assertEqual(statuses.__str__(), statuses.name)

    def create_service_percentage(self):
        statuses=self.create_statuses()
        return ServicePercentage.objects.create(percentage=statuses)

    def test_service_percentage_creation(self):
        service_percentage = self.create_service_percentage()
        self.assertTrue(isinstance(service_percentage, ServicePercentage))

    def create_meals(self, name="Manty", price=190, description='National food '):
        meals_categories = self.create_meal_categories()
        return Meals.objects.create(name=name, price=price, description=description, categoryid=meals_categories)

    def test_meals_creation(self):
        meals = self.create_meals()
        self.assertTrue(isinstance(meals, Meals))
        self.assertEqual(meals.__str__(), meals.name)

    def create_roles(self, name="waiter"):
        return Roles.objects.create(name=name)

    def test_roles_creation(self):
        roles = self.create_roles()
        self.assertTrue(isinstance(roles, Roles))
        self.assertEqual(roles.__str__(), roles.name)
