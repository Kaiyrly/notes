from django.db import models

class Document(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField(blank = True, null = True)

    created_at = models.TimeField(auto_now_add = True)
    modififed_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ('title',)