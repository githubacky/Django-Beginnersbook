from django.db import models
from django.utils import timezone

# Create your models here.
class CreatedAt(models.Model):
	name = models.CharField('作成日', max_length=255)
	
class Category(models.Model):
	name = models.CharField('カテゴリ名', max_length=255)
	
	def __str__(self):
		return self.name
		
class Diary(models.Model):
#	category = models.CharField('カテゴリ', max_length=255)
	category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
	
	text = models.TextField('本文')
#	created_at = models.DateTimeField('作成日', default=timezone.now)
#	created_at = models.DateTimeField('作成日')	# 追加
	created_at = models.ForeignKey(CreatedAt, verbose_name='作成日', null=True, blank=True, on_delete=models.PROTECT)

	# 追加
	def __str__(self):
		return 'カテゴリ: {} 本文: {}'.format(self.category, self.text[:10])

	def get_title(self):
		return 'カテゴリ:{} 本文:{}'.format(self.category, self.text[:10])

