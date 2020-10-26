# Cleaning, preliminary analysis and interpretation of residential real estate sales in Belgium (What)
The real estate company "ImmoEliza" wanted to create a machine learning model to predict prices on Belgium's sales.
A complete analysis and interpretation of the dataset was provided. 

# The Mission (Why)
- Be able to use pandas
- Be able to use Data visualisation libraries.(Matplotlib or Seaborn)
- Be able to establish conclusions about a dataset. 

## Features 
Hereby follow the project results by section. The related presentation, including graphs obtained through Matplotlib/Seaborn is available [here](https://github.com/FrancescoMariottini/residential-real-estate-analysis/blob/main/project3.pptx).

### A cleaned dataset
The provided dataset (available here) is cleaned of:
- duplicates
- blank spaces (ex: ``" I love python  "`` =>  ``"I love python"``)
- errors
- empty values

### Data analysis overview (QUESTIONS TO BE REPLACED WITH ANSWERS)
Hereby follow the main results from the preliminary data analysis:
- Which variable is the target ?
- How many rows and columns ?
- What is the correlation between variable/target ? (Why?)
- What is the correlation between the variables/variables ? (Why?)
- Which variables have the greatest influence on the target ?
- Which variables have the least influence on the target ?
- How many qualitative and quantitative variable is there ? How would you transform these values into numerical values ? 
- Percentage of missing values per column ?

### Data interpretation questions (<ins>non-exhaustive</ins> list)(QUESTIONS TO BE REPLACED WITH ANSWERS)
Hereby follow the main results from the data interpretation:
- Are there any outliers? If yes, which ones and why?
- Which variables would you delete and why ?
- In your opinion, which 5 variables are the most important and why?
- What are the most expensive municipalities in Belgium? (Average price, median price, price per square meter)
- What are the most expensive municipalities in Wallonia? (Average price, median price, price per square meter)
- What are the most expensive municipalities in Flanders? (Average price, median price, price per square meter)
- What are the less expensive municipalities in Belgium? (Average price, median price, price per square meter)
- What are the less expensive municipalities in Wallonia? (Average price, median price, price per square meter)
- What are the less expensive municipalities in Flanders? (Average price, median price, price per square meter)

### Presentation (26/10/20) 
Presentation is available here.

SY prepared the first draft of the presentation and the template. It was agreed to have 1 or 2 slides per person to kept the total presentation time within 5 minutes. No code was included in the presentation.


# Who did the project (Who):
Contributors : Joachim Kotek (JK), Francesco Mariottini (FM), Orhan Nurkan (ON), Saba Yahyaa (SY)

# Development (How)

## Communication and Management
Communication went mainly through live discussion on-site and, to a smaller extent, on Discord. Project management was mainly carried on Trello (available [here](https://trello.com/b/gtM8bCin/randomforest-progress)) with each person (mainly ON and FM) adding indipendently the labels and tasks as well as involving other team members on them. 
FM provided code specifications or clarifications when requested (e.g. column identifiers to check duplicates) or strictly needed (e.g. percentiles for outliers identifications and replacement of not realistic values with nan).

## Merging datasets from different sources (How)
Different independent teams worked on a merged dataset to be used by all the team.
On the first day (21/10/20) CUDA team splitted the sources (group 5's data were excluded because they only scrapped a few features in project 1) as follows: JK worked on source 3 and 4, FM worked on source 1 and 7, ON worked on source 2, 3 and 6. Group 3 required collaboration. Additional cleaning work was carried on the 22/10/20 by JK to improve the merged dataset for all the teams.
FM was also comparing the final dataframes from his team and Selma's team to verify which one was most fitted to be used.

## Pycharm & Github training (How)
At least 2 person days were spent on technical teaching (and installation) and clarifications about pycharm (FM), git (FM, JK) and statistics (FM) to allow everybody to work on the project. Additional self-training was spent by SY on understanding and replicating the code already developed by the team.

## Code merging (How)
JK toke sole responsibility for merging the code in order to effectively implement code from different sources (git and jupyter files) and eventually reviewing the code if necessary. When running the data formatting and values cleaning tools (see later), FM provided feedback to JK to ensure the resulting cleaned dataset complied with the required specifications.
Code merging was done inside a utility class named ```SalesDataCleaner``` that takes a path (or a URL) to a CSV file, loads it into a DataFrame then proceeds to clean it. Then a copy of the cleaned DataFrame is accessible with a public method for further jobs (such as visualization, data interpretation, learning algorithms)

## Data formatting and values cleaning (How)
Data cleaning was splitted into two main groups: initial formatting for similar types of columns (FM) and additional specific formatting for particularly complex cleaning.
FM toke reponsibility for the overall cleaning including: formatting to the required types, identification of string representing na (and replacement by na), extraction of simple numbers from text. ON worked on cleaning and aggregating the categorical values with multiple text values like subtype of property, location and state of the building. JK cleaned the postcode and toke over on price cleaning.

The resulting dataset before the first analysis is the following:
information|column name|variable type|example(s) or description
---|---|---|---
Source (team)|source|int|from 1 to 7|
Hyperlink|hyperlink|str||
Locality|locality|str||
Postcode|postcode|int||
Type of property (House/apartment)|house_is|bool||
Subtype of property|property_subtype|str|Bungalow, Chalet, Mansion, ...|
Price|price|int||
Type of sale (Exclusion of life sales)|sale|str|
Number of rooms|rooms_number|int|
Area|area|int|
Fully equipped kitchen (Yes/No)|kitchen_has|bool|
Furnished (Yes/No)|furnished|bool|
Open fire (Yes/No)|open_fire|bool|
Terrace (Yes/No)|terrace|bool|
Terrace Area|terrace_area|int|
Garden (Yes/No)|garden|bool|
Garden Area|garden_area|int|
Surface of the land|land_surface|int|
Surface area of the plot of land|land_plot_surface|int|
Number of facades|facades_number|int|
Swimming pool (Yes/No)|swimming_pool_has|bool|
State of the building|building_state|str|(New, to be renovated, ...)

## Data interpretation
JK took charge of creating categorical data bins from the 'area' property. Upon inspection of the distribution of instances for each possible area, the group has decided to use the following bins in order to have a similar number of instances per bin: [0-60 m²], [60-90 m²], [90-120 m²], [120-180 m²], [180-250 m²] and [250 m² and more].
As we expected, in each categorical bin, Brussels was the most expensive, followed by Flanders then Wallonia, in terms of mean but also in therm of median wich is a more interesting measure considering the outlier price we have in this dataset.
It should also be noted that the proportionality between each region in each data bin seemed to be approximately respected.

SY visualizes the percentage of missing values in each column alone and percentage of missing values in total.
SY visualizes the qualitative and quantitative features and checked the outliers in the quantitative feature using zscore. SY visualizes the quantitative features after deleting some outliers. SY fills the nan values of the area and price with their mean to fill the empty cells. SY creates violinplot to have fast visualize that Brussels is the most expensive in house compared to others.

FM introduced the procedure of replacing non-realistic values in the column (e.g. zero surface area) with np.nan values and implemented filters on all the numerical tables showing a pattern close to normal distribution (and not an excessive concentration of values towards higher values). Outliers analysis was distinguished by apartments and houses. Median price by postcode and by building status were introduced to deal with the correspondent non-numerical values. An online Google survey (available [here](https://docs.google.com/forms/d/1zLxgbiZQcPLo6fb5cEHZEC_Oye6vH9rCubEPmQZ-Fhk/edit?gxids=7628#responses)) was also carried on to be compared with found correlation.

ON created 50+ data analysis charts that he decided himself to make rough comments on the data before cleaning and editing the data, and he presented it to the members of the team for review. So we decided the meaning of the data and what kind of graphs we could concentrate on. He also prepared 18 graphs in seaborn, which is the goal of the project. He also joined tasks such as data cleaning and grouping columns area , building_state and others mand so.

# Future improvements 
TBD

# Take over
1. Excel may be an effective solution on a single table analysis but joining different tables through pandas could be more effective.
1. Task(s) must be fully clarified and agreed to avoid overlaps.
1. Teaching and self-training (code undersanding and replication) should be limited in the amount of time and effort spent during a project.

# Collecting Data (When)
- Repository: `challenge-data-analysis`
- Type of Challenge: `Consolidation`
- Duration: ``4 people * 3 days ` plus out of hours working
- Deadline: `26/10/2020 14:00`(extended from `23/10/2020 17:00`) 
- Presentation: `26/10/2020 14:00`
- Team challenge : 4

