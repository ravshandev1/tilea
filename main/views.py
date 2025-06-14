from django.shortcuts import render
from requests import post
from .models import Client, Gallery, Product, Project, Why, Feature, Main, About, Carousel, Phone

BOT_TOKEN = '7419830226:AAGIyVjLFm8AA_eo6D25Bf9ht7CD6iiw5pk'
CHAT_ID = '-1002164984527'


def send_telegram_message(name, phone, tour_name=None):
    text = f"📥 Yangi so'rov:\n👤 Ism: {name}\n📞 Telefon: {phone}"
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    try:
        response = post(url, data=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Telegram xabari yuborishda xatolik: {e}")


def index(request):
    main = Main.objects.first()
    about = About.objects.first()
    clients = Client.objects.all()
    galleries = Gallery.objects.all()
    projects = Project.objects.all()
    carousels = Carousel.objects.all()
    features = Feature.objects.all()
    whys = Why.objects.all()
    products = Product.objects.all().prefetch_related('images')
    phones = Phone.objects.all()
    return render(request, 'index.html',
                  {'main': main, 'about': about, 'clients': clients, 'galleries': galleries, 'projects': projects,
                   'features': features, 'whys': whys, 'products': products, 'carousels': carousels, 'phones': phones})


def product_inner(request, pk):
    product = Product.objects.filter(id=pk).prefetch_related('images').first()
    main = Main.objects.first()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        send_telegram_message(name, phone)
    return render(request, 'product-inner.html', {'product': product, 'main': main})
