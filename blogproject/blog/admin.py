from django.contrib import admin
from .models import Blog

# Register your models here.

#블로그 사이트 글 등록
#블로그 클래스 받아옴
admin.site.register(Blog)