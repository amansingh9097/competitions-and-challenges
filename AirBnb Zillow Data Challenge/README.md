# AirBnb & Zillow Data Challenge

## Challenge and Expectations

Isn’t data just more fun when you can interact and play with it? We need to find great people to join our team as we develop software data products across our three key areas of data work:
- Builder Mindset: Leverages creative and adaptive problem solving to selecting the right tool for the job; seeks automated and efficient solutions to manual or repetitive processes.
- Data Management: Strategically leads efforts to systematically evaluate, and document; monitors our data in a sustained and organizationally recognized way
- Business Intent: Translates business needs into actionable solutions or data products; effectively communicate results to stakeholders and technical partners.  

After receiving data instructions you’re putting hands-to-keyboard and have 1 week to submit a working data product, per the submission instructions, including: <br>
✔ Working code with documentation<br>
✔ Documentation of metadata and data quality <br>
✔ Visualizations of key insights<br>

Ready to show off your data chops? Let’s go!

## Problem Statement and Instructions

### Problem Statement

You are consulting for a real estate company that has a niche in purchasing properties to rent out short-term as part of their business model specifically within New York City.  The real estate company has already concluded that two bedroom properties are the most profitable; however, they do not know which zip codes are the best to invest in.    

The real estate company has engaged your firm to build out a data product and provide your conclusions to help them understand which zip codes would generate the most profit on short term rentals within New York City.
- You will be looking at publicly available data from Zillow and AirBnB:
- Cost data: Zillow provides us an estimate of value for two-bedroom properties
- Revenue data: AirBnB is the medium through which the investor plans to lease out their investment property. Fortunately for you, we are able to see how much properties in certain neighborhoods rent out for in New York City
- You can assume an occupancy rate of 75% or you can come up with your own model to calculate occupancy; just let us know how you came to that calculation.

After meeting with the strategy team, you’ve got an idea of where to start, key concerns, and how you can help this real estate company with the market data while keeping the following assumptions in mind:
- The investor will pay for the property in cash (i.e. no mortgage/interest rate will need to be accounted for).
- The time value of money discount rate is 0% (i.e. $1 today is worth the same 100 years from now).
- All properties and all square feet within each locale can be assumed to be homogeneous (i.e. a 1000 square foot property in a locale such as Bronx or Manhattan generates twice the revenue and costs twice as much as any other 500 square foot property within that same locale.)

### Instructions
As you start the challenge, realize that this is real-world, imperfect data.  We recommend planning about 4 hours to complete the Data Challenge, but it’s not timed, and you are judged on the quality of the work submitted.  If you find yourself uncertain of what the “right” answer is, use your best judgment, make an assumption (document the assumption), and keep going.  

Overall, we first ask you to show your data skills in three areas at a basic level, and then, in the last step, tell us what you would do next to provide a better conclusion. 

1. Quality Check – bad data is worse than no data at all
	a. Understand the data while keeping your final output in mind
	b. Highlight two to three data quality insights based on your analysis of the data
	c. Create metadata for any derived fields or metrics used to complete your analysis
2. Data munging – get the data
	a. The datasets do have different units of time – in order to complete the analysis, you will need to determine a common unit of time
	b. Write a function that can link the data together in a scalable way when new data is available or for when we are ready to approach a new market
3. Craft a visual data narrative – Charts and plots must be generated from your code; not from produced in external standalone software like Excel
	a. Visualize metrics for profitability on short term rentals by zip code
	b. Summarize your key insights and conclusions based on the data and your analysis
4. What’s Next – We recognize that 4 hours isn’t a lot of time… and you’ve probably come up with a number of great ideas from an analytical or visualization perspective that you don’t have time to do.  Tell us (but don’t do any work) what you would/could do next to inform a better decision or deliver a better product to the real estate company.

### Data and Tools
Solutions that require purchase of a software license or purchased access to data will not be accepted regardless of whether or not company uses said software or data. Abide by all applicable laws and regulations regarding the use of software or external data sources. If you have questions about a particular software package, please contact your recruiter immediately. 

#### Data
You need two datasets for this Challenge:<br>
	1. AirBnB data:  [Download from here](http://data.insideairbnb.com/united-states/ny/new-york-city/2019-07-08/data/listings.csv.gz)<br>
	2. Zillow data:  Zip_Zhvi_2bedroom.csv.zip <br>

In addition, you should have received the following additional files from Recruiting

### Tools
Here are some example platforms you should feel free to use. By no means are you limited to this list, and our solution review team will be able to evaluate solutions in most languages. If you really do have a question about the platform you would like to use to solve the problem, contact your recruiter with the exact setup you’d like to use (including OS and specific versions when applicable), your backup choice, and they can seek verification for the platform

Platform example	       |Notable packages                     |
-------------------------------|-------------------------------------|
Anaconda Python Distribution   |notebook, pandas, matplotlib, bokeh  |
R 			       |R, Shiny, plyr, ggplot               |
Javascript		       |D3, nvd3, node.js, Tableau           |
Java virtual machine	       |Groovy, Scala                        |
Other software packages with which you are familiar                  |

1. Working source code file with documentation 
	1.1. Code
	1.2. Source documentation (e.g., a README file)
	1.3. Any generated graphics files
	1.4. If you added data: if you added more than a couple of MB of data, provide a program or script, with documentation, to download the data set 
2. Documentation including metadata for any data created and your data quality insights
3. Visualizations and key insights from those visualizations

### Acknowledgements

The data for this challenge were sourced from: <br>
● [Zillow Group, Inc. (2016)](http://www.zillow.com/research/data/)<br>
● [Airbnb](http://insideairbnb.com/get-the-data.html)<br>

--

# Submission:

## How to run?
- `pip install -r requirements.txt`
- `python submission.py`

## How to view all the analysis at one place?
- Install `Jupyter Notebook`. [Link to download]()
- Navigate to the directory containing the `Airbnb-Zillow-Data-Challenge-Exploratory_Data_Analysis.ipynb` file.
- Open up Command Prompt(Windows) or Terminal(any Linux distro), and type the following command<br>
	`jupyter notebook`
- Open up the file `Airbnb-Zillow-Data-Challenge-Exploratory_Data_Analysis.ipynb`.

## I don't want to  install Jupyter Notebook, how do I view all analysis at one place?
- View the [pdf version](https://github.com/amansingh9097/Airbnb-Zillow-Data-Challenge/blob/master/Airbnb-Zillow-Data-Challenge-Exploratory_Data_Analysis.pdf) of the jupyter notebook.


**python version** used for analysis: **3.7**
