from projects.models import *

profile1 = Profile(years_employed=5)
profile1.save()

employee1 = Employee(name="Bob", profile=profile1)
employee1.save()