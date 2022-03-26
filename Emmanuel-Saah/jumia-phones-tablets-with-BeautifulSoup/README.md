ABOUT THE PROJECT.
This project is aimed at scraping data (phones and tablets with their prices) from www.jumia.com.gh/phones-tablets. I used the Python Programming language for this project, with BeautifulSoup, urllib, and Pandas as libraries. 
Data scraped from the site www.jumia.com.gh are for learning purposes and not for commercial use.
This is an assignment given during the 6 Weeks Intensive Data Science Training organised by PyData Ghana, with Mr. Daniel Boadzie as the trainer. The programme is made up of 40 participants.

OBSERVATION:
1. Most of the contents on the page are not phones or tablets but rather phones accessories.
2. You can call the prettify() function on results returned from the find() method but you can not do same for find_all() method.
Why is this so? ...Let's find out.... (Does this mean I can also perform other bs4 methods on results returned from the find() method?)
3. I realised that I can use the pandas DataFrame and serve it with records as the input data without calling the .from_records() function on it, and everything will work just fine.
4. I didn't want my .csv to have index column so I searched and found that I can set index to False and this will solve it. Something new I learnt though....

QUESTIONS:
Do I always have to get the parent elements of the elements that contains what I am looking for before I scrape or I can just go straight to what I am looking for using bs4?
What's the main difference between find() and find_all() in terms of the objects they return? What are some of the things we can perform on them?

MORE WILL BE WRITTEN AS I THINK ABOUT THE PROJECT.