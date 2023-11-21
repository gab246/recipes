from io import BytesIO 
import base64
import matplotlib.pyplot as plt

def get_graph():
  buffer = BytesIO()
  plt.savefig(buffer, format='jpg')
  buffer.seek(0)
  image_png=buffer.getvalue()
  graph = base64.b64encode(image_png)
  graph = graph.decode('utf-8')
  buffer.close()
  return graph

def get_chart(chart_type, data, **kwargs):
   plt.switch_backend('AGG')
   fig=plt.figure(figsize=(6,3))


   if chart_type == '#1':
       #plot bar chart between date on x-axis and quantity on y-axis
       plt.bar(data['name'], data['cooking_time'])
       plt.xlabel("Name")
       plt.ylabel("Cooking time")

   elif chart_type == '#2':
       plt.pie(data['cooking_time'], labels = data['name'])

   elif chart_type == '#3':
       #plot line chart based on date on x-axis and price on y-axis
       plt.plot(data['name'], data['cooking_time'])#
       plt.xlabel("Name")
       plt.ylabel("Cooking time")
   else:
       print ('unknown chart type')

   #specify layout details
   plt.tight_layout()

  
   chart = get_graph() 
   return chart   