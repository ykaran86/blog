from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
def post_list(request):
<<<<<<< HEAD
    posts = Post.objects.all()
    return render(request,'blog/post_list.html', {'posts':posts})
=======
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

>>>>>>> c29e393c3d53b53ca7a23959d9320710cc47c3ff
