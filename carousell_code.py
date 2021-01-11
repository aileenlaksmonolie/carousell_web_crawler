#!/usr/bin/env python
# coding: utf-8

# In[2]:


import smtplib
from pandas import DataFrame
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
#print("now =", now)

#query string

test = 'iphone 11 pro dual sim'
x = test.replace(' ', '%20')
#print(x)

end_price = '960'
start_price = '1049'
condition = 'USED%2CNEW'

import requests 
from bs4 import BeautifulSoup 

def find_item_carousell_3():#This will not run on online IDE 

    URL = 'https://sg.carousell.com/search/' + x +'?condition_v2='+condition+'&price_end='+end_price +'&price_start='+start_price+'&sort_by=time_created%2Cdescending'
    print(URL)

    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    #print(soup.prettify()) 

    table = soup.find('main', attrs = {'class':'_3egzkmmXgV'}) 
    #for row in table.findAll('div', attrs = {'class':'An6bc8d5sQ _9IlksbU0Mo _2t71A7rHgH'}): 
        #print(row.prettify())

    price_list = []
    for row in table.findAll('p', attrs = {'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6'}): 
        price_list.append(row.getText())

    listings_name_list = []
    for row in table.findAll('p', attrs = {'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}): 
        listings_name_list.append(row.getText())
    listings_name_list

    username_list = []
    for row in table.findAll('p', attrs = {'class':'_1gJzwc_bJS _2NNa9Zomqk Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}): 
        username_list.append(row.getText())

    time_list = []
    for row in table.findAll('p', attrs = {'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3HOr_TevCw _30RANjWDIv'}): 
        time_list.append(row.getText())

    caption_list = []
    for row in table.findAll('p', attrs = {'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _30RANjWDIv'}): 
        caption_list.append(row.getText())


    #print(time_list)

    caption_list_2 = []
    y = 0
    for i in caption_list:
        if y % 3 == 0:
            caption_list_2.append(i)
        y+=1
    len(listings_name_list)

    from pandas import DataFrame
    carousell_df = DataFrame(username_list,columns=['carousell account'])
    carousell_df['listings'] = listings_name_list
    carousell_df['price'] = price_list

    if (len(price_list)==0):
        print('none found. time: ');
        now = datetime.now()
        print("now =", now)
    else:
        carousell_df['price'] = carousell_df['price'].str.replace('$', '')
        carousell_df['price'] = carousell_df['price'].str.replace('S', '')


        carousell_df['price'] = carousell_df['price'].str.replace(',', '')
        carousell_df['price'] = carousell_df['price'].astype(str).astype(int)

        table = soup.find('main', attrs = {'class':'_3egzkmmXgV'}) 
        mean_price = str(carousell_df['price'].mean())
        carousell_df['price'] = carousell_df['price'].astype(int).astype(str)


        carousell_df.columns = ['name', 'item','price']
        name = carousell_df.name.str.cat(sep=',')
        item =carousell_df.item.str.cat(sep=',')
        price =carousell_df.price.str.cat(sep=',')
        string_append='username: ' + name+ '\n' + 'itemname: '+ item+ '\n' + 'price: ''$' + price + '\n' + 'mean price: '+ mean_price
        print('sending')
        #Email Account
        email_sender_account = "ssp.17s18.aileenlaksmonolie@gmail.com"
        email_sender_username = "ssp.17s18.aileenlaksmonolie@gmail.com"
        email_sender_password = "Alight89"
        email_smtp_server = "smtp.gmail.com"
        email_smtp_port = 587
        #Email Content
        email_receivers =["ssp.17s18.aileenlaksmonolie@gmail.com"]
        email_subject = "<iPhone 11 pro dual sim HIGH PRICE>"
        email_body = string_append
        #login to email server
        server = smtplib.SMTP(email_smtp_server,email_smtp_port)
        server.starttls()
        server.login(email_sender_username, email_sender_password)
        #For loop, sending emails to all email recipients
        for recipient in email_receivers:
            print(f"Sending email to {recipient}")
            message = MIMEMultipart('alternative')
            message['From'] = email_sender_account
            message['To'] = recipient
            message['Subject'] = email_subject
            message.attach(MIMEText(email_body, 'html'))
            text = message.as_string()
            server.sendmail(email_sender_account,recipient,text)
        print('sent')
        #All emails sent, zlog out.
        server.quit()


# In[ ]:




