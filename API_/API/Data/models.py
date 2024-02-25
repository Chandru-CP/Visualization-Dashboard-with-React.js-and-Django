from django.db import models

class Analysis(models.Model):
    end_year = models.IntegerField(blank=True)
    intensity = models.IntegerField(blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    topic = models.CharField(max_length=100, null=True, blank=True)
    insight = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    start_year = models.IntegerField(blank=True)
    impact = models.CharField(max_length=255, default=0, blank=True)
    added = models.DateTimeField(auto_now_add=True, blank=True)
    published = models.DateTimeField( blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    relevance = models.IntegerField(default=0)
    pestle = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    likelihood = models.IntegerField(blank=True)

