from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet
from django.views.generic import TemplateView
from tasks.views import IndexView 
from django.contrib import admin

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html')),  # nova rota adicionada aqui
   # path('', IndexView.as_view(), name='index'),
]
