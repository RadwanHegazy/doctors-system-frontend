from django.http import HttpResponse, Http404
from django.shortcuts import render
from globals.request_manager import Action
from frontend.settings import MAIN_URL

def RegisteWithDoctorView (request, doc_id) : 
    context = {}

    doctor = Action(
        url = MAIN_URL + f"/client/get/{doc_id}/"
    )

    doctor.get()

    context['doctor'] = doctor.json_data()


    if request.method == "POST" : 
         
        def get (name) : return request.POST.get(name,None)
        
        data = {
            'full_name' : get('full_name'),
            'email' : get('email'),
            'age' : get('age'),
            'gender' : get('gender'),
            'description' : get('description'),
        }
        
        action = Action(
            url = MAIN_URL + f"/client/create/{doc_id}/",
            data = data
        )


        if 'picture' in request.FILES :
            picture = request.FILES['picture']
            action.files = {
                'picture' : picture
            }

        action.post()
        response = action.json_data()

        context['ticket'] = response['qr']

    return render(request,'register-with-doctor.html',context)
