from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Post, Comment, Message
from .forms import PostForm, CommentForm, MessageForm


# Create your views here.

def index(request):
    posts = Post.objects.filter(status=1).order_by('created_at')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/index.html', {'posts': page_obj})


def load_more_posts(request):
    page_number = request.GET.get('page')
    posts = Post.objects.filter(status=1).order_by('created_at')
    paginator = Paginator(posts, 3)
    page_obj = paginator.get_page(page_number)
    posts_html = render_to_string('main/posts_list.html', {'posts': page_obj})
    return JsonResponse({
        'posts_html': posts_html,
        'has_next': page_obj.has_next()
    })


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    message_sent = False
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if request.user.is_authenticated:
                message.sender = request.user
            else:
                messages.warning(request, "You need to be logged in to send a message.")
                return redirect('contact')

            message.save()
            message_sent = True
            messages.success(request, "Thank you for your message!")
            return redirect('contact')

    return render(request, 'main/contact.html', {'form': form, 'message_sent': message_sent})


def is_moderator(user):
    return user.groups.filter(name='Administrator').exists()


@login_required
@user_passes_test(is_moderator)
def moderator_panel(request):
    posts = Post.objects.filter(status=0).order_by('created_at')
    messages = Message.objects.all()
    return render(request, 'main/admin_panel/moderator_panel.html', {'posts': posts, 'messages': messages})


@login_required
@user_passes_test(is_moderator)
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return redirect('moderator_panel')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'main/registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'main/registration/register.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'main/posts/post_detail.html',
                  {'post': post, 'comments': comments, 'comment_form': comment_form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()

    return render(request, 'main/posts/create_post.html', {'form': form})


@login_required
@user_passes_test(is_moderator)
def change_status(request, post_id, status):
    post = get_object_or_404(Post, id=post_id)
    if status in [0, 1, 2]:
        post.status = status
        post.save()
    return redirect('moderator_panel')
