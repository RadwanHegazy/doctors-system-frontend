from globals.request_manager import Action
from django.shortcuts import render, redirect
from frontend.settings import MAIN_URL

def LoginView (request) : 

    context = {}
    if request.method == "POST" : 
        def get (name) : return request.POST.get(name,None)
        
        data = {
            'email' : get('email'),
            'password' : get('password'),
        }
        
        action = Action(
            url = MAIN_URL + "/doctor/login/",
            data = data
        )

        action.post()

        if action.is_valid() : 
            response = redirect('profile')
            response.set_cookie('user',action.json_data()['access'])
            return response
        else:
            context['error'] = 'البيانات التي ادخلتها غير صحيحة'

    return render(request,'login.html',context)