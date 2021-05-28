# CoVSL - CoWIN Vaccination Session List

This program helps you to search for available centers and vaccination sessions near your area through pincode.

---

### Prerequisites
- Basics of Python
- Requests module 
    - You can install this module by doing -  `pip install requests` in the terminal
- Link for API call which is available [here](https://apisetu.gov.in/public/api/cowin#/).
- You can also install extensions to make the data in JSON format more readable, though I haven't used any.
    - JSON Formatter is a popular Chrome-Extension, used for read data present in JSON format. You can check it out [here](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en).

---

### How this works
- So we use the get method of requests module to send a GET request to the link (for API call) and then we get the data in JSON format. 
- We extract that data, store it in a variable and use string formatting to print it neatly. 
- In this program I am using a link which finds *available sessions by pincode*. But there are more options like *search by district*, *lattitude and longitude* etc.
- There are User Authentication APIs as well which I haven't used in this program, though I might implement such feature in the future. 

---

### Features
So, this program informs us about: 
- Total number of centers present in our area.
- The name of the center (you can also print the address)
- Number of slots available on respective dates (it shows the data for the next 7 days).
- The minimum age required to take that vaccine
- The vaccine type and 
- Its fee (which is in general free of cost)

---