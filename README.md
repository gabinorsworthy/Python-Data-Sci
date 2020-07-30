# Python-Data-Sci
**The exercises in this repository were designed and developed by [Eric Lohmar](https://github.com/EEdLoh).**

Per the designer of this course, Eric Lohmar, this set of exercises serves to "[Explore] the world of the Python Programming language with the intent to gain an understanding of Data Science and Machine Learning processes and skills."

# Python Basics
The first 5 exercises focus on learning the basics of Python - data types, string methods, conditionals, loops, functions, classes, and objects.
* 01: Python Data Types and Collections
* 02: Strings and String Methods in Python
* 03: Control Flow in Python
* 04: Functions in Python
* 05: Classes and Objects in Python

To run the exercises above, simply download the file and run in the following command line prompt. 
```bash
python "[file name]"
```
Using VS Code, you can also run the Jupyter cells in the Python Interactive Window. Be sure to install Jupyter using the following command line prompt.
```bash
pip install jupyter
```

# Python Pandas, MatPlotLib, and Seaborn
The final 3 exercises focus on understanding pandas, matplotlib, and seaborn Python libraries as they apply to data visualization and statistical analysis.
* 06: Intro to Pandas
* 07: Understanding and Interpolating Data with Pandas
* 08: Visualizing Data with Pandas, MatPlotLib, and Seaborn

To run the exercises above, I highly recommend using Python's Interactive Window to run the Jupyter cells.
The dataframes and data displays much cleaner using the interactive window. If using the command line to run
these exercises, the plots will show up, but the dataframes and other results are not set up to print in the command line.

# Exercise Examples
Below are some example graphs created in the final exercise.

**AAL Daily Highs**

The below graph was created from the data in 'aalStock.csv' and displays the daily, 7-day rolling average, and 30-day rolling average lines for the stock's highs.

Using pandas, the information was prepped by pulling data from the file into a dataframe, re-indexing and sorting the dataframe based on date,
and creating new columns with the 7-day and 30-day rolling averages. Then, using matplotlib, the three lines from the dataframe were plotted and labeled on the figure.

![AAL Daily Highs](/images/aal_daily_high.png)


**AAL Stock Data**

The below subplots were created using the same data from the previous graph. The three subplots show the following information, respectively:
1. AAL stock volume over time
2. AAL daily opening and closing prices
3. AAL daily high and low prices

![AAL Stock Data](/images/aal_stock_subplots.png)


**Tip Percentage by Customer**

The figure below was created from the data in 'tips.csv' and displays a swarmplot representing the tip percentage of customers - each dot representing an individual customer.
The customers are further broken down by day of the week they visited (on the x-axis) and smoker vs. non-smoker (by color).

Using pandas, the information was prepped by pulling data from the file into a dataframe and creating a new column for tip percentage based on the tip and the total bill.
The figure was created using seaborn's swarmplot method and then label and displayed using matplotlib.

![Tip % Swarmplot](/images/tip_percentage_swarmplot.png)
