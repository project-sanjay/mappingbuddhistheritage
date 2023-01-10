
from django import forms
from django.urls import path
from .views import dashboard_show
from .views import info_category,add_category,update_category,delete_category,delete_category_info
from .views import info_sitedescription,add_sitedescription,update_sitedescription,delete_sitedescription,delete_sitedescription_info
from .views import info_siteimage,info_siteimage_individual,add_siteimage,update_siteimage,delete_siteimage
from .views import info_sitevideo,info_sitevideo_individual,add_sitevideo,update_sitevideo,delete_sitevideo
from .views import logout
from .views import get_state_list,get_category_list
from .views import region,add_country,edit_country,delete_country
from .views import add_state,delete_state,edit_state
from .views import map,get_map_data
from .views import site
from .views import change_password
from .views import get_pagination,get_pagination_all,get_pagination_country,get_pagination_state,get_pagination_category
from .views import autocomplete_search,get_site_id
from .views import get_sitename,get_site_list
urlpatterns = [
        path('',dashboard_show,name='dashboard_show'),

        path('site/<int:id>',site,name='site'),
        path('change_password',change_password,name='change_password'),

        path('info_category/',info_category,name='info_category'),
        path('info_category/add_category/',add_category,name='add_category'),
        path('info_category/update_category/<int:id>',update_category,name='update_category'),
        path('info_category/delete_category/<int:id>',delete_category,name='delete_category'),
        path('info_category/delete_category_info/<int:id>',delete_category_info,name='delete_category_info'),

        path('region/',region,name='region'),
        path('region/add_country',add_country,name='add_country'),
        path('region/edit_country',edit_country,name='edit_country'),
        path('region/delete_country',delete_country,name='delete_country'),
        path('region/add_state',add_state,name='add_state'),
        path('region/delete_state',delete_state,name='delete_state'),
        path('region/edit_state',edit_state,name='edit_state'),


        path('info_sitedescription/',info_sitedescription,name='info_sitedescription'),
        path('info_sitedescription/add_sitedescription/',add_sitedescription,name='add_sitedescription'),
        path('info_sitedescription/update_sitedescription/<int:id>',update_sitedescription,name='update_sitedescription'),
        path('info_sitedescription/delete_sitedescription/<int:id>',delete_sitedescription,name='delete_sitedescription'),
        path('info_sitedescription/delete_sitedescription_info/<int:id>',delete_sitedescription_info,name='delete_sitedescription_info'),

        path('info_siteimage/',info_siteimage,name='info_siteimage'),
        path('info_siteimage/info_siteimage_individual/<int:id>',info_siteimage_individual,name='info_siteimage_individual'),
        path('info_siteimage/add_siteimage/',add_siteimage,name='add_siteimage'),
        path('info_siteimage/update_siteimage/<int:id>',update_siteimage,name='update_siteimage'),
        path('info_siteimage/delete_siteimage',delete_siteimage,name='delete_siteimage'),

        path('info_sitevideo/',info_sitevideo,name='info_sitevideo'),
        path('info_sitevideo/info_sitevideo_individual/<int:id>',info_sitevideo_individual,name='info_sitevideo_individual'),
        path('info_sitevideo/add_sitevideo/',add_sitevideo,name='add_sitevideo'),
        path('info_sitevideo/update_sitevideo/<int:id>',update_sitevideo,name='update_sitevideo'),
        path('info_sitevideo/delete_sitevideo',delete_sitevideo,name='delete_sitevideo'),

        path('get_state_list/',get_state_list,name='get_state_list'),

        path('map/',map,name='map'),
        path('map/get_map_data',get_map_data,name='get_map_data'),
        
        path('/',logout,name='logout'),
    
        path('get_state_list/',get_state_list,name='get_state_list'),
        path('get_category_list/',get_category_list,name='get_category_list'),
        path('get_pagination/',get_pagination,name='get_pagination'),
        path('get_pagination_all/',get_pagination_all,name='get_pagination_all'),
        path('get_pagination_country/',get_pagination_country,name='get_pagination_country'),
        path('get_pagination_state/',get_pagination_state,name='get_pagination_state'),
        path('get_pagination_category/',get_pagination_category,name='get_pagination_category'),
        path('autocomplete_search/',autocomplete_search,name='autocomplete_search'),
        path('get_site_id/',get_site_id,name='get_site_id'),
        path('get_sitename/',get_sitename,name='get_sitename'),
         path('get_site_list/',get_site_list,name='get_site_list'),
]

