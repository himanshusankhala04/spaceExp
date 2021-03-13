from django.shortcuts import render, HttpResponse
import requests
import json


# Create your views here.

def index(request):
    element=[]
    if request.method == "GET" and request.is_ajax():
        url = "https://api.spaceXdata.com/v3/launches?limit=100"
        url += request.GET['addurl']
        print("in here")
    else:
        url = "https://api.spaceXdata.com/v3/launches?limit=100"
    print(url)
    try:
        response = requests.get(url)
        data = response.json()
        
        
        if response.status_code == 200:
            for i in range(len(data)):
                dic1 = data[i]
                element.append({'name':dic1['mission_name'] + " #" + str(dic1['flight_number']),
                                'mission_ids':dic1['mission_id'], 
                                'launch_yrs':dic1['launch_year'], 
                                'launch_suc':str(dic1['launch_success']), 
                                'land_suc':str(dic1['rocket']['first_stage']['cores'][0]['land_success']),
                                'image1':dic1['links']['mission_patch']})
            
        

        context = {'element':element,'status_code':response.status_code}
        return render(request,'index.html',context)
        
    except Exception as e:
        context = {'element':element,'status_code':404}
        return render(request,'index.html',context)
    

