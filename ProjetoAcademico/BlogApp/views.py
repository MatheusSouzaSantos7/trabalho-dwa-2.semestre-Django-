from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BlogApp.models import Usuario, Postagem
from BlogApp.serializers import UsuarioSerializer, PostagemSerializer


@csrf_exempt


def usuarios_api(request, id=0):
    if request.method == "GET":
        usuarios = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuario_serializer.data, safe=False)

    elif request.method == "POST":
        usuario_dados = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_dados)
        try:
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return JsonResponse("CADASTRO REALIZADO COM SUCESSO!", safe=False)
        except IntegrityError as e:
            return JsonResponse({"error": "Não foi possível cadastrar este Usuário! Já existe um usuário com o mesmo Nickname ou Email.", "details": str(e)}, safe=False)
        
        return JsonResponse({"error": "Não foi possível cadastrar este Usuário!", "details": usuario_serializer.errors}, safe=False)

    elif request.method == "PUT":
        usuario_dados = JSONParser().parse(request)
        usuario = Usuario.objects.get(Usuario_Id=usuario_dados['Usuario_ID'])
        usuario_serializer = UsuarioSerializer(usuario, data=usuario_dados)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("CADASTRO ATUALIZADO COM SUCESSO!", safe=False)
        return JsonResponse({"error": "Não foi possível atualizar este Usuário!", "details": usuario_serializer.errors}, safe=False)

    elif request.method == "DELETE":
        usuario = Usuario.objects.get(Usuario_ID=id)
        usuario.delete()
        return JsonResponse("CADASTRO DELETADO COM SUCESSO", safe=False)

def postagens_api(request, id=0):
    if request.method == "GET":
        postagens = Postagem.objects.all()
        postagem_serializer = PostagemSerializer(postagens, many=True)
        return JsonResponse(postagem_serializer.data, safe=False)

    elif request.method == "POST":
        postagem_dados = JSONParser().parse(request)
        postagem_serializer = PostagemSerializer(data=postagem_dados)
        if postagem_serializer.is_valid():
            postagem_serializer.save()
            return JsonResponse("Postagem cadastrada com sucesso!", safe=False)
        return JsonResponse({"error": "Não foi possível cadastrar esta Postagem!", "details": postagem_serializer.errors}, safe=False)

    elif request.method == "PUT":
        postagem_dados = JSONParser().parse(request)
        postagem = Postagem.objects.get(id=id)
        postagem_serializer = PostagemSerializer(postagem, data=postagem_dados)
        
        if postagem_serializer.is_valid():
            postagem_serializer.save()
            return JsonResponse("Postagem atualizada com sucesso!", safe=False)
        return JsonResponse({"error": "Não foi possível atualizar esta Postagem!", "details": postagem_serializer.errors}, safe=False)

    elif request.method == "DELETE":
        postagem = Postagem.objects.get(id=id)
        postagem.delete()
        return JsonResponse("Postagem deletada com sucesso", safe=False)

