from django.db import models

# if i am not satisfied with default queryset , need to sorting or something?
# super().get_queryset() - default eg - Employee.objects.all()
class CustomManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset().order_by('eno')
        return qs      # queryset

    def get_emp_sal_range(self,minsal,maxsal):         # inside of write in views .ORM -esal_range(15000,2000)
        # here i will write bigget logic for filtration , every i will call to that it
        # re usability
        qs = super().get_queryset().filter(esal__range=(minsal,maxsal))
        return qs    # my own method

    def get_emps_sorted_by(self,param):         # inside of write in views .ORM -esal_range(15000,2000)
            # here i will write bigget logic for filtration , every i will call to that it
            # re usability
        qs = super().get_queryset().order_by(param)
        return qs    # my own method
        #based on esal , eno i will get the ordered records

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=254)
    objects = CustomManager()
    #if i am not declaring object , it will take default model manager
# based on our requiremt we can define ourWe  own methods in CustomManagerclass
