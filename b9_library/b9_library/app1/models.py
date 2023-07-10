from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default= True)
    is_active = models.BooleanField(default= True)

    class Meta():
        db_table = 'Book'

    def __str__(self):
        return self.name



