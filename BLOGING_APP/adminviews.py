from django.shortcuts import render, redirect

from BLOGING_APP.models import Blogger, BlogPost



def bloggers_list(request):
    data = Blogger.objects.all()
    return render(request,"admin/bloggers_list.html",{"data":data})


def blogpost_lists(request):
    data=BlogPost.objects.all()
    return render(request, "admin/blogpost_lists.html", {"data":data})

def bloggers_delete(request,id):
    data =Blogger.objects.get(id=id)
    data.delete()
    return redirect('bloggers_list')
