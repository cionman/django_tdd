from django.db import models


class Toy(models.Model):
    title = models.CharField(max_length=100)
    toy_image = models.ImageField(upload_to='toy/%Y/%m/%d')
    tech_stack = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    desc = models.TextField()
    url = models.CharField(max_length=200)
    idate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "toy"
        ordering = ["idate"]

    def __str__(self):
        return self.title
