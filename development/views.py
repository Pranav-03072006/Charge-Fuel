import sqlite3
from django.shortcuts import render
import datetime
# Create your views here.
def homefun(request):
    return render(request,"index.html")
def aboutfun(request):
    return render(request,"about.html")
def servicesfun(request):
    return render(request,"services.html")
def contactfun(request):
    return render(request,"contact.html")
def signupfun(request):
    return render(request,"signup.html")
def loginfun(request):
    return render(request,"login.html")

def customerdashboardfun(request):
    return render(request,"customerdashboard.html")
def signupdbcode(request):
    userid=request.POST['uid']
    password = request.POST['password']
    fullname=request.POST['fullname']
    address=request.POST['address']
    city=request.POST['city']
    contact=request.POST['contact']
    gender=request.POST['gender']
    dob=request.POST['dob']
    email=request.POST['mail']
    con=sqlite3.connect("db.sqlite3");
    operation=con.cursor()
    sql="insert into customersignup values(?,?,?,?,?,?,?,?,?)"
    values=(userid,password,fullname,address,city,contact,gender,dob,email)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "signup.html",{'signup_message':"Account Created Successfully"})

def logindbcode(request):
    userid=request.POST['uid']
    pwd=request.POST['password']
    con=sqlite3.connect('db.sqlite3')
    operation=con.cursor()
    sql="select * from customersignup where Id=? and Password=?"
    values=(userid,pwd)
    result=operation.execute(sql,values)
    if(result.fetchone()):
        return render(request, "customerdashboard.html")
    else:
        return render(request, "login.html", {'error_msg': "Invalid Id/Password"})

def contactdbcode(request):
    fnm=request.POST['fnm1']
    city=request.POST['city1']
    contact=request.POST['contact1']
    query=request.POST['query1']
    con = sqlite3.connect('db.sqlite3');
    operation = con.cursor()
    sql ="insert into contacttable values(?,?,?,?)"
    values =(fnm,city,contact,query)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "contact.html", {'contact_msg': "Query Successfully Sent"})

def settingsfun(request):
    return render(request,"settings.html")

def  settingsdbcode(request):
    uid=request.POST['id']
    oldpass = request.POST['opwd']
    newpass = request.POST['npwd']
    cnewpass = request.POST['cnpwd']
    con = sqlite3.connect("db.sqlite3")
    operation=con.cursor()
    sql="select *  from customersignup where Id=? and Password=?"
    values=(uid,oldpass)
    result=operation.execute(sql,values)
    if(result.fetchone()):
        if(newpass==cnewpass):
            sql1 = "update customersignup set Password=? where Id=?"
            values1=(newpass,uid)
            operation.execute(sql1,values1)
            con.commit()
            return render(request, "login.html")
        else:
            return render(request, "setting.html",{'error_msg': "password doesnt match"})
    else:
        return render(request, "setting.html", {'error_msg': "invalid id/old password"})

def accountsfun(request):
    return render(request,"accounts.html")
def accountsdbcode(request):
    uid = request.POST['id']
    password = request.POST['password']
    connect = sqlite3.connect("db.sqlite3")
    operation = connect.cursor()
    sql = "select *  from customersignup where Id=? and Password=?"
    values = (uid, password)
    result = operation.execute(sql, values)
    if (result.fetchone()):
        sql1 = "delete from customersignup where Id=? and Password=?"
        values1 = (uid, password)
        operation.execute(sql1, values1)
        connect.commit()
        return render(request, "index.html")
    else:
        return render(request, "accounts.html", {'error_msg': "invalid id/ password"})


def feedbackfun(request):
    return render(request,"feedback.html")

def feedbackdbcode(request):
    uid=request.POST['id']
    ufeedback=request.POST['feedback']
    con = sqlite3.connect('db.sqlite3');
    operation = con.cursor()
    sql ="insert into feedbacktable values(?,?)"
    values = (uid,ufeedback)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "feedback.html", {'feedback_msg': "Thanks for your Feedback!!!"})

def complainfun(request):
    return render(request,"complain.html")

def complaindbcode(request):
    customerid = request.POST['customerid']
    orderid=request.POST['orderid']
    complain = request.POST['complain']
    con = sqlite3.connect("db.sqlite3")
    operation = con.cursor()
    sql = "insert into customercomplaintable(customerid,orderid,dateofcomplain,complainstatus,complain) values(?,?,?,?,?)"
    values =(customerid,orderid,datetime.datetime.now(),"under process",complain)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request,"complain.html",{'complain_msg':"Complain Sent Successfully!!!"})

def orderfun(request):
    return render(request,"order.html")

def orderevfun(request):
    return render(request,"orderev.html")


