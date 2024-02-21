from globals.request_manager import Action
from django.shortcuts import render, redirect
from globals.decorators import login_required
from frontend.settings import MAIN_URL


@login_required
def DoctorHome (request) : 
    
    if 'check' in request.GET:
        client_id = request.GET.get('check',None)
        
        action = Action(
            url = MAIN_URL + f'/client/update/ticket/{client_id}/',
            headers={'Authorization':f"Bearer {request.COOKIES.get('user')}"}
        )

        action.patch()

        return redirect('profile')

    return render(request,'doc-profile.html')
