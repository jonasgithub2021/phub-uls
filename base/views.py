from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
rooms = [
    
        {'id': 1, 'name':'jonas '},
        {'id': 2, 'name':'tine '},
        {'id': 3, 'name':'jojo '},
             
]
def home(request):
    # return HttpResponse("hello Django")
    content = {'rooms':rooms}
    return render(request, 'base/home.html',content)
def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    content = {'room':room}
    # return HttpResponse("welcome to the room")
    return render(request, 'base/room.html',content)