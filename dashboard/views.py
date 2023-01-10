from django import forms
from django.db.models.query import QuerySet


from django.forms.forms import Form
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.utils.html import json_script

from dashboard.forms.add_category import Form_Add_Category
from dashboard.forms.add_sitedescription import Form_Add_Sitedescription
from dashboard.forms.add_siteimage import Form_Add_Siteimage
from dashboard.forms.update_siteimage import Form_Update_Siteimage
from dashboard.forms.add_sitevideo import Form_Add_Sitevideo
from dashboard.forms.change_login import Form_Change_Login
from ancientsites.forms.check_login import Form_Add_Login
#following are model import
from .models.category import Category
from .models.country import Country
from .models.state import State
from .models.sitedescription import Sitedescription
from .models.siteimage import Siteimage
from .models.sitevideo import Sitevideo
from ancientsites.models.login import Login


#following import will test the query
from django.contrib.auth.models import User
#following are the aggregate import
from django.db.models import Count
#following import for the messages fremwork
from django.contrib import messages
#following import for the paginator
from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_exempt

from django.db.models import F

from json import dumps

from ancientsites.views import archeological_site,login

from argon2 import PasswordHasher

#Below is json response code
# 0 - operations fail
# 1 - Add
# 2 - Edit
# 3 - Delete

# Create your views here.


def site(request,id):
    if 'name' in request.session:
        return archeological_site(request,id)
    else:
        return login(request)

def info_category(request):
    if 'name' in request.session:
        info=Category.objects.all().order_by('-modified_date')
        count_category=info.count()
        fm=Form_Add_Category()
        name=request.session['name']
        return render(request,'dashboard/info_category.html',{'categorys':info,'form':fm,'count_category':count_category,'name':name})
    else:
        return login(request)

