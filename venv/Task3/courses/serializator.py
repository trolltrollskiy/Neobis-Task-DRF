from rest_framework import serializers
from .models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['choice', 'value']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['address', 'longtitude', 'latitude']

class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Course
        fields = ['name', 'description', 'category',
                  'logo', 'contacts', 'branches']

    def create(self, validated_data):
        contacts = validated_data.pop('contacts')
        branches = validated_data.pop('branches')
        course = Course.objects.create(**validated_data)

        for data_contact in contacts:
            Contact.objects.create(course=course, **data)

        for data_branch in branches:
            Branch.objects.create(course=course, **data)

        return course
