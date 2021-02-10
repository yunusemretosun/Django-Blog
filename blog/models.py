from django.db import models
from django.urls import reverse  # bir objenin ismini kullanarak iliski saglar
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20)
    # ForeignKey gibi many to many iliskilerinde on_delete methodunu kullanmaliyiz.
    # CASCADE i kullanmamizin amaci egerki bir user silinirse ona dair postlarda silinir.
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
