from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post

class CategoryListView(ListView):
    model = Post

    def get_queryset(self):
        self.category = get_object_or_404(Category, category=self.kwargs['category'])
        return Post.objects.filter(category=self.category)

class PostDetailView(DetailView):
    model = Post

    template_name = 'blog/detail.html'




# def home(request):
#     posts = Post.objects.all()
#     cats = set()
#     for p in posts:
#         cats.add(p.category)
#     tabs = list(cats)
#     return render(request, 'blog/home.html', { 'posts': posts,
#                                           })






# def post_detail(request, post)
#     post = get_object_or_404(Post)
#     return render(request, 'blog/post/detail.html', {'post':post})



def model_form_upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/model_form_upload.html', {
        'form': form
    })
