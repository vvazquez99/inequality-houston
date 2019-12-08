#Import libraries necessary for a suite of data analyses.
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
%matplotlib inline
import numpy as np
plt.style.use('seaborn-whitegrid')

#Load data.
inequality = pd.read_csv('/home/vanellope/Documents/Thinkful/Inequality Project/data/inequality_data.csv')
display(inequality)

#Table describing survey data.
data_info = pd.DataFrame({'Year': ['2010', '2011', '2012', '2013*', '2014', '2015', '2016', '2017'], 
                   'Sample Size': [127757, 130965, 150406, 140249, 146897, 146469, 141647, 136667], 
                   'Response Rate (%)': [95.8, 96.6, 97.0, 88.4, 95.1, 94.3, 93.4, 91.5]})
data_info['Sample Size'] = data_info.apply(lambda x: "{:,}".format(x['Sample Size']), axis=1)
display(data_info)

#Plot percent of people in poverty and percent of people with income greater than $200k per year.
plt.figure(figsize=(10,10))
plt.errorbar(inequality['year'], inequality['per_poverty'], yerr = inequality['pov_error'], label = 'In Poverty',
             fmt='o', color='c', ecolor='slategrey', elinewidth=3, capsize=0)
plt.errorbar(inequality['year'], inequality['per_200k'], yerr = inequality['200k_error'], 
             label = 'Income Greater than $200k', fmt='o', color='b', ecolor='slategrey', elinewidth=3, capsize=0)
plt.ylim(0,25)
plt.title("Fig. 2 Changes in Poverty and Wealth in Houston, Texas", fontsize = 18)
plt.xlabel("Year", fontsize = 16)
plt.ylabel("Percent of People", fontsize = 16)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#Plot median annual income at different educational attainment levels.
plt.figure(figsize=(10,10))
plt.errorbar(inequality['year'], inequality['med_earn_less_HS'], yerr = inequality['earn_less_HS_error'], 
             label = 'Less than High School', fmt='o', color='b',
             ecolor='slategrey', elinewidth=3, capsize=0)
plt.errorbar(inequality['year'], inequality['med_earn_HS'], yerr = inequality['earn_HS_error'], 
             label = 'High School', fmt='o', color='g',
             ecolor='slategrey', elinewidth=3, capsize=0)
plt.errorbar(inequality['year'], inequality['med_earn_assoc'], yerr = inequality['earn_assoc_error'], 
             label = 'Some College or Associate Degree', fmt='o', color='c',
             ecolor='slategrey', elinewidth=3, capsize=0)
plt.errorbar(inequality['year'], inequality['med_earn_college'], yerr = inequality['earn_college_error'], 
             label = 'College Degree', fmt='o', color='m',
             ecolor='slategrey', elinewidth=3, capsize=0)
plt.errorbar(inequality['year'], inequality['med_earn_grad'], yerr = inequality['earn_grad_error'], 
             label = 'Graduate Degree', fmt='o', color='y',
             ecolor='slategrey', elinewidth=3, capsize=0)
plt.ylim(0,80000)
plt.title("Fig. 3 Educational Attainment and Income in Houston, Texas", fontsize = 18)
plt.xlabel("Year", fontsize = 16)
plt.ylabel("Annual Median Income (US$)", fontsize = 16)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#Plot of percent of people at different educational attainment levels.
plt.figure(figsize=(10,10))
plt.errorbar(inequality['year'], inequality['pov_lessHS'], yerr = inequality['pov_lessHS_error'], 
             label = 'Less Than High School', fmt='o', color='b',
             ecolor='slategrey', elinewidth=3, capsize=0)
plt.errorbar(inequality['year'], inequality['pov_HS'], yerr = inequality['pov_HS_error'], 
             label = 'High School Degree', fmt='o', color='g',
             ecolor='slategrey', elinewidth=3, capsize=0)
plt.errorbar(inequality['year'], inequality['pov_assoc'], yerr = inequality['pov_assoc_error'], 
             label = 'Some College or Associate Degree', fmt='o', color='c',
             ecolor='slategrey', elinewidth=3, capsize=0)
plt.errorbar(inequality['year'], inequality['pov_college'], yerr = inequality['pov_college_error'], 
             label = 'College Degree', fmt='o', color='m',
             ecolor='slategrey', elinewidth=3, capsize=0)
plt.ylim(0,35)
plt.title("Fig. 4 Poverty and Educational Attainment in Houston, Texas", fontsize = 18)
plt.xlabel("Year", fontsize = 16)
plt.ylabel("Percent of People", fontsize = 16)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=1.0)

wealthiest = pd.DataFrame({'Name': ['Richard Kinder', 'Dannine Avara', 'Scott Duncan', 'Milane Frantz', 'Randa Williams', 
                                    'Tillman Fertitta', 'Dan Friedkin', 'Jeffery Hildebrand', 'Robert McNair', 
                                    'John Arnold', 'Leslie Alexander'], 'Source of Wealth': ['Pipelines', 'Pipelines', 
                                    'Pipelines', 'Pipelines', 'Pipelines', 'Entertainment', 'Automobiles', 'Energy', 
                                    'Energy', 'Investment Banking', 'Investment Banking'], 'Net Worth': ['$6.6B', 
                                    '$6.2B', '$6.2B', '$6.2B', '$6.2B', '$4.5B', '$4B', '$4B', '$3.8B', '$3.3B', 
                                    '$2.1B']})
display(wealthiest)