def add_category(request):
    if 'name' in request.session:
        fm=Form_Add_Category(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Data added successfully')
            return HttpResponseRedirect('/dashboard/info_category/')
    else:
        return login(request)

def update_category(request,id):    
    if 'name' in request.session:
        if request.method=='POST':
            pi=Category.objects.get(pk=id)
            fm=Form_Add_Category(request.POST,request.FILES,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.add_message(request,messages.SUCCESS,'Update category :'+pi.category_name)
                return  HttpResponseRedirect('/dashboard/info_category/')
        else:
            pi=Category.objects.get(pk=id)
            fm=Form_Add_Category(instance=pi)
            return render(request,'dashboard/update_category.html',{'form':fm})
    else:
        return login(request)  

def delete_category_info(request,id):
    if 'name' in request.session:
        info=Category.objects.get(pk=id)
        return render(request,'dashboard/delete_category.html',{'categorys':info})
    else:
        return login(request)

def delete_category(request,id):
    if 'name' in request.session:
        pi=Category.objects.get(pk=id)
        pi.delete()
        messages.add_message(request,messages.SUCCESS,'Delete category :'+pi.category_name)
        return HttpResponseRedirect('/dashboard/info_category/')
    else:
        return login(request)

def region(request):
    if 'name' in request.session:
        info_country=Country.objects.all().order_by('country_name')
        info_state=State.objects.all().order_by('country_name')
        return render(request,'dashboard/region.html',{'countrys':info_country,'states':info_state})
    else:
        return login(request)


def add_country(request):
    if 'name' in request.session:
        if request.method=="POST":
            country_id=request.POST.get('country_id')
            country_name=request.POST['country_name']
            create_date=request.POST['create_date']
            if(country_id==""):
                country=Country(country_name=country_name)
                country.save()
                info=list(Country.objects.values().order_by('-modified_date'))
                return JsonResponse({'status':1,'countrys':info})
            else:
                country=Country(id=country_id,country_name=country_name,create_date=create_date)
                country.save()
                info=list(Country.objects.values().order_by('-modified_date'))
            return JsonResponse({'status':2,'countrys':info})
        else:
            return JsonResponse({'status':0})
    else:
        return login(request)

def edit_country(request):
    if 'name' in request.session:
        if request.method=="POST":
            country_id=request.POST.get('country_id')
            country=Country.objects.get(pk=country_id)
            country_data={"id":country.id,"country_name":country.country_name,"create_date":country.create_date}
            return JsonResponse(country_data)
    else:
        return login(request)

def delete_country(request):
    if 'name' in request.session:
        if request.method=="POST":
            country_id=request.POST.get('country_id')
            pi=Country.objects.get(pk=country_id)
            pi.delete()
            return JsonResponse({'status':1})
        else:
            return JsonResponse({'status':0})
    else:
        return login(request)

def add_state(request):
    if 'name' in request.session:
        if request.method=="POST":
            state_id=request.POST.get('stateid')
            state_name=request.POST['state_name']
            create_date=request.POST['create_date']
            country_name_id=request.POST['country_name_select_value']
            if(state_id==""):
                state=State(state_name=state_name,country_name_id=country_name_id)
                state.save()
                info= list(State.objects.select_related('country_name').annotate(name=F('country_name__country_name')).values('id','state_name','create_date','modified_date','country_name_id','name').order_by('-modified_date')) 
                return JsonResponse({'status':1,'states':info})
            else:
                state=State(id=state_id,state_name=state_name,create_date=create_date,country_name_id=country_name_id)
                state.save()
                info=list(State.objects.select_related('country_name').annotate(name=F('country_name__country_name')).values('id','state_name','create_date','modified_date','country_name_id','name').order_by('-modified_date')) 
                return JsonResponse({'status':2,'states':info}) 
        else:
            return JsonResponse({'status':0})
    else:
        return login(request)

def delete_state(request):
    if 'name' in request.session:
        if request.method=="POST":
            stateid=request.POST.get('stateid')
            pi=State.objects.get(pk=stateid)
            pi.delete()
            return JsonResponse({'status':1})
        else:
            return JsonResponse({'status':0})
    else:
        return login(request)

def edit_state(request):
    if 'name' in request.session:
        if request.method=="POST":
            state_id=request.POST.get('state_id')
            info=State.objects.select_related('country_name').annotate(name=F('country_name__country_name')).values('id','state_name','create_date','modified_date','country_name_id','name').get(id=state_id)
            print(info)
            return JsonResponse({'states':info})
    else:
        return login(request)


def info_sitedescription(request):
    if 'name' in request.session:
        info=Sitedescription.objects.all().order_by('-modified_date')
        count_sitedescription=info.count()
        fm=Form_Add_Sitedescription()
        country_count=Country.objects.all().order_by('country_name')
        return render(request,'dashboard/info_sitedescription.html',{'sites':info,'form':fm,'count_sitedescription':count_sitedescription,'country_count':country_count})
    else:
        return login(request)


def add_sitedescription(request):
    if 'name' in request.session:
        fm=Form_Add_Sitedescription(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Data added successfully')
            return HttpResponseRedirect('/dashboard/info_sitedescription/')
    else:
        return login(request)


def update_sitedescription(request,id):
    if 'name' in request.session:
        if request.method=='POST':
            pi=Sitedescription.objects.get(pk=id)
            fm=Form_Add_Sitedescription(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.add_message(request,messages.SUCCESS,'Update site description :'+pi.site_name)
                pi=Sitedescription.objects.get(pk=id)
                print(pi)
                fm=Form_Add_Sitedescription(instance=pi)
                info_sitedescription_image=Siteimage.objects.filter(site_name_id=id).order_by('create_date')
                info_sitedescription_video=Sitevideo.objects.filter(site_name_id=id).order_by('create_date')
                return render(request,'dashboard/update_sitedescription.html',{'form':fm,'info_sitedescription_image':info_sitedescription_image,'info_sitedescription_video':info_sitedescription_video,'id':id})
                #return HttpResponseRedirect('/dashboard/info_sitedescription/')
        else:
            pi=Sitedescription.objects.get(pk=id)
            fm=Form_Add_Sitedescription(instance=pi)
            info_sitedescription_image=Siteimage.objects.filter(site_name_id=id).order_by('create_date')
            info_sitedescription_video=Sitevideo.objects.filter(site_name_id=id).order_by('create_date')
            country_count=Country.objects.all().order_by('country_name')
        return render(request,'dashboard/update_sitedescription.html',{'form':fm,'info_sitedescription_image':info_sitedescription_image,'info_sitedescription_video':info_sitedescription_video,'country_count':country_count,'id':id})
    else:
        return login(request)
  

def delete_sitedescription(request,id):
    if 'name' in request.session:
        pi=Sitedescription.objects.get(pk=id)
        pi.delete()
        messages.add_message(request,messages.SUCCESS,'Delete site description :'+pi.site_name)
        return HttpResponseRedirect('/dashboard/info_sitedescription/')
    else:
        return login(request)
    

def delete_sitedescription_info(request,id):
    if 'name' in request.session:
        info_sitedescription=Sitedescription.objects.get(pk=id)
        info_sitedescription_image=Siteimage.objects.filter(site_name_id=id).order_by('-modified_date')
        info_sitedescription_video=info=Sitevideo.objects.filter(site_name_id=id)
        return render(request,'dashboard/delete_sitedescription.html',{'info_sitedescription':info_sitedescription,'info_sitedescription_image':info_sitedescription_image,'info_sitedescription_video':info_sitedescription_video})
    else:
        return login(request)

def info_siteimage(request):
    if 'name' in request.session:
        info=Siteimage.objects.all().order_by('site_name','-modified_date')
        country_count=Country.objects.all().order_by('country_name')
        count_siteimage=info.count()
        totalcount=Sitedescription.objects.annotate(counts=Count('siteimage'))
        fm=Form_Add_Siteimage()
        return render(request,'dashboard/info_siteimage.html',{'images':info,'form':fm,'count':count_siteimage,'totals':totalcount,'country_count':country_count})
    else:
        return login(request)

def info_siteimage_individual(request,id):
    if 'name' in request.session:
        info=Siteimage.objects.filter(site_name_id=id).order_by('-modified_date')
        count=info.count()
        paginator = Paginator(info, 1) # Show 1 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'dashboard/info_siteimage_individual.html',{'images':info,'page_obj':page_obj,'count':count})
    else:
        return login(request)

def add_siteimage(request):
    if 'name' in request.session:
        fm=Form_Add_Siteimage(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Data added successfully')
            return HttpResponseRedirect('/dashboard/info_siteimage/')
    else:
        return login(request)

def update_siteimage(request,id):
    if 'name' in request.session:
        if request.method=='POST':
            pi=Siteimage.objects.get(pk=id)
            fm=Form_Update_Siteimage(request.POST,request.FILES,instance=pi)
            if fm.is_valid():
                is_banner_image=fm.cleaned_data['is_banner_image']
                print(is_banner_image)
                if bool(is_banner_image):
                    print('hello')
                    site_name_id=Siteimage.objects.filter(site_name_id=pi.site_name_id).exclude(id=id)
                    print(site_name_id)
                    for i in site_name_id:
                        print(i.id)
                        i.is_banner_image='False'
                        i.save()
                    fm.save()
                    messages.add_message(request,messages.SUCCESS,'Update site image :'+pi.siteimage_name)
                    get_siteid=Siteimage.objects.get(pk=id)
                    siteid=Sitedescription.objects.get(pk=get_siteid.site_name.id)
                    fm=Form_Add_Sitedescription(instance=siteid)
                    info_sitedescription_image=Siteimage.objects.filter(site_name_id=siteid).order_by('create_date')
                    info_sitedescription_video=Sitevideo.objects.filter(site_name_id=siteid).order_by('create_date')
                    return render(request,'dashboard/update_sitedescription.html',{'form':fm,'info_sitedescription_image':info_sitedescription_image,'info_sitedescription_video':info_sitedescription_video})
                    #return HttpResponseRedirect('/dashboard/info_siteimage/')
                else:
                    fm.save()
                    messages.add_message(request,messages.SUCCESS,'Update site image :'+pi.siteimage_name)
                    get_siteid=Siteimage.objects.get(pk=id)
                    siteid=Sitedescription.objects.get(pk=get_siteid.site_name.id)
                    fm=Form_Add_Sitedescription(instance=siteid)
                    info_sitedescription_image=Siteimage.objects.filter(site_name_id=siteid).order_by('create_date')
                    info_sitedescription_video=Sitevideo.objects.filter(site_name_id=siteid).order_by('create_date')
                    return render(request,'dashboard/update_sitedescription.html',{'form':fm,'info_sitedescription_image':info_sitedescription_image,'info_sitedescription_video':info_sitedescription_video})
                    #return HttpResponseRedirect('/dashboard/info_siteimage/')
                    
        else:
            pi=Siteimage.objects.get(pk=id)
            fm=Form_Update_Siteimage(instance=pi)
            country_count=Country.objects.all().order_by('country_name')
            return render(request,'dashboard/update_siteimage.html',{'form':fm,'pi':pi,'country_count':country_count})
    else:
        return login(request)


@csrf_exempt
def delete_siteimage(request):
    if 'name' in request.session:
        if request.method=="POST":
            image_id=request.POST.get('image_id')
            print(image_id)
            pi=Siteimage.objects.get(pk=image_id)
            pi.delete()
            return JsonResponse({'status':1})
        else:
            return JsonResponse({'status':0})
    else:
        return login(request)

def info_sitevideo(request):
    if 'name' in request.session:
        info=Sitevideo.objects.all().order_by('site_name','-modified_date')
        count_sitevideo=info.count()
        country_count=Country.objects.all().order_by('country_name')
        totalcount=Sitedescription.objects.annotate(counts=Count('sitevideo'))
        fm=Form_Add_Sitevideo()
        return render(request,'dashboard/info_sitevideo.html',{'videos':info,'form':fm,'count':count_sitevideo,'totals':totalcount,'country_count':country_count})
    else:
        return login(request)


def info_sitevideo_individual(request,id):
    if 'name' in request.session:
        info=Sitevideo.objects.filter(site_name_id=id)
        return render(request,'dashboard/info_sitevideo_individual.html',{'videos':info})
    else:
        return login(request)

def add_sitevideo(request):
    if 'name' in request.session:
        fm=Form_Add_Sitevideo(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Data added successfully')
            return HttpResponseRedirect('/dashboard/info_sitevideo/')
    else:
        return login(request)

def update_sitevideo(request,id):
    if 'name' in request.session:
        if request.method=='POST':
            pi=Sitevideo.objects.get(pk=id)
            fm=Form_Add_Sitevideo(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.add_message(request,messages.SUCCESS,'Update site video :'+pi.sitevideo_name)
                get_siteid=Sitevideo.objects.get(pk=id)
                siteid=Sitedescription.objects.get(pk=get_siteid.site_name.id)
                fm=Form_Add_Sitedescription(instance=siteid)
                info_sitedescription_image=Siteimage.objects.filter(site_name_id=siteid).order_by('create_date')
                info_sitedescription_video=Sitevideo.objects.filter(site_name_id=siteid).order_by('create_date')
                return render(request,'dashboard/update_sitedescription.html',{'form':fm,'info_sitedescription_image':info_sitedescription_image,'info_sitedescription_video':info_sitedescription_video})
                #return HttpResponseRedirect('/dashboard/info_sitevideo/')
        else:
            pi=Sitevideo.objects.get(pk=id)
            fm=Form_Add_Sitevideo(instance=pi)
            country_count=Country.objects.all().order_by('country_name')
            return render(request,'dashboard/update_sitevideo.html',{'form':fm,'pi':pi,'country_count':country_count})
    else:
        return login(request)

@csrf_exempt
def delete_sitevideo(request):
    if 'name' in request.session:
        if request.method=="POST":
            video_id=request.POST.get('video_id')
            pi=Sitevideo.objects.get(pk=video_id)
            pi.delete()
            return JsonResponse({'status':1})
        else:
            return JsonResponse({'status':0})
    else:
        return login(request)

def map(request):
    if 'name' in request.session:
        info=Category.objects.all().order_by('-modified_date')
        return render(request,'dashboard/map.html',{'categorys':info})
    else:
        return login(request)

@csrf_exempt
def get_state_list(request):
    if request.method=="POST":
        id=request.POST.get('id')
        state=State.objects.values().filter(country_name_id=id)
        state_list=list(state)
        return JsonResponse({'state_list':state_list})

@csrf_exempt
def get_map_data(request):
    if request.method=='POST':
        info=list(Sitedescription.objects.select_related('category_name','state_name').annotate(category_url=F('category_name__id'),name_state=F('state_name__state_name'),name_country=F('state_name__country_name__country_name')).values('id','site_name','site_latitude','site_longitude','category_url','name_state','name_country').order_by('-modified_date'))
        return JsonResponse({'status':1,'sites':info})
    else:
        return JsonResponse({'status':0})

def change_password(request):
    if 'name' in request.session:
        if request.method=='POST':
            form=Form_Change_Login(request.POST)
            if form.is_valid():
                username=form.cleaned_data['login_name']
                old_password=form.cleaned_data['login_old_password']
                new_password=form.cleaned_data['login_new_password']
                try:
                    check=Login.objects.get(login_name=username)
                    ph = PasswordHasher()
                    if ph.verify(check.login_password, old_password):
                        hash = ph.hash(new_password)
                        check.login_password=hash
                        check.save()
                        fm=Form_Change_Login()
                        messages.add_message(request,messages.SUCCESS,'Password reset')
                        return render(request,'dashboard/change_password.html',{'form':fm})
                except: 
                    fm=Form_Add_Login()
                    messages.add_message(request,messages.SUCCESS,'Something is wrong with username or password')
                    return render(request,'ancientsites/login.html',{'form':fm})
        else:
            fm=Form_Change_Login()
            return render(request,'dashboard/change_password.html',{'form':fm})
    else:
        return login(request)

def logout(request):
    request.session.flush()
    request.session.clear_expired()
    return HttpResponseRedirect('/archeological_site/login/')

def dashboard_show(request):
    if 'name' in request.session:
        info=Sitedescription.objects.all().order_by('site_name')
        country_count=Country.objects.all().order_by('country_name')
        category_count=Category.objects.all()
        paginator = Paginator(info, 10) # Show 5 contacts per page.
        first_page = paginator.page(1).object_list
        page_range = paginator.page_range
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'dashboard/dashboard.html',{'sites':info,'country_count':country_count,'category_count':category_count,'page_obj':page_obj,'page_range':page_range,'first_page':first_page})
    else:
        return login(request)
    
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
@csrf_exempt
def get_site_list(request):
    if request.method=="POST":
        stateid=request.POST.get('stateid')
        categoryid=request.POST.get('categoryid')
        info=list(Sitedescription.objects.values().filter(state_name=stateid,category_name=categoryid))
        print(info)
        return JsonResponse({'site_list':info})

@csrf_exempt
def get_sitename(request):
     if request.method=="POST":
        country_id = request.POST.get('id', None)
        print(type(country_id))
        info=""
        if country_id == '0':   
            info=list(Sitedescription.objects.values('id','site_name'))
            print(info)
            return JsonResponse({'sitename':info})
        else:
            info =list(Sitedescription.objects.select_related('state_name').annotate(id_country=F('state_name__country_name_id')).values('id','site_name').filter(id_country=country_id).order_by('site_name'))
            return JsonResponse({'sitename':info})