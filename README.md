# Analystt.ai-assessment


README.md

Amazon Product Scraper
This Python script allows you to scrape product data from Amazon search results, including product name, URL, price, rating, and number of reviews. You can customize the script to scrape data for a specific category or keyword.

Prerequisites
Before running the script, make sure you have the following installed:

Python: Ensure you have Python installed on your system. You can download it from the official Python website.

Python Libraries: Install the required Python libraries using the following command:

Copy code
pip install beautifulsoup4 requests
How to Use
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/amazon-product-scraper.git
Navigate to the Project Directory:

bash
Copy code
cd amazon-product-scraper
Run the Script:

Copy code
python scraper.py
This will run the script and start scraping Amazon search results for the specified keyword ("bags" in this case) across multiple pages. The data will be stored in a CSV file named data.csv.

Customization
Keyword: You can change the search keyword by modifying the link variable in the scraper.py file. Replace "bags" with your desired search term.

Number of Pages: By default, the script scrapes data from 20 pages. You can modify the page_no variable to scrape more or fewer pages.

Output
The scraped data will be saved in a CSV file named data.csv in the same directory as the script. The CSV file will contain the following columns:

heading: Product name.
link: Product URL.
price: Product price.
rating: Product rating.
reviews: Number of reviews for the product.
Notes
Ensure you have a stable internet connection while running the script to avoid interruptions during web scraping.
Respect the website's terms of service and policies. Web scraping should be done responsibly and ethically.
Feel free to customize and enhance the script according to your requirements! Happy coding! 🚀
