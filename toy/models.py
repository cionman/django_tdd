from django.db import models


class Toy(models.Model):
    title = models.CharField(max_length=100)
    toy_image = models.ImageField(upload_to='toy/%Y/%m/%d', null=True, blank=True)
    tech_stack = models.ManyToManyField('TechStack', related_name='toy_techstack_set', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    desc = models.TextField()
    url = models.CharField(max_length=200)
    idate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "toy"
        ordering = ["-idate"]

    def __str__(self):
        return self.title


class TechStack(models.Model):
    stack_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'tech_stack'

    def __str__(self):
        return self.stack_name