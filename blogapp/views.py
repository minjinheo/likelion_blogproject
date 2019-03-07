from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost
# Create your views here.

def main(request):
    return render(request, 'main.html')
    
def home(request):
    blogs = Blog.objects #쿼리셋
    blog_list = Blog.objects.all() #블로그 모든 글 대상
    paginator = Paginator(blog_list, 3) #블로그 객체 3개를 한페이지로
    page = request.GET.get('page') #request된 페이지가 뭔지 알아냄/request 페이지를 page 변수에 담기
    posts = paginator.get_page(page)
    return render(request, 'home.html',{'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

#new.html을 띄워주는 함수
def new(request):
    return render(request, 'new.html')

#입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

#입력된 내용을 처리하는 기능 POST, 빈 페이지를 띄워주는 기능 GET
def blogpost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})