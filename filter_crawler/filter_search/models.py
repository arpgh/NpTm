from django.db import models

class FilterSearch(models.Model):
	level1 = models.CharField(max_length=255, null=True, blank=True)
	level2 = models.CharField(max_length=255, null=True, blank=True)
	level3 = models.CharField(max_length=255, null=True, blank=True)
	level4 = models.CharField(max_length=255, null=True, blank=True)
	level5 = models.CharField(max_length=255, null=True, blank=True)
	videos = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.level1
