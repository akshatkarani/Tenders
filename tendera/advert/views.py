from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Advert
from django.contrib.auth.decorators import login_required
from .forms import AdvertCreateForm, AdvertUpdateForm
# Create your views here.
class AdvertListView(ListView):
	model = Advert
	template_name = 'advert/home.html'
	context_object_name = 'adverts'
	ordering = ['-date_posted']
	paginate_by =5

	def get_queryset(self):
		order_by = self.kwargs.get('order_by') or '-date_posted'
		return Advert.objects.order_by(order_by)

class AdvertDetailView(DetailView):
	model = Advert
	context_object_name = 'advert' 

# class AdvertCreateView(LoginRequiredMixin, CreateView):
# 	model = Advert
# 	fields = ['image', 'details', 'address', 'products']

# 	def form_valid(self, form):
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)

# class AdvertUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
# 	model = Advert
# 	fields = ['image', 'details', 'address', 'products']

# 	def form_valid(self, form):
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)

# 	def test_func(self):
# 		advert = self.get_object()
# 		if self.request.user == advert.author:
# 			return True
# 		return False

@login_required
def advert_create(request):
	if request.method == "POST":
		form = AdvertCreateForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			return redirect('advert-home')
	else:
		form = AdvertCreateForm()
	return render(request, 'advert/advert_form.html', {'form': form})

@login_required
def advert_update(request,pk):
	if request.method == "POST":
		form = AdvertUpdateForm(request.POST, request.FILES, instance= Advert.objects.get(id=pk))
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			return redirect('advert-home')
	else:
		form = AdvertUpdateForm(instance= Advert.objects.get(id=pk))
	return render(request, 'advert/advert_form.html', {'form': form})

class AdvertDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Advert
	context_object_name = 'advert' 
	success_url = '/advert/'

	def test_func(self):
		advert = self.get_object()
		if self.request.user == advert.author:
			return True
		return False

def about(request):
	return render(request, 'advert/about.html')




	# image = models.ImageField(default= 'default_business.jpg', upload_to = 'business_pics')
	# details = models.TextField()
	
	# address = models.CharField(max_length=100)
	# products = models.ManyToManyField('Item')
	# date_posted = models.DateTimeField(auto_now_add= True)
	# author = models.ForeignKey(User, on_delete = models.CASCADE)
