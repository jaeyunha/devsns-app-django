from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    # posts = Post.objects.filter().order_by('date')
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    # request method가 POST일 경우
        # 입력값 저장
    if request.method == 'POST' or request.method == 'FILES':
        PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    # request method가 GET일 경우
        # from 입력 html 띄우기
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post_detial':post_detail})