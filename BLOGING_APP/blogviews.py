import profile

from django.contrib.auth import logout
from django.shortcuts import redirect, render

from BLOGING_APP.forms import BloggerRegister, BlogPostRegister
from BLOGING_APP.models import Blogger, BlogPost


def blogger_edit(request):

    user=request.user
    blogger=Blogger.objects.get(blogger_detail=user)

    if request.method == "POST":
        blog_form = BloggerRegister(request.POST,request.FILES,instance=blogger)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('my_profile')
    else:
        blog_form = BloggerRegister(instance=blogger)
    return render(request,"blogger/blogger_edit.html",{"data":blog_form})



def blogpost_add(request):

    if request.method == "POST":
         post_form = BlogPostRegister(request.POST,request.FILES)
         if post_form.is_valid():
           post = post_form.save(commit=False)
           blogger = Blogger.objects.get(blogger_detail=request.user)
           post.blog_detail = blogger
           post.save()
         return redirect('my_profile')
    else:
        post_form = BlogPostRegister()
    return render(request, "blogger/blogpost_add.html", {"post_form":post_form})


def blogpost_list(request):
    blogger = Blogger.objects.get(blogger_detail=request.user)
    data=BlogPost.objects.filter(blog_detail=blogger)
    return render(request, "blogger/blogpost_list.html", {"data":data})


def blogpost_update(request, id):
    blog_up = BlogPost.objects.get(id=id)
    if request.method == "POST":
        up_form = BlogPostRegister(request.POST, request.FILES, instance=blog_up)
        if up_form.is_valid():
            up_form.save()

            return redirect('blogpost_list')

    else:
        up_form = BlogPostRegister(instance=blog_up)
    return render(request, 'blogger/blogpost_update.html', {'data': up_form})



def blogpost_delete(request,id):
    data =BlogPost.objects.get(id=id)
    data.delete()
    return redirect('blogpost_list')


def blogposts_lists(request):
    data=BlogPost.objects.all()
    return render(request, "blogger/blogposts_lists.html", {"data":data})


def Log_out(request):
    logout(request)
    return redirect('index')