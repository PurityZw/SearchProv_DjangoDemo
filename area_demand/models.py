from django.db import models


# Create your models here.
# 自定义模型管理器类
class AreaInfoManager(models.Manager):
    def my_all(self):
        return self.all()


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=64)
    aParent = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        db_table = 'areas'

    def __str__(self):
        return self.atitle

    # 调用自定义管理器类
    areas = AreaInfoManager()
