from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BlogApp.models import PreferenciaAssunto,Usuario, Postagem, Comentario,Seguir
from BlogApp.serializers import PreferenciaAssuntoSerializer, UsuarioSerializer, PostagemSerializer,ComentarioSerializer, SeguirSerializer 

@csrf_exempt
def usuarios_api(request, id=0):
    if request.method == "GET":
        usuarios = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuario_serializer.data, safe=False)
    elif request.method == "POST":
        usuario_dados = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_dados)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("CADASTRO REALIZADO COM SUCESSO!", safe=False)
        return JsonResponse("Não foi possível cadastrar este Usuário!", safe=False)
    elif request.method == "PUT":
        usuario_dados = JSONParser().parse(request)
        usuario = Usuario.objects.get(Usuario_Id=usuario_dados['Usuario_ID'])
        usuario_serializer = UsuarioSerializer(usuario, data=usuario_dados)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("CADASTRO ATUALIZADO COM SUCESSO!", safe=False)
        return JsonResponse("Não foi possível atualizar o cadastro deste Usuário!", safe=False)
    elif request.method == "DELETE":
        usuario = Usuario.objects.get(Usuario_ID=id)
        usuario.delete()
        return JsonResponse("CADASTRO DELETADO COM SUCESSO", safe=False)
