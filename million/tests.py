from django.test import TestCase
from tutorial.million.models import Table , Roles ,Departments,Users,Meal_Categories,Statuses,ServicePercentage,Meals,Checks
from django.contrib.auth.models import User
class MillionTestCase(TestCase):
    def setUp(self):
        Table.objects.create(name='Table #1')
        Roles.objects.create(name='Waiter')
        Departments.objects.create(name='kitchen')
        Users.objects.create(name='User #1')
        Meal_Categories.objects.create(name='Pervoe')
        Statuses.objects.create(name='in progress')
        ServicePercentage.objects.create(percentage=34)
        Meals.objects.create(name='plov',price=250,description='bxchsvdcb')
        Checks.objects.create(servicefee=33,totalsum=500)
        rls = roles = Roles.objects.get(name='Waiter')
    # __________________
 
    def test_validCreatedTable(self):
        tbl = Table.objects.get(name='Table #1')
        self.assertEqual(tbl.name,'Table #1')

    def test_validCreatedRoles(self):
        rls = Roles.objects.get(name='Waiter')
        self.assertEqual(rls.name,'Waiter')

    def test_validCreatedDepartments(self):
        dpr = Departments.objects.get(name='kitchen')
        self.assertEqual(dpr.name,'kitchen')

    def test_validCreatedUsers(self):
        usr = Users.objects.get(name='User #1')
        self.assertEqual(usr.name,'User #1')

    def test_validCreatedMeal_Categories(self):
        mc = Meal_Categories.objects.get(name='Pervoe')
        self.assertEqual(mc.name,'Pervoe')

    def test_validCreatedStatuses(self):
        sts = Statuses.objects.get(name='in progress')
        self.assertEqual(sts.name,'in progress')

    def test_validCreatedServicePercentage(self):
        sp= ServicePercentage.objects.get(percentage=34)
        self.assertEqual(sp.percentage,34)

    def test_validCreatedMeals(self):
        mls = Meals.objects.get(name='plov',price=250,description='bxchsvdcb')
        self.assertEqual(mls.name,'plov')
        self.assertEqual(mls.price,250)
        self.assertEqual(mls.description,'bxchsvdcb')

    def test_validCreatedChecks(self):
        cks = Checks.objects.get(servicefee=33,totalsum=500)
        self.assertEqual(cks.servicefee,33)
        self.assertEqual(cks.totalsum,500)




    def test_isemptyStringTable(self):
        tbl = Table.objects.get(name='Table #1')
        self.assertEqual(sgr.when, '')

    def test_isemptyStringRoles(self):
        rls = Roles.objects.get(name='Waiter')
        self.assertEqual(rls.place,'')

    def test_isemptyStringDepartments(self):
        dpr = Departments.objects.get(name='kitchen')
        self.assertEqual(dpr.car,'')

    def test_isemptyStringUsers(self):
        usr = Users.objects.get(name='User #1')
        self.assertEqual(usr.number,'')

    def test_isemptyStringMeal_Categories(self):
        mc = Meal_Categories.objects.get(name='Pervoe')
        self.assertEqual(mc.what,'')

    def test_isemptyStringStatuses(self):
        sts = Statuses.objects.get(name='in progress')
        self.assertEqual(sts.where,'')

    def test_isemptyStringServicePercentage(self):
        sp= ServicePercentage.objects.get(percentage=34)
        self.assertEqual(sp.number,'')

    def test_isemptyStringMeals(self):
        mls = Meals.objects.get(name='plov',price=250,description='bxchsvdcb')
        self.assertEqual(mls.new,'')
        self.assertEqual(mls.pr,'')
        self.assertEqual(mls.desc,'')

    def test_isemptyStringChecks(self):
        cks = Checks.objects.get(servicefee=33,totalsum=500)
        self.assertEqual(cks.service,'')
        self.assertEqual(cks.total,'')
    def test_createdTable(self):
        tbl = Table.objects.get(name='Table #1')
        self.assertEqual(tbl.name,'Table #1')
        self.assertNotEqual(tbl.number,12)

    def test_createdRoles(self):
        rls = Roles.objects.get(name='Waiter')
        self.assertEqual(rls.name,'Waiter')
        self.assertNotEqual(rls.people,'Abramovich')

    def test_createdDepartments(self):
        dpr = Departments.objects.get(name='kitchen')
        self.assertEqual(dpr.name,'kitchen')
        self.assertNotEqual(dpr.place, 'Moscow')

    def test_createdUsers(self):
        usr = Users.objects.get(name='User #1')
        self.assertEqual(usr.name,'User #1')
        self.assertNotEqual(usr.time,12)

    def test_createdMeal_Categories(self):
        mc = Meal_Categories.objects.get(name='Pervoe')
        self.assertEqual(mc.name,'Pervoe')
        self.assertNotEqual(mc.cook,'pure')


    def test_createdStatuses(self):
        sts = Statuses.objects.get(name='in progress')
        self.assertEqual(sts.name,'in progress')
        self.assertNotEqual(sts.anime,'Naruto')


    def test_createdServicePercentage(self):
        sp= ServicePercentage.objects.get(percentage=34)
        self.assertEqual(sp.percentage,34)
        self.assertNotEqual(sp.car,'bmw')


    def test_createdMeals(self):
        mls = Meals.objects.get(name='plov',price=250,description='bxchsvdcb')
        self.assertEqual(mls.name,'plov')
        self.assertEqual(mls.price,250)
        self.assertEqual(mls.description,'bxchsvdcb')
        self.assertEqual(mls.anime2,'Bleach')
        self.assertEqual(mls.sum,20)
        self.assertEqual(mls.concert,'Katy Perry')

    def test_createdChecks(self):
        cks = Checks.objects.get(servicefee=33,totalsum=500)
        self.assertEqual(cks.servicefee,33)
        self.assertEqual(cks.totalsum,500)
        self.assertEqual(cks.number,55)
        self.assertEqual(cks.role,'progress')




