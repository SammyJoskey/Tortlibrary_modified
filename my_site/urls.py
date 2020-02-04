"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from p_library import views
from p_library.views import AuthorEdit, AuthorList, BookEdit, BookList, FriendEdit, FriendList, PublisherList

app_name = 'p_library'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.home, name='home'),
    path('book/', BookList.as_view(), name='book_list'),
    path('book/add',  BookEdit.as_view(), name='book_add'),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('author/add/', AuthorEdit.as_view(), name='author_add'),
	path('author/', AuthorList.as_view(), name='author_list'),
    path('friend/add/', FriendEdit.as_view(), name='friend_add'),
    path('friend/', FriendList.as_view(), name='friend_list'),
    path('publisher/', PublisherList.as_view(), name='publisher_list'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)