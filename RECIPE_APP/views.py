from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.template import loader
import requests
from .models import *
from .forms import * 
# Create your views here.
count = 0
def home(request):
    return render(request,"home.html")

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def userchoice(request):
    searchedrecipe=request.GET.get("searchedrecipe")
    if searchedrecipe:
        users=USER.objects.filter(recipename__icontains=searchedrecipe)
    else:    
        users=USER.objects.all()
    return render(request,"userchoice.html",{"users":users})

def recipesearch(request):
    recipe=request.GET.get("recipesearch")  
    url=f"https://api.edamam.com/api/recipes/v2?type=public&q={recipe}&app_id=88155ebd&app_key=66d1002dadb301971777a810a5542f17&random=true"
    responses=requests.get(url)
    data=responses.json()
    data=data["hits"]
    # return render(request,"recipesearch.html",{"data1":data})
    template = loader.get_template('recipesearch.html')
    context = {
    'data1':data,  
    }
    return HttpResponse(template.render(context, request))  

def count1(request):
    global count
    count += 1
    return count

def recipe(request):
    if request.user.is_authenticated:
        count = count1(HttpRequest)
        if count <=10:
            recipe_=request.GET.get("uri")
            recipe_=recipe_.split("#")[1]
            url=f"https://api.edamam.com/api/recipes/v2/{recipe_}?type=public&app_id=88155ebd&app_key=66d1002dadb301971777a810a5542f17"
            responses=requests.get(url)
            data=responses.json()
            data2=data["recipe"]["ingredientLines"]
            template = loader.get_template('recipename.html')
            context = {
            'data1':data, 
            'data2':data2 
            }
            return HttpResponse(template.render(context, request))
        else:
            return render(request,"pricing.html")
    
    else:
        count = count1(HttpRequest)
        if count<=5:
            recipe_=request.GET.get("uri")
            recipe_=recipe_.split("#")[1]
            url=f"https://api.edamam.com/api/recipes/v2/{recipe_}?type=public&app_id=88155ebd&app_key=66d1002dadb301971777a810a5542f17"
            responses=requests.get(url)
            data=responses.json()
            data2=data["recipe"]["ingredientLines"]
            template = loader.get_template('recipename.html')
            context = {
            'data1':data, 
            'data2':data2 
            }
            return HttpResponse(template.render(context, request))
        else:
            data="You reached your search limit. Login for further recipe tips."
            return render(request,"home.html",{"data":data})

def recipe1(request):
    search=request.GET.get("button1")
    data=USER.objects.filter(recipename__icontains=search)
    template = loader.get_template('recipename1.html')
    context = {
    'data1':data,
    'data2':search  
    }
    return HttpResponse(template.render(context, request))

def userrecipe(request):
    recipe1=request.GET.get("button1")
    x = USER.objects.filter(recipename__icontains=recipe1)
    template = loader.get_template('userrecipename.html')
    context = {
    'data1':x,  
    }
    return HttpResponse(template.render(context, request))  

def about(request):
    return render(request,"about.html")


def addrecipe(request):
    return render(request,"addrecipe.html")

def meals(request):
 
    url=f"https://api.edamam.com/api/recipes/v2?type=public&q=breakfast&app_id=88155ebd&app_key=66d1002dadb301971777a810a5542f17&random=true"
    responses=requests.get(url)
    data=responses.json()
    data=data["hits"]


    url1=f"https://api.edamam.com/api/recipes/v2?type=public&q=Lunch&app_id=88155ebd&app_key=66d1002dadb301971777a810a5542f17&random=true"
    responses1=requests.get(url1)
    data1=responses1.json()
    data1=data1["hits"]


    url2=f"https://api.edamam.com/api/recipes/v2?type=public&q=Dinner&app_id=88155ebd&app_key=66d1002dadb301971777a810a5542f17&random=true"
    responses2=requests.get(url2)
    data2=responses2.json()
    data2=data2["hits"]


    url3=f"https://api.edamam.com/api/recipes/v2?type=public&q=Snack&app_id=88155ebd&app_key=66d1002dadb301971777a810a5542f17&random=true"
    responses3=requests.get(url3)
    data3=responses3.json()
    data3=data3["hits"]

    url4=f"https://api.edamam.com/api/recipes/v2?type=public&app_id=88155ebd&app_key=66d1002dadb301971777a810a5542f17&mealType=Teatime"
    responses4=requests.get(url4)
    data4=responses4.json()
    data4=data4["hits"]
    template = loader.get_template('meals.html')

    context = {
    'data':data,
    'data1':data1, 
    'data2':data2,
    'data3':data3,
    'data4':data4 
    }
    return HttpResponse(template.render(context, request)) 
    # return render(request,"meals.html")

def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            ar = addrec(request.POST,request.FILES)
            print(request.FILES)
            if ar.is_valid():
                un = ar.cleaned_data['username']
                rn = ar.cleaned_data['recipename']
                dl = ar.cleaned_data['dietlabel']
                c = ar.cleaned_data['cuisine']
                d = ar.cleaned_data['dish']
                i = ar.cleaned_data['ingredients']
                h = ar.cleaned_data['health']
                fi = ar.cleaned_data['image']
                reg = USER(username=un,recipename=rn,dietlabel=dl,cuisine=c,dish=d,ingredients=i,health=h,image=fi)
                reg.save()
        else:
            ar = addrec()
            return render(request,'addrecipe.html',{'form':ar})
        data="RECIPE ADDED SUCCESSFULLY."
        return render(request,'home.html',{'data1':data})
    else:
        return render(request,"404.html")

def payment(request):
    return render(request,"payment.html")