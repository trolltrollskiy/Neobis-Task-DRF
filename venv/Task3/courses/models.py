from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    imgpath = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    logo = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=300)
    longtitude = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE)

    def __str__(self):
        return self.address


class Contact(models.Model):
    CHOICES = [
        ( 1 , 'phone'),
        ( 2 , 'facebook'),
        ( 3 , 'email')
    ]
    choice = models.IntegerField(choices=CHOICES, default=3)
    value = models.CharField(max_length=300)
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE)

    def __str__(self):
        return self.value
