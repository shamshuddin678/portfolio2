from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name ="home"),
    path('about/',views.about,name ="about"),
    path('projects/',views.projects,name ="projects"),
    path('contact/',views.contact,name ="contact")
]

# Here name="" explaination
''' 
Here name = index
why because the 
<a href='/about'>About</a>
like that About inside anchor tag  
if not given not works & not loads the error shows
'''

# Here about/ or /about/ explaination 
'''
-> Here use 'about/' or use 'about' not '/about'
Correct
path('about/', views.about)

Django checks:

about/  ==  about/

Match 

Wrong
path('/about/', views.about)

Now Django checks:

about/   ==   /about/

Not same 

So error.

'''