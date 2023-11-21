from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_chart


# Create your views here.
def aboutMe(request):
  return render(request, 'recipes/about_me.html')

def home(request):
  return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipes
  template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):                       
  model = Recipes                                     
  template_name = 'recipes/detail.html' 


def search(request):
  form = RecipeSearchForm(request.POST or None)
  recipes_df = None
  chart = None
  qs = None

  if request.method =='POST':
    input = request.POST.get('name')
    chart_type = request.POST.get('chart_type')
    
    qs = Recipes.objects.filter(name__contains=input)
    if not qs:
      qs = Recipes.objects.filter(ingredients__contains=input)
    if qs:
        print(qs.values())
        recipes_df = pd.DataFrame(qs.values())
        print(recipes_df.loc[:,'name'])
        print("Column Names:", recipes_df.columns)

        chart = get_chart(chart_type, recipes_df, labels = recipes_df['name'].values)
        recipes_df = recipes_df.to_html()
    

  context = {
             'form': form,
             'objects': qs,
             'chart': chart,
             }
  
  return render(request, 'recipes/search.html', context)


