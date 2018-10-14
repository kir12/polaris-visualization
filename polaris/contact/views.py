from django.shortcuts import render
from django.http import HttpResponse
from contact.forms import ContactForm
from django.utils.timezone import now
from django.shortcuts import redirect
def index(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.timestamp = now()
			post.save()
			return redirect('contact:success')
	form = ContactForm()
	return render(request,'contact/Contact.html',{'form':form})
def success(request):
	return render(request,'contact/success.html',{})

# Create your views here.
