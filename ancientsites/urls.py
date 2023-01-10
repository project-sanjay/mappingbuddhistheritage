
from django.urls import path
from .views import index,get_map_data,archeological_site,archeological_site_images,archeological_site_search
from .views import get_state_list,get_category_list
from .views import login,aboutus
from .views import get_pagination,get_pagination_all,get_pagination_country,get_pagination_state,get_pagination_category
from .views import autocomplete_search,get_site_id


urlpatterns = [
 path('',index,name='index'),
 
 path('get_map_data',get_map_data,name='get_map_data'),
 
 path('get_state_list/',get_state_list,name='get_state_list'),
 path('get_category_list/',get_category_list,name='get_category_list'),
 path('get_pagination/',get_pagination,name='get_pagination'),
 path('get_pagination_all/',get_pagination_all,name='get_pagination_all'),
 path('get_pagination_country/',get_pagination_country,name='get_pagination_country'),
 path('get_pagination_state/',get_pagination_state,name='get_pagination_state'),
 path('get_pagination_category/',get_pagination_category,name='get_pagination_category'),
 path('autocomplete_search/',autocomplete_search,name='autocomplete_search'),
 path('get_site_id/',get_site_id,name='get_site_id'),

 path('archeological_site/<int:id>',archeological_site,name='archeological_site'),
 path('archeological_site/archeological_site_images/<int:site_id>/<int:image_id>',archeological_site_images,name='archeological_site_images'),
 path('archeological_site_search',archeological_site_search,name='archeological_site_search'),
 path('archeological_site/login/',login,name='login'),
 path('archeological_site/aboutus/',aboutus,name='aboutus'),
]

