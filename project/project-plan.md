# Project Plan

## Title
<!-- Give your project a short title. -->
Rituparna_M-A-D-E_Project

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Does the analysis help to do correlate rate of road accident in Cologne and vehicle counting points with values in Cologne

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The project examines the link between the rise in accidents and vehicle counting with value in Cologne.The aim is to gradually include all routes in the main road network. Routes without values ​​were not counted from 2010 to 2016.

This data set contains the surveys from the automatic counting points for Cologne's cycling traffic from 2009.With the activation of a website for the permanent counting points, we are offering this service for the first time.


## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource 1: Mobilithek
* Metadata URL 1: https://mobilithek.info/offers/-7344603824143622751
* Data URL 1:  https://offenedaten-koeln.de/sites/default/files/KFZ_Zaheldaten_2016-2019_node.csv
* Data Type: CSV Vehicle counting points and values ​​Cologne
  

### Datasource 2: European Data Portal
* Metadata URL 2: https://data.europa.eu/data/datasets/70dd472a-dce0-401c-bb3e-5322d626e1f0?locale=en
* Data URL 2: https://offenedaten-koeln.de/dataset/unfallstatistik-k%C3%B6ln/resource/a32e0d4a-8a29-4b18-a49d-a9e1966c8c6f#{}
* Data Type: CSV Accident statistics Cologne


### Datasource 3: Mobilithek
* Metadata URL 3: https://mobilithek.info/offers/-4758259495105693759
* Data URL 3: https://offenedaten-koeln.de/sites/default/files/Radverkehr%20f%C3%BCr%20Offene%20Daten%20K%C3%B6ln%202013.csv
* Data Type: CSV Bicycle traffic data Cologne

This projects tries to draw a connections between the rate of in bicycle traffic data Cologne from the data of vehicle counting point with the road accidents statistics in cologne .

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Extract Data from the two data sources

2. Create graph

3. Draw Conclusion from the graphs

4. Calculate the occurence of accident statistics with bicycle traffic from graph


