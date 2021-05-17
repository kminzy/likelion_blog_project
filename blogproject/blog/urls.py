from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import blog.views
import portfolio.views
from .views import *
from django.conf import settings


urlpatterns = [
    path('<int:blog_id>',blog.views.detail, name="detail"), #blog/id형식으로 주소에 출력, id받아옴
    path('list/',blog.views.postlist, name="postlist"),
    path('about_me/',blog.views.about, name="about"),
    path('new/', blog.views.new, name="new"),
    path('create/', blog.views.create, name="create"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('edit/<int:id>', blog.views.edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)