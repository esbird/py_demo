from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    def __str__(self): #设置后台模板 表标题显示
        return "<Article: %s>" % self.title


