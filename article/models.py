from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30,verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    # create_time = models.DateTimeField(default=timezone.now())
    created_time = models.DateTimeField(auto_now_add = True,verbose_name="创建时间")
    last_updated_time = models.DateTimeField(auto_now=True,verbose_name="最近更新时间")#修改的时候就会更新时间
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1,verbose_name="作者")
    is_deleted = models.BooleanField(default=False,verbose_name="是否已删除")
    readed_num = models.IntegerField(default=0,verbose_name="阅读数量")
    def __str__(self): #设置后台模板 表标题显示
        return "<Article: %s>" % self.title


