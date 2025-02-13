from django.db import models
from django.urls import reverse


# Create your models here.
class FamilyMember(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    bio = models.TextField(blank=True, verbose_name="Биография")
    bornDate = models.DateField(verbose_name="Дата рождения")
    deathDate = models.DateField(blank=True, null=True, verbose_name="Дата смерти")
    photo = models.ImageField(upload_to='photos/', default=None, blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'человека'
        verbose_name_plural = 'Члены семьи'

    def get_absolute_url(self):
        return reverse('card', kwargs={'man_id': self.pk})


class Relations(models.Model):
    parent = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='parent', blank=True, null=True)
    child = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    class Meta:
        verbose_name = 'Взаимотношение'
        verbose_name_plural = 'Взаимотношения'

    def __str__(self):
        return f"Родитель: {self.parent.name} -> ребенок {self.child.name}"


class Images(models.Model):
    image = models.ImageField(upload_to='photos/', default=None, blank=True, null=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фоторулетка'
