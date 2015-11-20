from django.db import models

class Problem(models.Model):
	number = models.PositiveSmallIntegerField(blank=False)
	hold_set = models.CharField(max_length=100, blank=False)
	setup = models.CharField(max_length=100, blank=False)
	name = models.CharField(max_length=100, blank=False)
	setter = models.CharField(max_length=100, blank=False)
	grade = models.CharField(max_length=4, blank=False)
	start = models.CharField(max_length=100, blank=False)
	path = models.CharField(max_length=100, blank=False)
	finish = models.CharField(max_length=100, blank=False)

	def __str__(self):
		return self.grade + ": " + self.name + ' (' + self.hold_set +')'