
#encoding=utf-8

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests

@login_required
def index(request):
  return redirect('/')

@login_required
def kauniainen_services(request):
  return render(request, 'dreamgadgets/kauniainen_services.html')

@login_required
def dreamschool_services(request):
  return render(request, 'dreamgadgets/dreamschool_services.html')

@login_required
def video_service(request):
  return render(request, 'dreamgadgets/video_service.html')

@login_required
def fisholution(request):
  return render(request, 'dreamgadgets/fisholution.html')

@login_required
def unelmasalkku(request):
  return render(request, 'dreamgadgets/unelmasalkku.html')

@login_required
def dropbox(request):
  return render(request, 'dreamgadgets/dropbox.html')

@login_required
def sporttigalaksi(request):
  return render(request, 'dreamgadgets/sporttigalaksi.html')

@login_required
def pelitehdas(request):
  return render(request, 'dreamgadgets/pelitehdas.html')

@login_required
def steinerkoulu_espoo(request):
  return render(request, 'dreamgadgets/steinerkoulu_espoo.html')

@login_required
def steinerkoulu_espoo_services(request):
  return render(request, 'dreamgadgets/steinerkoulu_espoo_services.html')

@login_required
def steinerkoulu_tampere(request):
  return render(request, 'dreamgadgets/steinerkoulu_tampere.html')

@login_required
def steinerkoulu_tampere_services(request):
  return render(request, 'dreamgadgets/steinerkoulu_tampere_services.html')

@login_required
def google_calendar(request):
  return render(request, 'dreamgadgets/google_calendar.html')

@login_required
def google_drive(request):
  return render(request, 'dreamgadgets/google_drive.html')

@login_required
def innoomnia(request):
  return render(request, 'dreamgadgets/innoomnia.html')

@login_required
def moodle(request):
  return render(request, 'dreamgadgets/moodle.html')

@login_required
def wiki(request):
  return render(request, 'dreamgadgets/wiki.html')

@login_required
def blogi(request):
  return render(request, 'dreamgadgets/blogi.html')