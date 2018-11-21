from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Review
from advert.models import Advert
from .forms import PostCreateForm, PostUpdateForm, ReviewForm
from django.contrib.auth.decorators import login_required

# def home(request):
# 	context = {
# 		'posts': Post.objects.all()
# 	}
# 	return render(request, 'post/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'post/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5
	
	def get_queryset(self):
		order_by = self.kwargs.get('order_by') or '-date_posted'
		return Post.objects.order_by(order_by)
# class PostListViewSorted(ListView):
# 	model = Post
# 	template_name = 'post/home.html'
# 	context_object_name = 'posts'
# 	ordering = ['-date_posted']

# 	# def get_queryset(self):
	# 	order_by = self.request.GET.get('order_by') or '-date_posted'
	# 	return Post.objects.order_by(order_by)
			

class UserPostListView(ListView):
	model = Post
	template_name = 'post/user_posts.html'
	context_object_name = 'posts'
	# paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username= self.kwargs.get('username'))
		return Post.objects.filter(author= user).order_by('-date_posted')

class UserDashboard(ListView):
	model = Post
	template_name = 'post/user_dashboard.html'
	context_object_name = 'posts'
	# paginate_by = 7

	def get_queryset(self):
		user = get_object_or_404(User, username= self.kwargs.get('username'))
		return Post.objects.filter(author= user).order_by('-date_posted')

class UserDashboardAds(ListView):
	model = Advert
	template_name = 'post/user_dashboardads.html'
	context_object_name = 'adverts'
	# paginate_by = 7

	def get_queryset(self):
		user = get_object_or_404(User, username= self.kwargs.get('username'))
		return Advert.objects.filter(author= user).order_by('-date_posted')

@login_required
def PostDetailView(request,pk):
	post = get_object_or_404(Post, pk = pk)
	if request.method == "POST":
		form = ReviewForm(request.POST, request.FILES)
		if form.is_valid():
			document = form.cleaned_data['document'] 
			comment = form.cleaned_data['comment']
			user_name = request.user.username
			review = Review()
			review.post = post
			review.user_name = user_name
			# review.author = request.user
			review.comment = comment
			review.document = document
			review.save()
	form=ReviewForm()
	return render(request, 'post/post_detail.html', {'post': post, 'form': form})
	# if request.method == "POST":
	# 	form = ReviewForm(request.POST, instance= Review.objects.get(id=pk))
	# 	if form.is_valid():
	# 		form.instance.user_name = request.user
	# 		form.save()
	# else:
	# 	form = ReviewForm(instance= Review.objects.get(id=pk))
	# return render(request, 'post/post_detail.html', {'post': post, 'form': form})


# class PostDetailView(DetailView):
# 	model = Post
# 	context_object_name = 'post' 

class PaymentView(DetailView):
	model = Post
	context_object_name = 'post' 

@login_required
def post_create(request):
	if request.method == "POST":
		form = PostCreateForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			return redirect('post-home')
	else:
		form = PostCreateForm()
	return render(request, 'post/post_form.html', {'form': form})

@login_required
def post_update(request,pk):
	if request.method == "POST":
		form = PostUpdateForm(request.POST, request.FILES, instance= Post.objects.get(id=pk))
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			return redirect('post-home')
	else:
		form = PostUpdateForm(instance= Post.objects.get(id=pk))
	return render(request, 'post/post_form.html', {'form': form})
	# def form_valid(self, form):
	# 	form.instance.author = self.request.user
	# 	return super().form_valid(form)
# class PostCreateView(LoginRequiredMixin, PostCreateForm):
# 	model = Post
# 	fields = ['item','category', 'quantity','description'] 

# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
# 	model = Post
# 	fields = ['category', 'item', 'description'] 

# 	def form_valid(self, form):
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)

# 	def test_func(self):
# 		post = self.get_object()
# 		if self.request.user == post.author:
# 			return True
# 		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	context_object_name = 'post' 
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'post/about.html')

def welcome(request):
	return render(request, 'post/welcome.html')
# Create your views here.
 