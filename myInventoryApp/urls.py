from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('',views.index, name='index'),
    path('add/',views.add,name='add'),
    path('add/add_item/',views.add_item, name='add_item'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('update/update_item/<int:id>',views.update_item,name='update_item'),
    path('sale/',views.sell,name='sale'),
    path('sale/sell_item/',views.sell_item,name='sell_item'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)