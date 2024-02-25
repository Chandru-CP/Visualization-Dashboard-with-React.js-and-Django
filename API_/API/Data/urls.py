from django.urls import path
from .views import *


urlpatterns = [
    path('get_form_data/', get_form_data),
    path('get_end_year_data/<str:end_year>/', get_end_year_data),
    path('get_topic_data/<str:topic>/', get_topic_data),
    path('get_sector_data/<str:sector>/', get_sector_data),
    path('get_region_data/<str:region>/', get_region_data),
    path('get_pestle_data/<str:pestle>/', get_pestle_data),
    path('get_source_data/<str:source>/', get_source_data),
    path('get_country_data/<str:country>/', get_country_data),
    path('upload_json/', upload_json,name='upload_json'),
    path('delete_form_data/', delete_form_data),
    path('get_swot_data/',get_swot_data,name='impact_list'),
]