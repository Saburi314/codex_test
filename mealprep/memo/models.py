from django.db import models

class PreparedItem(models.Model):
    title = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    prepared_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
