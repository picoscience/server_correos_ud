from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import *

def index(request):
    return render(request,'home/index.html')


def login(request):
    return render(request,'home/login.html')

def send(request):

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    public_ip = get_client_ip(request)

    context = {
        'subject':request.POST.get('subject'),
        'message':request.POST.get('message'),
    }
    correo = correos_enviados(subject=context['subject'],message=context['message'],ip=public_ip)
    correo.save()

    mess = context['message'] + ' from: ' + public_ip

    send_mail(context['subject'],mess,'picoscience.09@gmail.com',['jcacostap09@gmail.com'])
    print(context['subject'],'\n\n'+context['message'],'\n'+public_ip)
    return JsonResponse(context)