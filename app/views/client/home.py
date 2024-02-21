from django.shortcuts import render
from globals.request_manager import Action
from frontend.settings import MAIN_URL

def ClientHomeView (request) :

    context = {} 



    url = "/client/get/"

    if 'search' in request.GET:
        search = request.GET['search']
        url += "?search=" + search
        context['current_search'] = search

    if 'department' in request.GET:
        dep = request.GET['department']
        url += "&department=" + dep
        context['current_dep'] = dep

    action = Action(
        url = MAIN_URL + url,
    )

    action.get()

    context['doctors'] = action.json_data()

    depratmetns = Action(
        url = MAIN_URL + "/doctor/get/departments/"
    )

    depratmetns.get()

    context['departments'] = depratmetns.json_data()

    return render(request,'index.html',context)