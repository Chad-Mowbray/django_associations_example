from django.db import models


class Profile(models.Model):
    years_employed = models.IntegerField()

    def __str__(self):
        return f"Profile, years_employed: {self.years_employed}"


class Employee(models.Model):
    name = models.CharField(max_length=20)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee, name: {self.name}"


class Project(models.Model):
    secret_name = models.CharField(max_length=255)
    employees = models.ManyToManyField(Employee, related_name="projects")

    def __str__(self):
        return f"Project, secret name: {self.secret_name}"