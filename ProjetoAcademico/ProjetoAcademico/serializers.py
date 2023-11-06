from rest_framework import serializers
from BlogApp.models import PreferenciaAssunto, BlogApp

class PreferenciaAssuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferenciaAssunto
        fields = ('Assunto_Nome')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('UsuarioId',
                  'Usuario_Email',
                  'Usuario_Data_Nascimento',
                  'Usuario_Data_Cadastro',
                  'Usuario_Senha',
                  'Usuario_Descricao',
                  'Usuario_Foto_Perfil',
                  'Usuario_Assuntos')

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = ('Postagem_Autor',
                  'Postagem_Conteudo',
                  'Postagem_Data')

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('Postagem',
                  'Comentario_Autor',
                  'Comentario_Texto',
                  'Comentario_Data')

class SeguirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguir
        fields = ('Seguidor',
                  'Seguindo')