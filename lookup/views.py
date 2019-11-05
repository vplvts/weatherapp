from django.shortcuts import render

# Create your views here.
def home(request):
    
    import requests
    import json
    if request.method =="POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=10&API_KEY=AC1D2ECD-1F47-418D-883D-B75CE553BB45")
        
        try:
            api = json.loads(api_request.content)
        except Exception as e :
            api = "Error has occured."
        if api[0]['Category']['Name'] == "Good":
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_color = "hazardous"
        return render(request,'home.html',{'api':api,'category_color':category_color})
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=88901&distance=10&API_KEY=AC1D2ECD-1F47-418D-883D-B75CE553BB45")
        
        try:
            api = json.loads(api_request.content)
        except Exception as e :
            api = "Error has occured."
        if api[0]['Category']['Name'] == "Good":
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_color = "hazardous"
        return render(request,'home.html',{'api':api,'category_color':category_color})

def about(request):
    return render(request,'about.html')