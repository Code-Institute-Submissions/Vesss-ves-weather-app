# The Weather App

#### **[Live demo](https://ves-weather-app.herokuapp.com/)**

### Requirements:
 - `python v3.6+`
 - `django v1.11`
 - `bootstrap v4.3.1`
 -  [Open Weather API](https://openweathermap.org/api)

### Install:
 1. Install/Setup database
 2. Copy `.env.example` to `.env`
 3. Update required variable changes to `.env`
 4. Install `virtualenv`: `virtualenv -p python3 <env folder name>`
 5. Activate: `source  <env folder name>/bin/activate`
 6. Install packages: `pip install -r requirements.txt`
 7. Runserver: `python manage.py runserver`


### Description
The Weather App is a web-based application which shows the weather in real time.

The user may type in the name of a city and they will then get a result of the current weather.

The site has been created with Django 1.11.xx, as well as with HTML, CSS, Bootstrap 4 and the Open Weather API.

The backend is Python, since Django is a Python-based framework.

It uses Postgresql to store data.

**The project is split into eight apps - 'Accounts', 'Cart', 'Donations', 'Orders', 'Products', & 'User templates'' .**

## Features

- Users may register, login, logout, buy T-shirts (or a jacket), or make a donation
- Users get informed that they are in their personal profile at the top left corner of the dashboard.
![Profile screenshot](https://i.ibb.co/k84nwYQ/menu.png)

## Design

The website has been designed with CSS and Bootstrap 4.

Bootstrap's role has been mostly in styling.

Most of the colouring has been created via pure CSS.

The clouds/mountains image on the index page (login/registration page) has been taken from unsplash.com.

## UX

The Weather App has a very untuitive nature.

When the user goes to the home page, he is met with a title and two buttons - Login and Register. Those are accompanied with a beautiful, clean background of white clouds and white mountain tops.
![Weather App](https://i.ibb.co/TH56ft8/Login-page.png)


Inspiration for this type of design has been drawn from the likes of Apple and Tesla, where there is little text and beautiful, high-quality background images.
![Tesla](https://i.ibb.co/SdGyv7X/tesla.jpg)

The website is mobile-friendly. The navigation menu collapses on smaller devices and has a toggler menu icon (a.k.a burger button), which expands the menu items on click.

![navigation](https://i.ibb.co/QcDhj46/dropdown-menu.png)

The main feature of the web-based application is the weather search tool. The user types in the name of a city/town and once he clicks on the search button / enter key (submit button) he gets the current weather of that city.
![Weather example](https://i.ibb.co/TrJ4F0F/weather-function.png)

As demonstrated in the screenshot above, the app functionality does more than simply show the current temperature - it also shows whether it's currently cloudy, sunny, raining, etc; it shows the minimum and maximum temperature; it shows the speed of the wind; it shows the atmospheric pressure (hPa); it shows the humidity.

It is very important to note that the Weather App is showing the current weather for the city the user has searched for. If the user would like to get a new update, they would have to search for the city again (similar to refreshing the page).

## Products and Cart
The products page is titled 'Get a T-shirt' and contains 3 items:
![Products](https://i.ibb.co/6BncDmS/get-a-t-shirt.png)

When the user clicks on an item, he gets to see it on a separate item details page:

![Product](https://i.ibb.co/QYgW0Sn/jacket.png)

If the user chooses to add the item to the cart, he gets redirected to the cart page, where it shows him how many items he has. One of the options on the cart page, once there is at least one item, is for the user to remove the item, as demonstrated below:
![Cart with product](https://i.ibb.co/BLvq3hn/cart-with-item.png)

Once the user has decided he has all the products they wish to buy, they can then click on 'Checkout' in the cart.
They then need to input their shipping address and billing address, on separate pages:
![Shipping address](https://i.ibb.co/TRrW9Xz/shipping-address.png)
![Billing address](https://i.ibb.co/xmS0K0d/Billing-address.png)

Following the insertion of shipping and billing addresses, the user is redirected to the Finalise Checkout page, where they are shown their items, their addresses, the cart total, the cost of the shipping, and a combined total price (items + shipping).
![Finalise order](https://i.ibb.co/qsVG7Tj/Finalise-Checkout.png)

When the user clicks on 'Pay the money', they then get redirected to the Stripe payment page. It is set to work with the development input, meanning the user needs to type in '4242 4242...'.
![Stripe](https://i.ibb.co/GVGmDYC/Stripe.png)

Once that's completed and the payment is accepted, the user gets redirected to a 'Thank you for your order page.'
![Thank you for your order](https://i.ibb.co/cXbp0SV/Thank-you-for-your-order.png)


## Back-end technology
The main feature of the application is the live weather search tool, which is built using the Open Weather API.
This is the code that handles it:

```
def user_homepage(request, name="userhomepage"):
    user = User.objects.get(email=request.user.email)
    profile = {'user' : user}
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=38e4fec38e509c018629074ac1754906'
    
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city_name"]
            r = requests.get(url.format(city)).json()
            city_weather = {
                'city': city,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' :  r['weather'][0]['icon'],
            }
            result = {'city_weather' : city_weather, 'Form': form}
            
    else:
        form = Form()
        city = "London"
        r = requests.get(url.format(city)).json()
        city_weather = {
                'city': city,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' :  r['weather'][0]['icon'],
            }
        result = {'city_weather' : city_weather, 'Form': form}
        
    
    return render(request, 'userhomepage.html', result, profile)
```

## Deployment
The application has been uploaded to both GitHub and Heroku. It is being hosted on Heroku.

## Contributions
Contributions need to be given to Unsplash.com, The Open Weather API.







