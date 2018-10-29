from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
# 	{
# 		'user': 'Arpit',
# 		'category': 'Security',
# 		'requirement': 'I am in need of 10 security guards.',
# 		'date_posted': '10 Jan 2018'
# 	},
# 	{
# 		'user': 'Arpit. ddd',
# 		'category': 'Securityd',
# 		'requirement': '10',
# 		'date_posted': '10 Jan 2018'
# 	},
# ]

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'post/home.html', context)

def about(request):
	return render(request, 'post/about.html')
# Create your views here.
