from django.shortcuts import render, redirect
from .models import Post,  Review
from django.http import HttpResponse, HttpRequest


def home(request:HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')[0:3]
    return render(request, 'app_main/home.html', {'posts': posts})

def add_post(request:HttpRequest):
    if request.method == 'POST':

        new_post = Post(title = request.POST.get('title'), content = request.POST.get('content'), published_at = request.POST.get('published_at'), is_published = request.POST.get('is_published') == 'on',image=request.FILES["image"])
        new_post.save()

        # new_post = post(title=request.POST["title"], description=request.POST["description"], publisher=request.POST["publisher"], rating=request.POST["rating"], release_date=request.POST["release_date"], poster=request.FILES["poster"])
        # new_post.save()

        #return redirect('app_main:home_view')
    
        return redirect('app_main:home')
    return render(request, 'app_main/add_post.html')

def details(request:HttpRequest, post_id:int):

    post = Post.objects.get(id=post_id)
    reviews = Review.objects.filter(post=post)


    return render(request, 'app_main/detail.html', {'post': post, "reviews":reviews})


def update(request:HttpRequest, post_id):
    
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        title=request.POST["title"] 
        content=request.POST["content"]
        is_published=request.POST.get('is_published') == 'on'  
        published_at=request.POST["published_at"]

        if "image" in request.FILES("image"): post.image = request.FILES("image")
        
        post.save()
      

    return render(request,'app_main/post.update.html', {'post': post})

def delete(request:HttpRequest, post_id):
    
    post = Post.objects.get(id=post_id)
    post.delete()
      

    return render(request,'app_main/home.html', {'post': post})

def review(request:HttpRequest, post_id):
    if request.method == "POST":
        post_object= Post.objects.get(pk=post_id)
        new_review= Review(post=post_object, name = request.POST['name'], rating = request.POST['rating'], comment = request.POST['comment'])
        new_review.save()
    return redirect("app_main:details", post_id=post_id) 