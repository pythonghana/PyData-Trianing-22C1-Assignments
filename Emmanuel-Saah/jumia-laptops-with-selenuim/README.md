SCRAPING JUMIA LAPTOPS/COMPUTERS WITH SELENIUM AND XPATH.
This project is an assignment given during the PyData Ghana 6 Weeks Intensive Data Science Training. It's a beginner's course in Data Science. 
The assignment is meant to check our understanding of the Selenuim and Xpath.
I scraped the url, "https://www.jumia.com.gh/catalog/?q=laptops", for available laptops, their prices and the links that leads to details about the laptop.
During the scraping journey, I realised that it is easier to use Selenium and xpath to scrape a website than to use Requests or urllib and BeautifulSoup. 
Selenium makes it easy to access content on the website. You hardly face a 403 response code. I guess this is because it controls the browser. I used the Chrome webdriver for linux ubuntu and version 99 of the chrome browser.
The tideous part of this assignment was using xpath to find and scrape the links that points to each laptop on the page.
I spent hours and days on this alone. Lol....It's normal in programming....I guess.
I googled and asked questions. Fell into errors and fraustrations but finally I was able to do it. I picked some clues from what our instructor for the program, Mr. Daniel Boadzie, gave.

The data from this scraping was processed with pandas and saved in a csv file.

GOING FORWARD.....
I hope to use Pagination in Selenuim to scrape all laptop products in Jumia's catelog. This will be after I have learnt how it is done.
I also have to read more on how to use xpath.