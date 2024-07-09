from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    carbohydrates = models.FloatField()
    cholesterol = models.FloatField()
    fat_saturated = models.FloatField()
    fat_total = models.FloatField()
    fiber = models.FloatField()
    potassium = models.FloatField()
    protein = models.FloatField()
    sodium = models.FloatField()
    sugar = models.FloatField()

    def __str__(self):
        return self.name