def orderevdbcode(request):
    customerid = request.POST['customerid']
    droplocation = request.POST['droplocation']
    contact = request.POST['contact']
    con = sqlite3.connect("db.sqlite3")
    operation = con.cursor()
    sql = "insert into orderevchargingtable(customerid,droplocation,contact) values(?,?,?)"
    values =(customerid,droplocation,contact)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request,"orderev.html",{'order_msg':"Your Order Is Placed Successfully!!!"})

def orderfuelfun(request):
    return render(request,"orderfuel.html")


def orderfueldbcode(request):
    cid = request.POST['customerid']
    fcategory = request.POST['fuelcategory']
    ftype = request.POST['fueltype']
    quantity = request.POST['quantity']
    droplocation = request.POST['droplocation']
    contact = request.POST['contact']
    con = sqlite3.connect("db.sqlite3")
    operation = con.cursor()
    sql = "insert into customerorderfueltable(ID,Fuelcategory,fueltype,quantity,droplocation,contact) values(?,?,?,?,?,?)"
    values =(cid,fcategory,ftype,quantity,droplocation,contact)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request,"orderfuel.html",{'order_msg':"Your Order Is Placed Successfully!!!"})


def companyfun(request):
    return render(request,"company.html")

def companylogindbcode(request):
    userid=request.POST['uid']
    pwd=request.POST['password']
    con=sqlite3.connect('db.sqlite3');
    operation=con.cursor()
    sql="select * from companylogintable where ID=? and Password=?"
    values=(userid,pwd)
    result=operation.execute(sql,values)
    if(result.fetchone()):
        return render(request, "companydashboard.html")
    else:
        return render(request, "company.html", {'error_msg': "Invalid Id/Password"})


def companydashboardfun(request):
    return render(request,"companydashboard.html")

def companysettingsfun(request):
    return render(request,"companysettings.html")


def companysettingsdbcode(request):
    uid=request.POST['id']
    oldpass = request.POST['opwd']
    newpass = request.POST['npwd']
    cnewpass = request.POST['cnpwd']
    con = sqlite3.connect("db.sqlite3")
    operation=con.cursor()
    sql="select *  from companylogintable where Id=? and Password=?"
    values=(uid,oldpass)
    result=operation.execute(sql,values)
    if(result.fetchone()):
        if(newpass==cnewpass):
            sql1 = "update companylogintable set Password=? where Id=?"
            values1=(newpass,uid)
            operation.execute(sql1,values1)
            con.commit()
            return render(request, "company.html")
        else:
            return render(request, "companysettings.html",{'error_msg': "password doesnt match"})
    else:
        return render(request, "companysettings.html", {'error_msg': "invalid id/old password"})

def loadcomplainfun(request):
    return render(request,"companycomplain.html")

def  companycomplaindbcode(request):
    con = sqlite3.connect("db.sqlite3")
    operation=con.cursor()
    sql="select *  from customercomplaintable"
    result=operation.execute(sql)
    list=result.fetchall()
    return render(request, "companycomplain.html",{'data':list})

def loadorderfuelfun(request):
    return render(request,"companyorderfuel.html")

def  companyorderfueldbcode(request):
    con = sqlite3.connect("db.sqlite3")
    operation=con.cursor()
    sql="select *  from customerorderfueltable"
    result=operation.execute(sql)
    list=result.fetchall()
    return render(request, "companyorderfuel.html",{'data':list})

def loadorderevfun(request):
    return render(request,"companyorderev.html")

def  companyorderevdbcode(request):
    con = sqlite3.connect("db.sqlite3")
    operation=con.cursor()
    sql="select *  from orderevchargingtable"
    result=operation.execute(sql)
    list=result.fetchall()
    return render(request, "companyorderev.html",{'data':list})

def companyfeedbackfun(request):
    return render(request,"companyfeedback.html")

def  companyfeedbackdbcode(request):
    con = sqlite3.connect("db.sqlite3")
    operation=con.cursor()
    sql="select *  from feedbacktable"
    result=operation.execute(sql)
    list=result.fetchall()
    return render(request, "companyfeedback.html",{'data':list})


def companycustomersfun(request):
    return render(request,"companycustomers.html")

def  companycustomersdbcode(request):
    con = sqlite3.connect("db.sqlite3")
    operation=con.cursor()
    sql="select *  from customersignup"
    result=operation.execute(sql)
    list=result.fetchall()
    return render(request, "companycustomers.html",{'data':list})


def companycontactfun(request):
    return render(request,"companycontact.html")

def  companycontactdbcode(request):
    con = sqlite3.connect("db.sqlite3")
    operation=con.cursor()
    sql="select *  from contacttable"
    result=operation.execute(sql)
    list=result.fetchall()
    return render(request, "companycontact.html",{'data':list})


