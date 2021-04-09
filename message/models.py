from django.utils import timezone
from django.db import models


# Create your models here.
class MessageBoard(models.Model):
    mb_content = models.TextField()  # 留言内容
    mb_time = models.DateTimeField(default=timezone.now)  # 留言的日期
    mb_isShow = models.BooleanField(default=True)  # 留言是否可见

    class Meta:
        db_table = "message_board"  # 为数据库表指定名称
