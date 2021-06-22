from django.test import TestCase
from courses.serializator import CourseSerializer
from courses.models import Category, Course
from courses.views import CourseView, CourseDelete
from django.urls import resolve
from rest_framework.reverse import reverse

class TestViews(TestCase):
    def setUp(self):
        category = Category.objects.create(id=2, name='Test', imgpath=None)
        Course.objects.create(id=2, name='Test course',
                              description='this checks test',
                              category=category, logo=None)

    def test_course_view(self):
        response = self.client.get(reverse('courses_api'))
        self.assertEqual(response.status_code, 200)

    def test_course_view_data(self):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        response = self.client.get(reverse('courses_api'))
        self.assertEqual(response.data, serializer.data)

    def test_course_view_2(self):
        url = reverse('courses_api')
        self.assertEqual(resolve(url).func.view_class, CourseView)

    def test_course_delete(self):
        url = reverse('single_course', args=[1])
        self.assertEqual(resolve(url).func.view_class, CourseDelete)