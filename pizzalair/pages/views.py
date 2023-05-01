from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Pizza Lair!')

def about(request):
    template = loader.get_template("page.html")
    context = {
        "page_title": "About Pizza Lair",
        "page_content": """
<p>Welcome to Pizza Lair, where every slice is a saucy masterpiece! Established in 1568, we have been serving up delicious pizzas for over four centuries. Our founder was born in a lair, and his love of pizza and passion for saucy goodness inspired him to start this company.</p>

<p>At Pizza Lair, we believe that the key to a great pizza is in the sauce. That's why we take extra care to ensure that every pizza is expertly sauced for maximum flavor impact. Whether you prefer classic marinara, spicy buffalo, or creamy Alfredo, we've got a sauce that will tantalize your taste buds and leave you wanting more.</p>

<p>We also believe in using only the freshest ingredients in our pizzas. From our hand-tossed crusts to our premium toppings, we use only the best quality ingredients to create pizzas that are as delicious as they are memorable.</p>

<p>At Pizza Lair, we are proud of our rich history and our commitment to quality. We continue to honor our founder's legacy by creating pizzas that truly whip the sauce's ass. So whether you're a longtime fan or a first-time customer, we invite you to experience the saucy side of pizza at Pizza Lair.</p>
        """
    }
    return HttpResponse(template.render(context, request))
