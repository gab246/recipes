from django.db import models
from django.shortcuts import reverse

class Recipes(models.Model):
  pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
  name = models.CharField(max_length = 80)
  description = models.TextField(default='')
  cooking_time = models.IntegerField()
  ingredients = models.TextField()

  def calculate_difficulty(self):
    ingredients = self.ingredients.split(', ')
    if self.cooking_time < 10 and len(ingredients) < 4:
        difficulty = 'Easy'
    elif self.cooking_time < 10 and len(ingredients) >= 4:
        difficulty = 'Medium'
    elif self.cooking_time >= 10 and len(ingredients) < 4:
        difficulty = 'Intermediate'
    elif self.cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = 'Hard'
    return difficulty


  def get_absolute_url(self):
    return reverse ('recipes:detail', kwargs={'pk': self.pk})

  def __str__(self):
    returnstring = f"name: {self.name}, description: {self.description}, cooking time: {self.cooking_time}, ingredients: {self.ingredients}"
    return str(returnstring)
