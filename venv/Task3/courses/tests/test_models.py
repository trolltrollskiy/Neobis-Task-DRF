from django.test import TestCase
from courses.models import *

class CategoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Ton', imgpath=None)

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_image(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('imgpath').verbose_name
        self.assertEqual(field_label, 'imgpath')

class CourseTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Ton', imgpath=None)
        Course.objects.create(
            name='Neolabs', description='Neolabs club',
            category=category, logo=None
        )

    def test_name_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)


    def test_description_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_legth(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)

    def test_foreign_key_category(self):
        course = Course.objects.get(id=1)
        foreign_key = course._meta.get_field('category').verbose_name
        self.assertEqual(foreign_key, 'category')

    def test_logo(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('logo').verbose_name
        self.assertEqual(field_label, 'logo')


class BranchTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(id=2, name='Maths', imgpath=None)
        course = Course.objects.create(id=3, name='TestCase',
                                       category=category, logo=None)

        Branch.objects.create(latitude='lati', longtitude='longti',
                              address='test address', course=course)

    def test_latitude_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('latitude').verbose_name
        self.assertEqual(field_label, 'latitude')

    def test_latitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('latitude').max_length
        self.assertEqual(max_length, 300)

    def test_longtitude_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('longtitude').verbose_name
        self.assertEqual(field_label, 'longtitude')

    def test_longtitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('longtitude').max_length
        self.assertEqual(max_length, 300)

    def test_address_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_address_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('address').max_length
        self.assertEqual(max_length, 300)

    def test_foreign_key_branch(self):
        branch = Branch.objects.get(id=1)
        foreign_key = branch._meta.get_field('course').verbose_name
        self.assertEqual(foreign_key, 'course')


class ContactTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(id=2, name='Maths', imgpath=None)
        course = Course.objects.create(id=3, name='TestCase',
                                       category=category, logo=None)

        Contact.objects.create(choice=2, value='Test value', course=course)

    def test_choice(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('choice').verbose_name
        self.assertEqual(field_label, 'choice')

    def test_value_lable(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('value').verbose_name
        self.assertEqual(field_label, 'value')

    def test_value_max_length(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('value').max_length
        self.assertEqual(field_label, 300)

    def test_foreign_key_contact(self):
        contact = Contact.objects.get(id=1)
        foreign_key = contact._meta.get_field('course').verbose_name
        self.assertEqual(foreign_key, 'course')