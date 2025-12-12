from django.db import models

class TextoSobre(models.Model):
    texto = models.TextField()

    def __str__(self):
        return f'{self.texto}'