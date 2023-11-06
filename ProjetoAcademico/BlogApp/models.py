from django.db import models

# Create your models here.

    
class Usuario(models.Model):
    Usuario_Id = models.AutoField(primary_key=True)
    Usuario_Nickname = models.CharField(max_length = 30, unique=True)
    Usuario_Email = models.CharField(max_length = 60, unique=True)
    Usuario_Data_Nascimento = models.DateField()
    Usuario_Data_Cadastro = models.DateField()
    Usuario_Senha = models.CharField(max_length=128)  # Armazene senhas criptografadas

class Postagem(models.Model):
    Postagem_Autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Postagem_Conteudo = models.TextField()
    Postagem_Data = models.DateTimeField(auto_now_add=True)

