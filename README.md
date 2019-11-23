# The Weather App

**LINK to the active application:** https://ves-weather-app.herokuapp.com/

The Weather App is a web-based application which shows the weather in real time.

The user may type in the name of a city and they will then get a result of the current weather.

The site has been created with Django 1.11.xx, as well as with HTML, CSS, Bootstrap 4 and the Open Weather API.

The backend is Python, since Django is a Python-based framework.

It uses Postgresql to store data.

## Features

- Users may register, login, logout.
- Users get informed that they are in their personal profile at the top left corner of the dashboard.
![Profile screenshot](https://i.ibb.co/02twHW5/profile.jpg)
- The user has the option to submit a $5 donation via the donation button.

## Design

The website has been designed with CSS and Bootstrap 4.

Bootstrap's role has been mostly in styling.

Most of the colouring has been created via pure CSS.

The clouds/mountains image on the index page (login/registration page) has been taken from unsplash.com.

## UX

The Weather App has a very untuitive nature.

When the user goes to the home page, he is met with a title and two buttons - Login and Register. Those are accompanied with a beautiful, clean background of white clouds and white mountain tops.
![Weather App](https://i.ibb.co/Hrn9dVL/weather-app.jpg)


Inspiration for this type of design has been drawn from the likes of Apple and Tesla, where there is little text and beautiful, high-quality background images.
![Tesla](https://i.ibb.co/SdGyv7X/tesla.jpg)

The website is mobile-friendly. The navigation menu collapses on smaller devices and has a toggler menu icon (a.k.a burger button), which expands the menu items on click.
![Menu Item](https://i.ibb.co/k1Y7Z6C/mobile-first.jpg)

The main feature of the web-based application is the weather search tool. The user types in the name of a city/town and once he clicks on the search button / enter key (submit button) he gets the current weather of that city.
![Weather example](https://i.ibb.co/gPMLwMF/open-weather.jpg)

To further advance the user experience, the results also shows an icon of the current weahter on the top-left corner, alongside with the temperature and text-description of the weather.


## Language and Frameworks
- Django
- HTML5
- CSS3
- Bootstrap 4
- Font Awesome
- Open Weather API (https://openweathermap.org/api)


## Back-end technology
The main feature of the application is the live weather search tool, which is built using the Open Weather API.
This is the code that handles it:

`
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
`

## Deployment
The application has been uploaded to both GitHub and Heroku. It is being hosted on Heroku.

## Contributions
Contributions need to be given to Unsplash.com, The Open Weather API.







