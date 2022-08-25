# Project One - ETF Analyzer


![etf](https://user-images.githubusercontent.com/108433370/186504769-328a3156-e375-4801-85a8-c209ee266a64.jpg)


### Project Goal 

The aim of our project is to provide investors advice on which Exchange Traded Fund (ETF) is best to invest in (best returns) based on their risk appetite, type of ETF they prefer and time period they want to keep their money invested in.

In this project, we applied financial analysis concepts to be able to give sound advice to investors. In coming up with financial advice we used financial programming concepts and skills to calculate ETFs’ performance using historical data and forecasting future performance.

We selected 5 ETFs with diversified strategies for analysis:

      1. BND - Vanguard Bond ETF
      2. VNQ - Vanguard Real Estate Index Fund
      3. VOX - Vanguard Communication Services Index Fund
      4. VIG - Vanguard Dividend Appreciation Index Fund
      5. SNP - S&P 500 Index Fund

---
### How this project works …....

* We created an investor interface (CLI) where users can ask for which ETF is best to invest in based on:
    
    * Risk appetite (no/little risk, medium risk or high risk)
    * Type of ETF (Mutual Fund, Fixed Income Fund, Real Estate, Specialty/Sector, Dividend-Focused) 
    * Time / Investment Period (2, 5 or +10 years)

* Investor interface will recommend ETF to invest in based on responses 

* Financial analysis and programming codes were used to come up with financial advice 

---

### Technologies, libraries, dependencies
 
* [Pandas](https://github.com/google/pandas) - Pandas is a powerfull tool for data analysis and manipulation. Pandas provides a plethora of useful functions that make it easy to express, analyze, and manipulate data.

* [Hvplot](https://github.com/google/hvplot) - This Module provides a high-level potting API that allows for users to easily generate a wide array of plot types. HvPlot's main benefit is that it allows for very interactive visualizations.

* [Numpy](https://github.com/google/numpy) - This module offers comprehensive mathematical functions, used for working with arrays. Numpy allows for seamlessand speedy integration with a wide variety of databases.

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint. Python Fire allows us to convert our Python code into a command-line interface very easily.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs. Questionary allows us to utilize input prompts to obtain necessary information from users.

* [MCForecastTools](https://github.com/google/MCForecastTools) - This module allows for us to build a Monte Carlo simulation to predict the range of potential values for a portfolio.
   
---

### Usage

To use the financial advisory CLI file that we created for this project simply clone the repository and open the VS codes for the investor interace (CLI) is in "[questionexample.py](https://github.com/AdamCooke22/project_one/blob/main/questionexample.py)".

To use the code for the financial analysis that we created for this project simply clone the repository and open the file named "[project_one.ipynb](https://github.com/AdamCooke22/project_one/blob/main/project_one.ipynb)". 


Upon opening the financial analysis file you will have the option to run the whole note book and that will provide you with all of the calculations, evaluations, and visualizations for the analysis of the etf data. With the implementation of the Voila library you will have access to all of the outputs of the code as a web application. Some screenshots of that in action can be seen below.


This is an example of how we collected our data using the yfinance 'history' module. ![image](https://user-images.githubusercontent.com/107158380/186553900-f4fec01d-da92-4fd1-b8a4-c62fe3a5e2d7.png)

This is an example of how we sliced our data using the '.loc' function. ![image](https://user-images.githubusercontent.com/107158380/186554123-37ca3d91-1de4-4f12-838f-601af6607cd8.png)

This is an example of how we concatenated our data into a single dataframe. ![image](https://user-images.githubusercontent.com/107158380/186554199-c845edc9-6754-482e-a2cc-f9e9a17652c1.png)

This is where we displayed the closing prices of all of the funds. ![image](https://user-images.githubusercontent.com/107158380/186554808-9d15e013-db26-44d7-b8a3-d1fc02245356.png)

This is where we displayed the closing prices of only the ETFs. ![image](https://user-images.githubusercontent.com/107158380/186554887-de16ed76-a87e-452c-85cf-8ff75393ba98.png)

This is where we created a data frame of the daily returns for all of the funds. ![image](https://user-images.githubusercontent.com/107158380/186555014-f164f6ff-e3ad-469e-ba6b-013c94daba7d.png)

This is where we displayed the daily returns for each fund in a line plot. ![image](https://user-images.githubusercontent.com/107158380/186555151-b97f5f16-906f-4f04-b3ae-dd886acb39c8.png)

This is where we created a box plot on the daily returns for each fund. ![image](https://user-images.githubusercontent.com/107158380/186555303-5ac16192-95d8-495b-afb0-94dde7ad6a4e.png)

This is where we created a histogram based on the daily returns of each fund. ![image](https://user-images.githubusercontent.com/107158380/186555436-fc15e23c-bfd0-4cd7-a429-87c5fb8aa7c8.png)

This is where we created a density plot based on the daily returns of each fund. ![image](https://user-images.githubusercontent.com/107158380/186555527-44063fb9-b585-4543-b9ad-ee853f4cd01e.png)

This is where we created a dataframe by calculating the cumulative returns of each fund. ![image](https://user-images.githubusercontent.com/107158380/186555755-9355085b-c5d7-4715-ae21-6182b1cae18a.png)

This is where we visualized that dataframe with a line plot. ![image](https://user-images.githubusercontent.com/107158380/186555862-ce68a3d0-7db6-41dc-b353-8f937adc7c30.png)

This is where we created a correlation dataframe with each fund. ![image](https://user-images.githubusercontent.com/107158380/186556044-fb7ae616-d98f-4ab4-9e4d-08de6f58cfe6.png)

This is where we created a heatmap to help visualize the correlation dataframe. ![image](https://user-images.githubusercontent.com/107158380/186556151-ea9be5e8-974b-4a8b-a643-72a14586bb2f.png)

This is where we plotted the sharpe ratios with a bar plot. ![image](https://user-images.githubusercontent.com/107158380/186556249-7a6f55c2-097d-42f1-ae4b-f896fc594eec.png)

This is an example of 1 of the 15 monte carlo simulations that we did, we did 3 for each fund showing short-term ,med-term, and long-term forecasting. ![image](https://user-images.githubusercontent.com/107158380/186556427-2edb167e-296a-4e83-8b98-42337ad72a1c.png)

This is ultimately the most important part of the analysis. This is where we created a dictionary that goes through the summary statistics of each fund and displays the mean/average return trajectories. ![image](https://user-images.githubusercontent.com/107158380/186556814-e7df182b-4120-4187-b614-9a26a6f4cc41.png)

---
## Installation Guide

Before running the application first install the following dependencies.

```
import pandas as pd
import yfinance as yf
import numpy as np
import hvplot.pandas
import seaborn as sns
from MCForecastTools import MCSimulation
%matplotlib inline


```

## Contributors

Completed by Adam Cooke, Ros Tiamzon, Nevyn Brown, Priya Sukumaran

---

## License

MIT

