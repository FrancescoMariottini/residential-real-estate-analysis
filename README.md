# "Collecting real estate sales in Belgium" (What)
The real estate company "ImmoEliza" wants to create a machine learning model to predict prices on Belgium's sales.
A complete analysis and interpretation of the dataset need to be provided. 

# The Mission (Why)
- Be able to use pandas
- Be able to use Data visualisation libraries.(Matplotlib or Seaborn)
- Be able to establish conclusions about a dataset. 

## Features 
Hereby follow the project requirements divided by section. Results will need to be presented through Matplotlib/Seaborn.

Everything need to be updloaded <ins>non-exhaustive</ins> Friday 23/10/20.

### Providing a cleaned dataset
- No duplicates
- No blank spaces (ex: ``" I love python  "`` =>  ``"I love python"``)
- No errors
- No empty values

### Data analysing questions 
- Which variable is the target ?
- How many rows and columns ?
- What is the correlation between variable/target ? (Why?)
- What is the correlation between the variables/variables ? (Why?)
- Which variables have the greatest influence on the target ?
- Which variables have the least influence on the target ?
- How many qualitative and quantitative variable is there ? How would you transform these values into numerical values ? 
- Percentage of missing values per column ?

### Data interpretation questions (<ins>non-exhaustive</ins> list)
- Are there any outliers? If yes, which ones and why?
- Which variables would you delete and why ?
- In your opinion, which 5 variables are the most important and why?
- What are the most expensive municipalities in Belgium? (Average price, median price, price per square meter)
- What are the most expensive municipalities in Wallonia? (Average price, median price, price per square meter)
- What are the most expensive municipalities in Flanders? (Average price, median price, price per square meter)
- What are the less expensive municipalities in Belgium? (Average price, median price, price per square meter)
- What are the less expensive municipalities in Wallonia? (Average price, median price, price per square meter)
- What are the less expensive municipalities in Flanders? (Average price, median price, price per square meter)

### Presentation (26/10/20) characteristics
- professional design
- 5 minutes long
- participation of each team member
- no showing of code or jupyter notebook

### Readme characteristics
- What, Why, When, How, Who.
- Pending things to do
  
### Evaluation criteria summary
Hereby follow the criteria to be comply with
| Criteria       | Indicator                                                                             | Yes/No |
|----------------|---------------------------------------------------------------------------------------|--------|
| 1. Is complete | Know how to answer all the above questions.                                           |        |
|                | Use pandas and matplotlib/seaborn.                                                    |        |
|                | Pimp up the readme. (what,why, how, who)                                              |        |
|                | Present the results                               			                         |        |
| 2. Is good     | The repo doesn't contains unnecessary files.                   			             |        |
|                | You used typing.                                                			             |        |
|                | The presentation is clean.                                   			             |        |  

# Who did the project (Who):
Contributors : Joachim Kotek (JK), Francesco Mariottini (FM), Orhan Nurkan (ON), Saba Yahyaa (SY)

# Development (How)

## Communication and Management
Communication went mainly through live discussion on-site and, to a smaller extent, on Discord. Project management was mainly carried on Trello with each person adding indipendently the labels and tasks as well as involving other team members on them. 

## Merging datasets from different sources (How)
Different indipendent teams worked on a merged dataset to be used by all the team.
On the first day (21/10/20) CUDA team splitted the sources (5 was excluded not being good enough) as follows: JK worked on source 3 and 4, FM worked on source 1 and 7, ON worked on source 2, 3 and 6. Group 3 required collaboration. Additional cleaning work was carried on the 22/10/20 by JK to improve the merged dataset for all the teams.

## Pycharm & Github training (How)
At least 2 person days were spent on technical teaching (and installation) and clarifications about pycharm (FM), git (FM, JK) and statistics (FM) to allow everybody to work on the project. Additional self-training was spent by SY on understanding and replicating the code already developed by the team.

## Code merging (How)
JK toke sole responsibility for merging the code in order to effectively implement code from different sources (git and jupyter files) and eventually reviewing the code if necessary.

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

# Take over
1. Excel may be an effective solution on a single table analysis but joining different tables through pandas could be more effective.
1. Task(s) must be fully clarified and agreed to avoid overlaps.
1. Teaching and self-training (code undersanding and replication) should be limited in the amount of time and effort spent during a project.

# Collecting Data (When)
- Repository: `challenge-data-analysis`
- Type of Challenge: `Consolidation`
- Duration: ``4 people * 3 days ` plus out of hours working
- Deadline: `23/10/2020 17:00`
- Presentation: `26/10/2020 9:00`
- Team challenge : 4

