from django.db import models
from DjangoUeditor.models import UEditorField
from django. urls import reverse
# Create your models here.

class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')

    nav_display = models.BooleanField('导航显示', default=False)
    home_display = models.BooleanField('首页显示', default=False)

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))
 
    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']  # 按照哪个栏目排序

class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')
 
    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)
    #unique=True)
 
    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者',on_delete=models.CASCADE,)
    # content = UEditorField('内容', height=300, width=1000,
    #     default=u'', blank=True, imagePath="uploads/images/",
    #     toolbars='besttome', filePath='uploads/files/')
    content = UEditorField(verbose_name='内容',width=800, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":12040000},default='')
 
    published = models.BooleanField('正式发布', default=True)

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def get_absolute_url(self):
        #return reverse('article', args=(self.slug,))
        return reverse('article', args=(self.pk, self.slug))
 
    def __str__(self):
        return self.title
 
    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'