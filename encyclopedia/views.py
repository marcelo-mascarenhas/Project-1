from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import markdown2
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, html):
   
    link = util.get_entry(html)

    if link == None:
        return render(request, "encyclopedia/entries.html", {
            "body": "<h1>Page not found</h1> <div> Please, enter a valid address.</div>", "title": "Page Not Found"
        })

    return render(request, "encyclopedia/entries.html", {
        "body": markdown2.markdown(link), "title": html
    })



def random_page(request):
    entry_list = util.list_entries()
    
    list_item = random.randint(0, len(entry_list)-1)
    
    file_name = entry_list[list_item]
    return redirect('entries', html=file_name)


def search(request):
    #To check if it was really sent#
    if request.method == "POST":

        name = request.POST['q']
        
        if util.get_entry(name) != None:
            return redirect('entries', html = name)
        else:  
            list_of_entries = list()
            for entry in util.list_entries():
                if name.upper() in entry.upper():
                    list_of_entries.append(entry)
            return render(request, "encyclopedia/search.html",
            { "suggestions": list_of_entries
            })

def create(request):
    return render(request, "encyclopedia/create_new_page.html")

def create_page(request):
    if request.method == "POST":
        title = request.POST['title']
        if util.get_entry(title) != None:
            return HttpResponse("<h1>This page already exists. Please, enter a title that doesn't exists yet.</h1>")
        elif title == "":
            return HttpResponse('<h1>Please, enter a valid title.</h1>')
        else:
            body = request.POST['body']
            util.save_entry(title, body)
            return redirect('entries', html=title)
            
            

def edt(request, name):
    if request.method == "POST":
        body = util.get_entry(name)
        return render(request, "encyclopedia/edit_page.html", {
            'title': name, 'body':body
        })

def confirm_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        util.save_entry(title, body)
        return redirect('entries', html=title)


