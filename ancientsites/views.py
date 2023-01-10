from asyncio.proactor_events import constants
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from dashboard.models.country import Country
from dashboard.models.state import State
from dashboard.models.category import Category
from dashboard.models.sitedescription import Sitedescription
from dashboard.models.siteimage import Siteimage
from dashboard.models.sitevideo import Sitevideo
from dashboard.models.adminuser import Adminuser
from .models.login import Login
from django.views.decorators.csrf import csrf_exempt
import json 
from django.db.models import Q
from django.db.models import F, base
from django.core.paginator import Paginator
from ancientsites.forms.check_login import Form_Add_Login
from django.contrib import messages
from argon2 import PasswordHasher
import random
# Create your views here.

def index(request):
    info=Category.objects.all()
    info_site=Sitedescription.objects.all()
    images=""
    image=""
    list=[]
    list_image=[]
    for i in info_site:
        list=[]
        image=Siteimage.objects.filter(site_name_id=i.id)
        if image:
            image=image.exclude(is_banner_image=True)
            for j in image:
                list.append(j.id)
            print(list)
            image_choice=random.choice(list)
            list_image.append(image_choice)
            print(list_image)
            print(i.id,image_choice)
    images=Siteimage.objects.filter(id__in=list_image)
    return render(request,'ancientsites/index.html',{'categorys':info,'images':images})

def archeological_site(request,id):
    # get the banner image
    check_banner_images=Siteimage.objects.filter(site_name_id=id).filter(is_banner_image=True).order_by('-modified_date')[:1]
    print(check_banner_images.count())
    info=Sitedescription.objects.get(pk=id)
    #image=Siteimage.objects.filter(site_name_id=id).order_by('-modified_date')
    image=Siteimage.objects.filter(site_name_id=id).exclude(is_banner_image=True).order_by('create_date')
    info_category=Category.objects.all()
    video=Sitevideo.objects.filter(site_name_id=id).order_by('-modified_date')
    if check_banner_images.count()==1:
        banner_image=Siteimage.objects.filter(site_name_id=id).filter(is_banner_image=True).order_by('-modified_date')[0]
        return render(request,'ancientsites/archeological_site.html',{'info':info,'banner_image':banner_image,'images':image,'categorys':info_category,'videos':video})
    else:
        return render(request,'ancientsites/archeological_site.html',{'info':info,'images':image,'categorys':info_category,'videos':video})


@csrf_exempt
def get_map_data(request):
    if request.method=='POST':
        info=list(Sitedescription.objects.select_related('category_name','state_name').annotate(category_url=F('category_name__id'),name_state=F('state_name__state_name'),name_country=F('state_name__country_name__country_name')).values('id','site_name','site_latitude','site_longitude','category_url','name_state','name_country').order_by('-modified_date'))
        return JsonResponse({'status':1,'sites':info})
    else:
        return JsonResponse({'status':0})


def archeological_site_images(request,site_id,image_id):
    info_image_id=Siteimage.objects.filter(id=image_id)
    info_site_id=Siteimage.objects.filter(site_name_id=site_id).exclude(id=image_id)
    info_site_id=info_site_id.exclude(is_banner_image=True).order_by('create_date') 
    info=info_image_id.union(info_site_id,all=True)
    print(info)
    for i in info:
        print(i.id)
    count=info.count()
    site_name=Sitedescription.objects.filter(id=site_id)[0]
    paginator = Paginator(info, 1) # Show 1 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'ancientsites/archeological_site_images.html',{'images':info,'page_obj':page_obj,'count':count,'site_id':site_id,'site_name':site_name})

def archeological_site_search(request):
    info=Sitedescription.objects.all().order_by('site_name')
    country_count=Country.objects.all().order_by('country_name')
    category_count=Category.objects.all()
    paginator = Paginator(info, 10) # Show 5 contacts per page.
    first_page = paginator.page(1).object_list
    page_range = paginator.page_range
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'ancientsites/archeological_site_search.html',{'sites':info,'country_count':country_count,'category_count':category_count,'page_obj':page_obj,'page_range':page_range,'first_page':first_page})

def autocomplete_search(request):
    if 'term' in request.GET:
        gs=Sitedescription.objects.filter(site_name__istartswith=request.GET.get('term'))
        data=list()
        for site in gs:
            data.append(site.site_name)
        return JsonResponse(data,safe=False)

@csrf_exempt
def get_site_id(request):
    if request.method == 'POST':
        site_name = request.POST.get('site_name', None)
        print(site_name)
        site_id=list(Sitedescription.objects.values('id').filter(site_name=site_name))
        print(site_id)
        return JsonResponse({"results":site_id})

