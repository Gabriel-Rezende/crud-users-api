from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class User(models.Model):
    nome = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)

    # Máscara para (XX) 9XXXX-XXXX e (XX) XXXX-XXXX
    telefone = models.CharField(validators=[
                                                RegexValidator(regex='^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$',
                                                message='Telefone Inválido', code='nomatch')
                                            ], max_length=15)
    class Meta:
        ordering = ['nome']
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def to_dict(self):
        return {'nome': self.nome, 'email': self.email, 'telefone': self.telefone}

    def __str__(self):
        return '{} {}'.format(self.nome, self.email, self.telefone)

