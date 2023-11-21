from django.test import TestCase
from .models import Recipes
from .forms import RecipeSearchForm
from django.contrib.auth.models import User
from django.urls import reverse


class RecipesModelTest(TestCase):

  def setUpTestData():
    Recipes.objects.create(name='cookies', ingredients='sugar, butter, flour, chocolate chips, eggs', cooking_time=15)

  def test_recipes_name(self):
    recipe = Recipes.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_recipe_name_max_length(self):
    recipe = Recipes.objects.get(id=1)
    max_length = recipe._meta.get_field('name').max_length
    self.assertEqual(max_length, 80)

  def test_recipe_cooking_time(self):
    recipe = Recipes.objects.get(id=1)
    field_label = recipe._meta.get_field('cooking_time').verbose_name
    self.assertEqual(field_label, 'cooking time')

  def test_get_absolute_url(self):
    recipe = Recipes.objects.get(id=1)
    self.assertEqual(recipe.get_absolute_url(), '/list/1')
  
  def test_difficulty_calculation(self):
    recipe = Recipes.objects.get( id=1)
    self.assertEqual(recipe.calculate_difficulty(), 'Hard')

class RecipesFormTest(TestCase):
  
  def test_valid_search_length(self):
    data = {
      'name': 'cookies',
      'chart_type': '#1'
    }
    form = RecipeSearchForm(data=data)
    self.assertTrue(form.is_valid())
   
  def test_invalid_search(self):
    data = {
      'name': ''
    }
    form = RecipeSearchForm(data=data)
    self.assertFalse(form.is_valid())
    
  def test_valid_chart(self):
    data = {
      'name': 'cottage pie',
      'chart_type': '#2'
    }
    form = RecipeSearchForm(data=data)
    self.assertTrue(form.is_valid())

  
  def test_invalid_chart(self):
    data = {
      'chart_type': '#5'
    }
    form = RecipeSearchForm(data=data)
    self.assertFalse(form.is_valid())

class LoginTest(TestCase):

  def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='testuser')
    self.recipe = Recipes.objects.create(name='recipe test', cooking_time=4)

  def test_authenicated_user_detail_view(self):
    self.client.login(username='testuser', password='testuser')
    response = self.client.get(reverse('recipes:detail', args=[self.recipe.id]))
    self.assertEqual(response.status_code, 200)

  
  def test_authenicated_user_list_view(self):
    self.client.login(username='testuser', password='testuser')
    response = self.client.get(reverse('recipes:list'))
    self.assertEqual(response.status_code, 200)




  

  
  