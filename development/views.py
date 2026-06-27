import datetime
from django.shortcuts import render
from .models import (
    CustomerSignup, OrderEvCharging, ContactTable,
    FeedbackTable, CustomerComplaint, CustomerOrderFuel, CompanyLogin
)


# ─── Public Pages ───────────────────────────────────────────────────────────

def homefun(request):
    return render(request, "index.html")

def aboutfun(request):
    return render(request, "about.html")

def servicesfun(request):
    return render(request, "services.html")

def contactfun(request):
    return render(request, "contact.html")

def signupfun(request):
    return render(request, "signup.html")

def loginfun(request):
    return render(request, "login.html")


# ─── Customer Auth ───────────────────────────────────────────────────────────

def customerdashboardfun(request):
    return render(request, "customerdashboard.html")

def signupdbcode(request):
    CustomerSignup.objects.create(
        id=request.POST['uid'],
        password=request.POST['password'],
        fullname=request.POST['fullname'],
        address=request.POST['address'],
        city=request.POST['city'],
        contact=request.POST['contact'],
        gender=request.POST['gender'],
        dob=request.POST['dob'],
        emailid=request.POST['mail'],
    )
    return render(request, "signup.html", {'signup_message': "Account Created Successfully"})

def logindbcode(request):
    userid = request.POST['uid']
    pwd = request.POST['password']
    user = CustomerSignup.objects.filter(id=userid, password=pwd).first()
    if user:
        return render(request, "customerdashboard.html")
    else:
        return render(request, "login.html", {'error_msg': "Invalid Id/Password"})


# ─── Contact ─────────────────────────────────────────────────────────────────

def contactdbcode(request):
    ContactTable.objects.create(
        fullname=request.POST['fnm1'],
        city=request.POST['city1'],
        contact=request.POST['contact1'],
        query=request.POST['query1'],
    )
    return render(request, "contact.html", {'contact_msg': "Query Successfully Sent"})


# ─── Customer Settings ───────────────────────────────────────────────────────

def settingsfun(request):
    return render(request, "settings.html")

def settingsdbcode(request):
    uid = request.POST['id']
    oldpass = request.POST['opwd']
    newpass = request.POST['npwd']
    cnewpass = request.POST['cnpwd']
    user = CustomerSignup.objects.filter(id=uid, password=oldpass).first()
    if user:
        if newpass == cnewpass:
            user.password = newpass
            user.save()
            return render(request, "login.html")
        else:
            return render(request, "settings.html", {'error_msg': "Password doesn't match"})
    else:
        return render(request, "settings.html", {'error_msg': "Invalid id/old password"})


# ─── Customer Accounts (Delete) ──────────────────────────────────────────────

def accountsfun(request):
    return render(request, "accounts.html")

def accountsdbcode(request):
    uid = request.POST['id']
    pwd = request.POST['password']
    user = CustomerSignup.objects.filter(id=uid, password=pwd).first()
    if user:
        user.delete()
        return render(request, "index.html")
    else:
        return render(request, "accounts.html", {'error_msg': "Invalid id/password"})


# ─── Feedback ────────────────────────────────────────────────────────────────

def feedbackfun(request):
    return render(request, "feedback.html")

def feedbackdbcode(request):
    FeedbackTable.objects.update_or_create(
        customerid=request.POST['id'],
        defaults={'feedback': request.POST['feedback']}
    )
    return render(request, "feedback.html", {'feedback_msg': "Thanks for your Feedback!!!"})


# ─── Complaints ──────────────────────────────────────────────────────────────

def complainfun(request):
    return render(request, "complain.html")

def complaindbcode(request):
    CustomerComplaint.objects.create(
        customerid=request.POST['customerid'],
        orderid=request.POST.get('orderid') or None,
        complain=request.POST['complain'],
        dateofcomplain=str(datetime.datetime.now()),
        complainstatus="under process",
    )
    return render(request, "complain.html", {'complain_msg': "Complain Sent Successfully!!!"})


# ─── Orders ──────────────────────────────────────────────────────────────────

def orderfun(request):
    return render(request, "order.html")

def orderevfun(request):
    return render(request, "orderev.html")

def orderevdbcode(request):
    OrderEvCharging.objects.create(
        customerid=request.POST['customerid'],
        droplocation=request.POST['droplocation'],
        contact=request.POST['contact'],
    )
    return render(request, "orderev.html", {'order_msg': "Your Order Is Placed Successfully!!!"})

def orderfuelfun(request):
    return render(request, "orderfuel.html")

def orderfueldbcode(request):
    CustomerOrderFuel.objects.create(
        customer_id=request.POST['customerid'],
        fuelcategory=request.POST['fuelcategory'],
        fueltype=request.POST['fueltype'],
        quantity=request.POST['quantity'],
        droplocation=request.POST['droplocation'],
        contact=request.POST['contact'],
    )
    return render(request, "orderfuel.html", {'order_msg': "Your Order Is Placed Successfully!!!"})


# ─── Company ─────────────────────────────────────────────────────────────────

def companyfun(request):
    return render(request, "company.html")

def companylogindbcode(request):
    userid = request.POST['uid']
    pwd = request.POST['password']
    company = CompanyLogin.objects.filter(id=userid, password=pwd).first()
    if company:
        return render(request, "companydashboard.html")
    else:
        return render(request, "company.html", {'error_msg': "Invalid Id/Password"})

def companydashboardfun(request):
    return render(request, "companydashboard.html")

def companysettingsfun(request):
    return render(request, "companysettings.html")

def companysettingsdbcode(request):
    uid = request.POST['id']
    oldpass = request.POST['opwd']
    newpass = request.POST['npwd']
    cnewpass = request.POST['cnpwd']
    company = CompanyLogin.objects.filter(id=uid, password=oldpass).first()
    if company:
        if newpass == cnewpass:
            company.password = newpass
            company.save()
            return render(request, "company.html")
        else:
            return render(request, "companysettings.html", {'error_msg': "Password doesn't match"})
    else:
        return render(request, "companysettings.html", {'error_msg': "Invalid id/old password"})


# ─── Company Data Views ───────────────────────────────────────────────────────

def loadcomplainfun(request):
    return render(request, "companycomplain.html")

def companycomplaindbcode(request):
    data = list(CustomerComplaint.objects.values_list())
    return render(request, "companycomplain.html", {'data': data})

def loadorderfuelfun(request):
    return render(request, "companyorderfuel.html")

def companyorderfueldbcode(request):
    data = list(CustomerOrderFuel.objects.values_list())
    return render(request, "companyorderfuel.html", {'data': data})

def loadorderevfun(request):
    return render(request, "companyorderev.html")

def companyorderevdbcode(request):
    data = list(OrderEvCharging.objects.values_list())
    return render(request, "companyorderev.html", {'data': data})

def companyfeedbackfun(request):
    return render(request, "companyfeedback.html")

def companyfeedbackdbcode(request):
    data = list(FeedbackTable.objects.values_list())
    return render(request, "companyfeedback.html", {'data': data})

def companycustomersfun(request):
    return render(request, "companycustomers.html")

def companycustomersdbcode(request):
    data = list(CustomerSignup.objects.values_list())
    return render(request, "companycustomers.html", {'data': data})

def companycontactfun(request):
    return render(request, "companycontact.html")

def companycontactdbcode(request):
    data = list(ContactTable.objects.values_list())
    return render(request, "companycontact.html", {'data': data})
