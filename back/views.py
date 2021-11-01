from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template

from django.core.mail import EmailMessage

from back.models import Email, Image, Product, Size, Color

import json

# Create your views here.
def index(request):
    return render(request,'app/index.html')
    
def about(request):
    return render(request,'app/about.html')
    
def products(request):
    products = Product.objects.all()
    return render(request,'app/products.html',{'products': products})
    
def gallery(request):
    images = Image.objects.all()
    return render(request,'app/gallery.html',{'images': images})
    
def product(request,id):
    product = Product.objects.get(id=id)
    sizes = Size.objects.filter(of=product)
    colors = Color.objects.filter(of=product)
    return render(request,'app/product.html',{'product': product,'sizes': sizes,'colors': colors})
    
def contact(request):
    if request.method == 'GET':
        return render(request,'app/contact.html')
    if request.method == 'POST':
        data = json.loads(request.body)
        print("Data",data)
        template = get_template('email/thankyou.html')
        content = template.render({'name': data['name']})
        email = EmailMessage(
		'Thank you for contacting Us',
		content,
		'Pinnamaya Cycles <info@pinnamayacycles.com>',
		[data['email']],
		[],
		reply_to=[],
		headers={'Message-ID': 'pdf'},)
        email.content_subtype = "html"
        email.send()
        
        template2 = get_template('email/message.html')
        content2 = template2.render({'name': data['name'],'message': data['message'],'email': data['email']})
        email2 = EmailMessage(
		'New Message',
		content2,
		'Pinnamaya Cycles <info@pinnamayacycles.com>',
		['info@pinnamayacycles.com'],
		[],
		reply_to=[],
		headers={'Message-ID': 'pdf'},)
        email2.content_subtype = "html"
        email2.send()
        return JsonResponse({'error': False,'message': 'Successfully Done'})


    
def subscribe(request):
    data = json.loads(request.body)
    try:
        print(data['email'])
        new2 = Email.objects.get(email=data['email'])
        print('email exists')
        return JsonResponse({'error': True,'message': 'Email already subscribed'})   
    except:
        print('email not exists')
        new = Email(email=json.loads(request.body)['email'])
        new.save()
        # print("Data",data)
        template = get_template('email/subscribe.html')
        content = template.render({'email': data['email']})
        email = EmailMessage(
        'Thank you for subscribing',
        content,
        'Pinnamaya Cycles <info@pinnamayacycles.com>',
        [data['email']],
        [],
        reply_to=[],
        headers={'Message-ID': 'pdf'},)
        email.content_subtype = "html"
        email.send()
        
        return JsonResponse({'error': False,'message': 'Successfully Done'})   


def charcha_serviceworker(request, js):
      template = get_template('app/charcha-serviceworker.js')
      html = template.render()
      return HttpResponse(html, content_type="application/x-javascript")

      


# def manifest(request, js):
#       template = get_template('app/charcha-serviceworker.js')
#       html = template.render()
#       return HttpResponse(html, content_type="application/x-javascript")