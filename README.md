# 🇺🇸 USCIS Case Status 📣
With this automation, we can check our case status, also this tool will mail you when your case is "Approved".

When we apply for **H1B** visa 🎫 we have to keep checking the case status, so for the same I made this script which will automate the entire activity for you :).

When we run this script, selenium will open the chromium instance and open the **USCIS**'s tool url, also it will populate with given case number and will click on search button. Once the response came it will analyze it and if it found to be case as "Approved", it will mail you for the same 📨.

#### Pre-requisite 📝:

Following packages need to be installed before using the script.

1. Selenium package
2. BS4 (i.e. BeautifulSoup)
3. SMTP library

**⚠️ Note:** Before using the script, please update the place-holder in the script with your values.

We can also use **crontab** to run this script in regular interval of time, like everyday at 12 noon etc.

Press ⭐️ to repo, if you find this is awesome.