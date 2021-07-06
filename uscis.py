#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:13:10 2021

@author: mujib
"""

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib

driver = webdriver.Chrome()

def visit_tool():
    driver.get("https://egov.uscis.gov/casestatus/landing.do")
    
    driver.find_element_by_name("appReceiptNum").send_keys("YOUR_CASE_NUMBER")
    driver.find_element_by_xpath("/html/body/div[2]/form/div/div[1]/div/div[1]/fieldset/div[2]/div[2]/input").click()
    
    time.sleep(5)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "lxml")
    
    father_element = soup.find("div", {"class": "rows text-center"})
    
    status = father_element.h1.string
    details = father_element.find("p").text
    
    try:
        index = status.index("Approved")
        if index >=0:
            create_email = "Subject: CHECK STATUS its APPROVED !!!"
            from_address = "YOUR_EMAIL_ADDRESS"
            to_address = "YOUR_EMAIL_ADDRESS"
            
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            
            mail.starttls()
            
            mail.login("YOUR_EMAIL_ADDRESS", "YOUR_EMAILS_PASSWORD")
            mail.sendmail(from_address, to_address, create_email)
            mail.close()
            
            print("Approved :) ")
    except Exception as ex:
        print("Not Approved :(")
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        
    
visit_tool()

time.sleep(5)
driver.quit()
