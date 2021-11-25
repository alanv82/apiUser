from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
import json

# Create your views here.


class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            jd = json.loads(request.body)
            usuarios = list(Usuario.objects.filter(email=jd['email']).values())
            if len(usuarios) > 0:
                usuario = usuarios[0]
                datos = {'message': "Success", 'usuario': usuario}
                return JsonResponse(datos)
            else:
                datos = {'message': "Usuario no encontrado..."}
                return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {'message': "Success", 'usuarios': usuarios}
            else:
                datos = {'message': "Usuarios no encontrados..."}
            return JsonResponse(datos)



    def post(self, request):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(email=jd['email']).values())
        if len(usuarios) > 0:
            datos = {'message': 'Email ya exitente..'}
            return JsonResponse(datos)
        else:
            Usuario.objects.create(email=jd['email'], password=jd['password'])
            datos = {'message': "Success"}
            return JsonResponse(datos)


    def put(self, request, email):
        jd = json.loads(request.body)
        usuario = list(Usuario.objects.filter(email=email).values())
        if len(usuario) > 0:
            usuario = Usuario.objects.get(email=jd['email'])
            usuario.email = jd['email']
            usuario.password = jd['password']
            usuario.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, email):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(email=email).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(email=jd['email']).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario no encontrado..."}
        return JsonResponse(datos)  