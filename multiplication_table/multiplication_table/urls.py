"""multiplication_table URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from table.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserView.as_view(), name='user'),
    path('add_kid', AddNewKidView.as_view(), name='new_kid'),
    path('edit_profile', EditProfileView.as_view(), name='edit_profile'),
    # ---------------------------------------
    path('choice/', CategorySelectionView.as_view()),
    path('match/', MatchView.as_view(), name='match'),
    path('history/', HistoryView.as_view(), name='history'),
    path('biology/', BiologyView.as_view(), name='biology'),

    # --------------------------------------------
    path('test/', TestView.as_view(), name='test'),
    path('test1/', TestPointsView.as_view(), name='test1'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
