{"filter":false,"title":"views.py","tooltip":"/accounts/views.py","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":2,"column":25},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":3,"column":0},"end":{"row":45,"column":48},"action":"insert","lines":["def login(request):","    \"\"\"Return a login page\"\"\"","    if request.method==\"POST\":","        login_form = UserLoginForm(request.POST)","        ","        if login_form.is_valid():","            user = auth.authenticate(username=request.POST['username'],","                                    password=request.POST['password'])","                                    ","            ","            if user:","                auth.login(user=user, request=request)","                return redirect(\"user_homepage\")","            ","            else:","                login_form.add_error(None, \"Your username or password is incorrect\")","    else:","        login_form = UserLoginForm()","    return render(request, \"login.html\", {\"login_form\": login_form})","","def registration(request):","    \"\"\"Render the registration page\"\"\"","    if request.user.is_authenticated:","        return redirect(reverse('index'))","    ","    if request.method == \"POST\":","        registration_form = UserRegistrationForm(request.POST)","        ","        if registration_form.is_valid():","            registration_form.save()","            ","            user = auth.authenticate(username=request.POST['username'],","                                    password=request.POST['password1'])","            if user:","                auth.login(user=user, request=request)","                messages.success(request, \"You have successfully registered!\")","                return redirect(reverse('index'))","            else:","                messages.error(request, \"Unable to register your account at this time\")","    else:","        registration_form = UserRegistrationForm()","    return render(request, 'registration.html', {","        \"registration_form\": registration_form})"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":35},"action":"remove","lines":["from django.shortcuts import render"],"id":4},{"start":{"row":0,"column":0},"end":{"row":2,"column":62},"action":"insert","lines":["from django.shortcuts import render, redirect, reverse","from django.contrib import auth, messages","from homepage.forms import UserLoginForm, UserRegistrationForm"]}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"remove","lines":["e"],"id":5},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"remove","lines":["g"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["a"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["p"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["e"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"remove","lines":["m"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":["o"]},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"remove","lines":["h"]}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["a"],"id":6},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["c"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["c"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["o"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["u"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["n"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["t"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":23,"column":28},"end":{"row":23,"column":29},"action":"insert","lines":["a"],"id":7},{"start":{"row":23,"column":29},"end":{"row":23,"column":30},"action":"insert","lines":["c"]},{"start":{"row":23,"column":30},"end":{"row":23,"column":31},"action":"insert","lines":["c"]},{"start":{"row":23,"column":31},"end":{"row":23,"column":32},"action":"insert","lines":["o"]}],[{"start":{"row":23,"column":28},"end":{"row":23,"column":32},"action":"remove","lines":["acco"],"id":8},{"start":{"row":23,"column":28},"end":{"row":23,"column":36},"action":"insert","lines":["accounts"]}],[{"start":{"row":23,"column":36},"end":{"row":23,"column":37},"action":"insert","lines":["/"],"id":9}],[{"start":{"row":46,"column":28},"end":{"row":46,"column":29},"action":"insert","lines":["a"],"id":10},{"start":{"row":46,"column":29},"end":{"row":46,"column":30},"action":"insert","lines":["c"]},{"start":{"row":46,"column":30},"end":{"row":46,"column":31},"action":"insert","lines":["c"]},{"start":{"row":46,"column":31},"end":{"row":46,"column":32},"action":"insert","lines":["o"]},{"start":{"row":46,"column":32},"end":{"row":46,"column":33},"action":"insert","lines":["u"]},{"start":{"row":46,"column":33},"end":{"row":46,"column":34},"action":"insert","lines":["n"]},{"start":{"row":46,"column":34},"end":{"row":46,"column":35},"action":"insert","lines":["s"]},{"start":{"row":46,"column":35},"end":{"row":46,"column":36},"action":"insert","lines":["/"]}],[{"start":{"row":46,"column":35},"end":{"row":46,"column":36},"action":"remove","lines":["/"],"id":11},{"start":{"row":46,"column":34},"end":{"row":46,"column":35},"action":"remove","lines":["s"]}],[{"start":{"row":46,"column":34},"end":{"row":46,"column":35},"action":"insert","lines":["t"],"id":12},{"start":{"row":46,"column":35},"end":{"row":46,"column":36},"action":"insert","lines":["s"]},{"start":{"row":46,"column":36},"end":{"row":46,"column":37},"action":"insert","lines":["/"]}]]},"ace":{"folds":[],"scrolltop":404.79998779296875,"scrollleft":0,"selection":{"start":{"row":46,"column":37},"end":{"row":46,"column":37},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":22,"state":"start","mode":"ace/mode/python"}},"timestamp":1583670191698,"hash":"9f4be4a3710351865b4436216877d1e201f2a5f6"}