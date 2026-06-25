
from django.contrib import admin
from django.urls import path
from civis import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='accueil'),
    path('detail_chef/<int:id>/',views.detail_chef,name='detail_chef'),
    path('civilisation',views.all_civilisation,name='civilisation'),
    path('Chef',views.all_chef,name='chef'),
    path('detail_civilisation/<int:id>/',views.detail_civilisation,name='detail_civilisation'),

]

