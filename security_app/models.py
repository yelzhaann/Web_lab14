from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=100, verbose_name="Автор")
    content = models.TextField(verbose_name="Мазмұн")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Жазылған уақыт")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Түсініктеме"
        verbose_name_plural = "Түсініктемелер"

    def __str__(self):
        return f"{self.author}: {self.content[:50]}"
