from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.TextField()


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_number = models.CharField(max_length=32)
    apartment_number = models.CharField(max_length=32, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Phone(models.Model):
    number = models.CharField(max_length=64)
    number_type = models.CharField(max_length=64)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Email(models.Model):
    address = models.CharField(max_length=64)
    address_type = models.CharField(max_length=64)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=64)
    person = models.ManyToManyField(Person)


