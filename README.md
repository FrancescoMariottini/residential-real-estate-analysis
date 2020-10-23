# "Collecting real estate sales in Belgium" (What)
The real estate company "ImmoEliza" wants to create a machine learning model to predict prices on Belgium's sales.
A complete analysis and interpretation of the dataset need to be provided. 

# The Mission (Why)
- Be able to use pandas
- Be able to use Data visualisation libraries.(Matplotlib or Seaborn)
- Be able to establish conclusions about a dataset. 

## Features 
The dataset holds the following information.

Everything in a csv file.

## Highlights
TBD
- Data for all of Belgium.
- Minimum 10 000 inputs
- No empty row. If information is missing, the value is set to None.
- No duplicates. 
- Binary values replacing "Yes" or "Not" 

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

## Data formatting and cleaning (How)
Data cleaning was splitted into two main groups: initial formatting for similar types of columns (FM) and additional specific formatting for particularly complex cleaning.
FM toke reponsibility for the overall cleaning including: formatting to the required types, identification of string representing na (and replacement by na)

The resulting dataset was the following:
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

## Code merging (How)
JK toke sole responsibility for merging the code in order to effectively implement code from different sources (git and jupyter files) and eventually reviewing the code if necessary.



## Take over
TBD
1. Input(s) and output(s) must be fully clarified and agreed when working independently on modules.
1. A clearer workflow, including responsibilities and deadlines, could help to make coding more effective.
1. Every team members should be able to run the used packages to allow also parallel testing
1. Previous training necessary to effectively code and support team members.



# Collecting Data (When)
- Repository: `challenge-data-analysis`
- Type of Challenge: `Consolidation`
- Duration: ``4 people * 3 days ` plus out of hours working
- Deadline: `23/10/2020 17:00`
- Presentation: `26/10/2020 9:00`
- Team challenge : 4

