from django.db import models

# Create your models here.

class Expenses(models.Model):
    expense_name = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    expense_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expenses'


class Revenue(models.Model):
    id = models.IntegerField(primary_key=True)
    revenue = models.CharField(max_length=45)
    credit_date = models.DateField()
    revenue_type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'revenue'

