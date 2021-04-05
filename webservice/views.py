from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import urllib.request 

def awal(request):
    context = {
        "nav": 'Hallo'
    }
    return render(request, 'awal.html', context)

def index(request):
    response = requests.get('https://batikita.herokuapp.com/index.php/batik/all').json()
    context = {
        "all_item": response,
        "nav": 'Home'
    }
    return render(request, 'index.html', context)


def detail(request):
    link = request.POST['link']
    detail_batik = link.replace(" ", "_").lower()
    response = requests.get('https://batikita.herokuapp.com/index.php/batik/'+detail_batik).json()
    context = {
        "detail": response,
        "nav": 'Detail'
    }
    return render(request, 'detail.html', context)

def download_yt(request):
    if request.method == 'GET':
        context = {
            "nav": 'Download Video'
        }
        return render(request, 'yt_video.html', context)
    elif request.method == 'POST':
        link = {
            "url": request.POST['link']
        }
        response = requests.post("http://sosmeeed.herokuapp.com:80/api/youtube/video", data=link).json()
        url = response['data'][0]['video']['url']
        return redirect(url)


def download_twitter(request):
    if request.method == 'GET':
        context = {
            "nav": 'Download Video'
        }
        return render(request, 'twit_video.html', context)
    elif request.method == 'POST':
        link = {
            "url": request.POST['link']
        }
        response = requests.post("http://sosmeeed.herokuapp.com:80/api/twitter/video", data=link).json()
        url = response['data']['data'][0]['link']
        return redirect(url)


def playstore(request):
    if request.method == 'GET':
        context = {
            "nav": 'Link App Playstore'
        }
        return render(request, 'playstore.html', context)
    elif request.method == 'POST':
        suggest = request.POST['suggest']
        response = requests.get("https://api-gplay.azharimm.tk/apps?suggest="+suggest).json()
        context = {
            "all_item": response
        }
        return render(request, 'playstore_detail.html', context)


def playstore_list(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        response = requests.get('http://api-gplay.azharimm.tk/apps/?q='+keyword).json()
        context = {
            "all_item": response,
            "nav": 'Aplikasi'
        }
        return render(request, 'playstore_listapp.html', context)


def sekolah(request):
    if request.method == 'GET':
        response = requests.get('https://datasekolahapi.herokuapp.com/api/data/').json()
        context = {
            "all_item": response,
            "nav": 'Pilih Jenjang'
        }
        return render(request, 'sekolah.html', context)


def sekolah_jenjang(request, jenjang):
    response = requests.get('https://datasekolahapi.herokuapp.com/api/data/'+jenjang).json()
    context = {
        "all_item": response,
        "nav": 'Pilih Jenjang'
    }
    return render(request, 'sekolah_jenjang.html', context)


def sekolah_provinsi(request, jenjang, provinsi):
    response = requests.get('https://datasekolahapi.herokuapp.com/api/data/'+jenjang+'/'+provinsi).json()
    context = {
        "all_item": response,
        "nav": 'Pilih Jenjang'
    }
    return render(request, 'sekolah_provinsi.html', context)


def sekolah_daerah(request, jenjang, provinsi, daerah):
    response = requests.get('https://datasekolahapi.herokuapp.com/api/data/'+jenjang+'/'+provinsi+'/'+daerah).json()
    context = {
        "all_item": response,
        "nav": 'Detail Sekolah'
    }
    return render(request, 'detail_sekolah.html', context)