# Create your views here.
from django.shortcuts import render,render_to_response,HttpResponse,Http404,HttpResponseRedirect
from django.template import Context
from libdb.models import Book,Author


# Create your views here.
def home(request):
     if request.POST:
        c=search(request)
        return render_to_response("search.html",c)
     else:
        return render_to_response("home.html")


def search(request):
    if request.POST:
        q=request.POST["books"]
        bid=Author.objects.filter(Name=q)
        #print bid
        ge=Book.objects.filter(AuthorId=bid)
        c=Context({"list":ge})
        return c
    else:
        return HttpResponse("please submit a term")

def dele(req,offset):
    try:
        offset=int(offset)
        Book.objects.filter(ISBN=offset).delete()

    except:
        return HttpResponse("none")

    return render_to_response("delete.html",{"name":offset})

def detail(req,off):
    offset=int(off)
    print offset
    offob=Book.objects.filter(ISBN=off)
    print offob
    c=Context({"list":offob})
    print c
    return render_to_response("detail.html",{"list":offob})

def add(req):
    if req.POST:
        print req.POST
        Authorg=req.POST["AuthorId"]
        if not Authorg:
            print Authorg
            Aname=Author.objects.get(Name=Authorg)
            book=Book(ISBN=req.POST["ISBN"],Title=req.POST["Title"],AuthorId=Aname,publisher=req.POST["publisher"],Publishdata=req.POST["publishdate"],Price=req.POST["price"])
            book.save()
        else:
            newid=int(Author.objects.count())+1
            newAuthor=Author(AuthorId=newid,Name=req.POST["AuthorId"],Age=req.POST["age"],Country=req.POST["country"])
            newAuthor.save()
            book=Book(ISBN=req.POST["ISBN"],Title=req.POST["Title"],AuthorId=newAuthor,publisher=req.POST["publisher"],Publishdata=req.POST["publishdate"],Price=req.POST["price"])
            book.save()
        return HttpResponseRedirect("/home.html")
    else:
        return render_to_response("add.html")

def update(req,off):
    if req.POST:
        offset=int(off)

        Authorg=req.POST["AuthorId"]
        Aname=Author.objects.get(Name=Authorg)
        Book.objects.filter(ISBN=offset).update(ISBN=req.POST["ISBN"],Title=req.POST["Title"],AuthorId=Aname,publisher=req.POST["publisher"],Publishdata=req.POST["publishdate"],Price=req.POST["price"])
        return HttpResponseRedirect("/home.html")

    else:
        offset=int(off)
        g=Book.objects.filter(ISBN=offset)
        c=Context({"list":g})
        return render_to_response("update.html",c)
