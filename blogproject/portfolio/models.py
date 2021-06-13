from django.db import models

# Create your models here.

class Portfolio(models.Model): # Model 클래스 메소드 사용
    title = models.CharField(max_length=200) # 제목은 최대 200자
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length = 100)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title
