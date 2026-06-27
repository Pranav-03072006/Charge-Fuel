from django.db import models


class CustomerSignup(models.Model):
    id = models.TextField(primary_key=True, db_column='ID')
    password = models.TextField(db_column='Password')
    fullname = models.TextField(db_column='Fullname')
    address = models.TextField(db_column='Address')
    city = models.TextField(db_column='City')
    contact = models.TextField(db_column='Contact')
    gender = models.TextField(db_column='Gender')
    dob = models.TextField(db_column='DOB')
    emailid = models.TextField(db_column='EmailId')

    class Meta:
        db_table = 'customersignup'


class OrderEvCharging(models.Model):
    orderid = models.AutoField(primary_key=True, db_column='orderid')
    customerid = models.TextField(db_column='customerid')
    droplocation = models.TextField(db_column='droplocation')
    contact = models.TextField(db_column='contact')

    class Meta:
        db_table = 'orderevchargingtable'


class ContactTable(models.Model):
    fullname = models.TextField(db_column='Fullname')
    city = models.TextField(db_column='City')
    contact = models.TextField(db_column='Contact')
    query = models.TextField(db_column='Query')

    class Meta:
        db_table = 'contacttable'


class FeedbackTable(models.Model):
    customerid = models.TextField(primary_key=True, db_column='CustomerId')
    feedback = models.TextField(db_column='Feedback')

    class Meta:
        db_table = 'feedbacktable'


class CustomerComplaint(models.Model):
    complainid = models.AutoField(primary_key=True, db_column='complainid')
    customerid = models.TextField(db_column='customerid')
    orderid = models.IntegerField(db_column='orderid', null=True, blank=True)
    complain = models.TextField(db_column='complain')
    dateofcomplain = models.TextField(db_column='dateofcomplain')
    complainstatus = models.TextField(db_column='complainstatus')

    class Meta:
        db_table = 'customercomplaintable'


class CustomerOrderFuel(models.Model):
    orderid = models.AutoField(primary_key=True, db_column='Orderid')
    customer_id = models.TextField(db_column='ID')
    fuelcategory = models.TextField(db_column='Fuelcategory')
    fueltype = models.TextField(db_column='fueltype')
    quantity = models.TextField(db_column='quantity')
    droplocation = models.TextField(db_column='droplocation')
    contact = models.TextField(db_column='contact')

    class Meta:
        db_table = 'customerorderfueltable'


class CompanyLogin(models.Model):
    id = models.TextField(primary_key=True, db_column='ID', default='admin')
    password = models.TextField(db_column='Password', default='admin')

    class Meta:
        db_table = 'companylogintable'
