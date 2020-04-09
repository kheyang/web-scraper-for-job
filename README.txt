# Web Scraping Using Beautiful Soup - Static Website

Beautiful Soup Documentation:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Part 1: Inspect your Data Source

1.1	Explore the Website
	
1.2	Decipher the Information in URLs

	Example: https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia
	Base URL: represents the path to the search functionality of the website :: https://www.monster.com/jobs/search/
	Query parameters: represent additional values that can be declared on the page :: ?q=Software-Developer&where=Australia
	
1.3	Understand the Query Parameters
	
	Query parameters generally consist of 3 things:
	a) Start: The beginning of the query parameters is denoted by a question mark (?)	
	b) Information: The pieces of information constituting one query parameter are encoded in key-value pairs, where related keys and values are joined together by an equals sign (=)
	c) Separator: Every URL can have multiple query parameters, which are separate from each other by an ampersand (&)

1.4 	Inspect the Site Using Developer Tools
	
	Understand the page structure to pick what you want from the HTML response that you’ll collect

Part 2: Scrape HTML Content From a Page

2.1	Get Site’s HTML Code into Python Script
	
	Use Python’s requests library :: pip install requests

2.2	Performs HTTP Request to an URL
	
	Retrieves the HTML data that the server sends back and stores that data in a Python object
	See file "web-scraper.py"

2.3	Use an HTML Formatter to Clean Up 
	
	To visualuize the HTML blocks better, can use :: https://htmlformatter.com/
	Identify keywords

Part 3: Parse HTML Code with Beautiful Soup
	
3.1	Install Beautiful Soup
	
	Beautiful Soup is a Python library for parsing structured data
	Allows you to interact with HTML in a similar way to how you would interact with a web page using developer tools
	Command line :: pip install beautifulsoup4

3.2	Import Library and Create a Beautiful Soup Object

3.3	Find Elements by ID	

	In an HTML web page, every element can have an id attribute assigned
	Begin to parse your page by selecting a specific element by its ID
	
3.4	Filter Out Specific Element by its ID
	
	soup.find(id='my-specific-id')

3.5	Find Elements by HTML Class Name
	
	Every job posting is wrapped in a <section> element with the class card-content
	Work with results and select only the job postings

3.6	Extract Text from HTML Elements
	
	Add .text to a Beautiful Soup object to return only the text content of the HTML elements that the object contains
	Add .strip() to clear up white spaces

*****	The web is messy and you can’t rely on a page structure to be consistent throughout. Therefore, you’ll more often than not run into errors while parsing HTML.
	AttributeError: 'NoneType' object has no attribute 'text'	
	There could be an advertisement in there that displays in a different way than the normal job postings, which may return different results.

Part 4: Filter Only Specific Content

4.1 	Filter Out Content of Interest
	
	Instead of printing out all of the jobs from the page, you’ll first filter them for some keywords
	Job titles in the page are kept within <h2> elements
	To filter only specific jobs, can use the string argument:
	python_jobs = results.find_all('h2', string='Python Developer')
	However, when you use string= like you did above, your program looks for exactly that string. Any differences in capitalization or whitespace will prevent the element from matching.

4.2	Pass a Function to a Beautiful Soup Method

	python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
	Now you’re passing an anonymous function to the string= argument. The lambda function looks at the text of each <h2> element, converts it to lowercase, and checks whether the substring 'python' is found anywhere in there. 
	
4.3 	Extract Attributes fromm HTML Elements
	
	At this point, the script already scrapes the site and filters its HTML for relevant job postings
	One thing that’s still missing is the link to apply for a job
	The current code strips away the entire link when accessing the .text attribute of its parent element
	To get the actual URL, you want to extract one of those attributes instead of discarding it
	The URL is contained in the href attribute of the nested <a> tag

# Conclusion

Learned how to scrape data from the Web using Python, requests, and Beautiful Soup
Built a script that fetches job postings from the Internet and went through the full web scraping process from start to finish.

Learned how to:
1) Inspect the HTML structure of your target site with your browser’s developer tools
2) Gain insight into how to decipher the data encoded in URLs
3) Download the page’s HTML content using Python’s requests library
4) Parse the downloaded HTML with Beautiful Soup to extract relevant information

Source: https://realpython.com/beautiful-soup-web-scraper-python/	
