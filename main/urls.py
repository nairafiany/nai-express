from django.urls import path
from main import views
from main.views import create_product_flutter, edit_product, show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, create_product_ajax
from django.conf.urls.static import static
from django.conf import settings
from main.views import register, login_user, logout_user, delete_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('', views.show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_mood_flutter'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)