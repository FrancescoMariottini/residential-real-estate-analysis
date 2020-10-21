# "Collecting real estate sales in Belgium" (What)
TBS
A tool to scrap real estate sales data from Belgium to obtain a valuable insight of the real estate market.

# The Mission (Why)
TBS
The real estate company "ImmoEliza" wants to create a machine learning model to make price predictions on real estate sales in Belgium. 

## Features 
The dataset holds the following information.

information|column name|variable type|example(s)
---|---|---|---
Source (team)|source|str|groups names to be agreed|
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

Everything in a csv file.

## Highlights
TBD
- Data for all of Belgium.
- Minimum 10 000 inputs
- No empty row. If information is missing, the value is set to None.
- No duplicates. 
- Binary values replacing "Yes" or "Not" 

# Who did the project (Who):
Contributors : Philippe Fimmers (PF), Francesco Mariottini (FM), Opap's Ditudidi (OD)

# Development (How)
First brainstorm identified four main independent modules:
1. Scrapping links of valid search results from Immoweb (PF & OD ).
    * Input: search hyperlinks (one per results page).
    * Output: hyperlinks, type of property and postcode.
1. Scrapping required information from each building (PF & OD).
    * Input: building hyperlink (one per house/apartment).
    * Output: scrapped building parameters and values.
1. Cleaning result through quality checks (FM).
    * Input: building parameters and values as dictionary of lists.
    * Output: full table (dataframe) including checks and cleaned table.
4. Filling founded parameters into a csv (FM).

OD started (1) after realising challenge of scrapping building results through only BeautifulSoup function. PF found a solution to it by using Selenium and reviewed both (1) and (2) with the help of OP.
FM worked independently on (3) and (4).

## Links scrapping development (How)
Since the single building page provides information only about the subtype, and not if it is an house or an apartment, it was agreed to check the type of property parameter (house_is) was checked during module (1). 

## Data cleaning development (How)
Data cleaning development initially includes only general cases and testing was performed on a small generated dataset since scrapped building information were initially not available. 
A preliminary analysis on the research engine showed frequent not filled parameters and a few inconsistencies in the datasets, i.e.count of True and False values higher than the number of values provided when launching an unfiltered search (e.g. presence of garden). 
Due to time pressure these issues were not investigated immediately but delayed until the overall dataframe analysis.
(3) was progressively extended based on the received (2) outputs to comply with project requirements.
Since data type manipulation wasn't performed for all the parameters during (2), handling of exceptions and instances as well as a formatting function was added to (3) to cope with it.
True and False values were replaced by 0 and 1 only when running the dataframe describe function to provide meaningful results.

## Take over
1. Input(s) and output(s) must be fully clarified and agreed when working independently on modules.
1. A clearer workflow, including responsibilities and deadlines, could help to make coding more effective.
1. Every team members should be able to run the used packages to allow also parallel testing
1. Previous training necessary to effectively code and support team members.

# Collecting Data (When)
- Repository: `challenge-collecting-data`
- Type of Challenge: `Consolidation`
- Duration: `3 days * 3 people` (officially) but additional out of work time spent  `at least 1 day * 1 person`
- Deadline: `25/09/2020 17:00`, postponed to `28/09/2020 17:00`
- Team challenge : 3



