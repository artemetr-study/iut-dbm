from django.db import models


class Crew(models.Model):
    name = models.CharField(max_length=512)

    class Meta:
        db_table = 'crews'


class Position(models.Model):
    name = models.CharField(max_length=512)

    class Meta:
        db_table = 'positions'


class Employee(models.Model):
    lastname = models.CharField(max_length=512)
    firstname = models.CharField(max_length=512)
    middlename = models.CharField(max_length=512)
    birthday = models.DateField(null=True)
    hiring_date = models.DateField(null=True)
    dismissal_date = models.DateField(null=True)
    salary = models.FloatField(null=True)

    position_id = models.IntegerField(null=True)
    # position = models.ForeignKey(Position, on_delete=models.CASCADE)
    crew_id = models.IntegerField(null=True)

    @property
    def name(self):
        return ' '.join([i for i in [self.lastname, self.firstname, self.middlename] if i])

    class Meta:
        db_table = 'employees'
