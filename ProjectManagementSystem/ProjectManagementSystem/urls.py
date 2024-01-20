"""
URL configuration for ProjectManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from management import views

urlpatterns = [
    path('add_developer/', views.add_developer , name='add_developer'),
    path('update_developer/<int:developer_id>' , views.update_developer , name='update_developer' ),
    path('delete_developer/<int:developer_id>', views.delete_developer, name='delete_developer'),

    path('admin/', admin.site.urls),
    path('', views.index , name='index'),
    path('add_project/', views.add_project , name='add_project'),
    path('update_project/<int:project_id>' , views.update_project , name='update_project' ),
    path('delete_project/<int:project_id>', views.delete_project, name='delete_project'),
    path('accounts/', include('accounts.urls')),

]


