from django.db import models

# Create your models here.
# 가공하고자 하는 데이터 종류, 어떤 정보 처리되길 원하는지 class로 정의

class Blog(models.Model): # Model 클래스 메소드 사용
    title = models.CharField(max_length=200) # 제목은 최대 200자
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "blog/", blank=True, null=True) #업로드할 폴더 지정, settings.py 에 MEDIA_URL로 지정해둔 media폴더 안에 blog폴더를 만들어서 관리

    def __str__(self): #self인자값 받아서 title 반환
        return self.title

    def summary(self):
        return self.body[:50] #100자 이하로 출력
