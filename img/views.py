from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from img.models import Github

from .forms import GithubForm

import requests
from bs4 import BeautifulSoup as bs

# Create your views here.


@login_required
def home(request):
    if request.method == 'POST':
        form = GithubForm(request.POST)
        if form.is_valid():
            github = form.save(commit=False)
            github.username = request.user
            github.github_username = form.cleaned_data.get('github_username')
            url = 'https://github.com/' + \
                form.cleaned_data.get('github_username')
            res = requests.get(url)
            soup = bs(res.content)  # warning
            avatar = soup.find('img', {'alt': 'Avatar'})['src']
            github.github_image = avatar
            github.save()
        redirect('home')
    else:
        form = GithubForm()
    return render(request, 'home.html', {'form': form})


@login_required
def images(request):
    github = Github.objects.filter(username=request.user)
    return render(request, 'images.html', {'github': github})