@csrf_exempt
def get_pagination(request):
    info=Sitedescription.objects.all().order_by('site_name')
    paginator = Paginator(info, 10)
    page_range = list(paginator.page_range)
    if request.method == 'POST':
        page_n = request.POST.get('page_n', None)
        print(page_n)
        results = list(paginator.page(page_n).object_list.values('id', 'site_name'))
        print(results)
        return JsonResponse({"results":results,'page_range':page_range})

@csrf_exempt
def get_pagination_all(request):
    info=Sitedescription.objects.all().order_by('site_name')
    paginator = Paginator(info, 10)
    page_range = list(paginator.page_range)
    if request.method == 'POST':
        page_n = request.POST.get('page_n', None)
        print(page_n)
        results = list(paginator.page(page_n).object_list.values('id', 'site_name'))
        print(results)
        return JsonResponse({"results":results,'page_range':page_range})
   

@csrf_exempt
def get_pagination_country(request):
    if request.method == 'POST':
        page_n = request.POST.get('page_n', None)
        country_id = request.POST.get('id', None)
        info =Sitedescription.objects.select_related('state_name').annotate(id_country=F('state_name__country_name_id')).values('id','site_name').filter(id_country=country_id).order_by('site_name')
        paginator = Paginator(info, 2)
        page_range = list(paginator.page_range)
        results = list(paginator.page(page_n).object_list.values('id', 'site_name'))
        print(results)
        return JsonResponse({"results":results,'page_range':page_range})
    
@csrf_exempt
def get_pagination_state(request):
    if request.method == 'POST':
        page_n = request.POST.get('page_n', None)
        country_id = request.POST.get('countryid', None)
        state_id = request.POST.get('stateid', None)
        info =Sitedescription.objects.filter(state_name=state_id).order_by('site_name')
        print(info)
        paginator = Paginator(info, 2)
        page_range = list(paginator.page_range)
        results = list(paginator.page(page_n).object_list.values('id', 'site_name'))
        print(results)
        return JsonResponse({"results":results,'page_range':page_range})

@csrf_exempt
def get_pagination_category(request):
    if request.method == 'POST':
        page_n = request.POST.get('page_n', None)
        country_id = request.POST.get('countryid', None)
        state_id = request.POST.get('stateid', None)
        category_id = request.POST.get('categoryid', None)
        info =Sitedescription.objects.filter(state_name=state_id,category_name=category_id).order_by('site_name')
        print(info)
        paginator = Paginator(info, 2)
        page_range = list(paginator.page_range)
        results = list(paginator.page(page_n).object_list.values('id', 'site_name'))
        print(results)
        return JsonResponse({"results":results,'page_range':page_range})
        

@csrf_exempt
def get_state_list(request):
    if request.method=="POST":
        id=request.POST.get('id')
        state=State.objects.values().filter(country_name_id=id)
        state_list=list(state)
        return JsonResponse({'state_list':state_list})

@csrf_exempt
def get_category_list(request):
    if request.method=="POST":
        id=request.POST.get('id')
        info=list(Sitedescription.objects.select_related('category_name').annotate(name_category=F('category_name__category_name'),id_category=F('category_name__id')).values('id_category','name_category').filter(state_name_id=id).distinct('category_name__category_name'))
        return JsonResponse({'category_list':info})

def login(request):
    if request.method=='POST':
        form=Form_Add_Login(request.POST)
        if form.is_valid():
            username=form.cleaned_data['login_name']
            password=form.cleaned_data['login_password']
            print(username)
            print(password)
            try:
                check=Login.objects.get(login_name=username)
                print(check)
                
                ph = PasswordHasher()
                if ph.verify(check.login_password, password):
                    
                    info=Sitedescription.objects.all().order_by('site_name')
                    country_count=Country.objects.all().order_by('country_name')
                    category_count=Category.objects.all()
                    paginator = Paginator(info, 10) 
                    first_page = paginator.page(1).object_list
                    page_range = paginator.page_range
                    print('page_range',page_range)
                    page_number = request.GET.get('page')
                    page_obj = paginator.get_page(page_number)
                    request.session['name']='Sanjay Jambhulkar'
                    name=request.session['name']
                    request.session.set_expiry(0)
                    print(name)
                    return render(request,'dashboard/dashboard.html',{'sites':info,'country_count':country_count,'category_count':category_count,'page_obj':page_obj,'page_range':page_range,'first_page':first_page,'name':name})
            except: 
                fm=Form_Add_Login()
                messages.add_message(request,messages.SUCCESS,'Something is wrong with username or password')
                return render(request,'ancientsites/login.html',{'form':fm})
    else:  
        fm=Form_Add_Login()
        return render(request,'ancientsites/login.html',{'form':fm})

def aboutus(request):
    return render(request,'ancientsites/aboutus.html')