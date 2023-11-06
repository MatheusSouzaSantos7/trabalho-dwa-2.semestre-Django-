from rest_framework import serializers
from BlogApp.models import Usuario, Postagem


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('Usuario_Id',
                  'Usuario_Email',
                  'Usuario_Data_Nascimento',
                  'Usuario_Data_Cadastro',
                  'Usuario_Senha',
                  'Usuario_Nickname',)

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = ('Postagem_Autor',
                  'Postagem_Conteudo',
                  'Postagem_Data',)
