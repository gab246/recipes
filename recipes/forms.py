from django import forms

CHART__CHOICES = (         
   ('#1', 'Bar chart'),    
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )

class RecipeSearchForm(forms.Form): 
   name = forms.CharField(max_length = 80)
   chart_type = forms.ChoiceField(choices=CHART__CHOICES)