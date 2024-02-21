from django.http import HttpResponse
from django.shortcuts import redirect

def LogoutView (request) : 
    reponse = redirect('home')
    reponse.delete_cookie('user')
    return reponse
