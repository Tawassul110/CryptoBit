from django.shortcuts import render
from .models import Coin
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags

# Create your views here.
def get_coins():
    
    coins = Coin.objects.all()
    return coins

def get_featured_coins():
    featured_coins = Coin.objects.all()[:3]
    return featured_coins

def coinDetail(request,coin_id):
    coin = Coin.objects.get(id = coin_id)  
    coindata = {
        'coin' : coin
     }   
    return render(request,'pages/details.html', coindata)

def buy(request,coinId):
    coinn = Coin.objects.get(id = coinId)
    coinD = {
        'coinn' : coinn
    }

    return render(request,'pages/express.html', coinD)

def transaction(request,coinid):
    coin = Coin.objects.get(id = coinid)
    # price = Coin.price

   
    print(request.POST)
    quantity = request.POST.get('quantity')
    email = request.POST.get('userEmail')
    accno = request.POST.get('userAccno')
    fname = request.POST.get('firstName')
    lname = request.POST.get('lastName')

    # save.quantity = quantity
    # save.email = email
    # save.acc_no = accno
    # save.name = name

    # save.save()
    receipt = {
        'Coin' : coin,
        'quantity' : quantity,
        'fname' : fname,
        'lname' : lname,
        'email' : email ,
        'accno' : accno

        # 'total' : 'quantity' * price
    }

    email_template_html = render_to_string('emails/receipt.html', receipt)
    email_template_txt = strip_tags(email_template_html)

    subject = 'Transaction Successful | cryptobit'
    from_email = 'subscribe@cryptobit.com'
    to_email = ['tawassul02@gmail.com']
    send_mail(
        subject=subject,
        from_email=from_email, 
        recipient_list = to_email, 
        html_message=email_template_html, 
        message=email_template_txt
        )

    print(accno)
    print(receipt)
    return render(request,'buy/receipt.html', receipt)
