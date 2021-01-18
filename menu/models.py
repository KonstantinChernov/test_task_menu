from django.db import models


class Menu(models.Model):

    parent = models.ForeignKey('self',
                               null=True,
                               blank=True,
                               related_name='children',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    url = models.SlugField(max_length=200)

    def __str__(self):
        return self.title
