Name: Mauricio Canales, Parth Gupta, Sungsoo Kim 
Data Source: Austin B Cycle Data (2014) 
Project Description:

Overview

This API will enable the user to review B-Cycle usage, including usage dates, travel time, and docking locations, in the City of Austin from October 26th, 2014 onwards. 

The API specification is RESTful in that it uses HTTP methods (GET, POST, PUT, and DELETE) to interact with the allocations database. The HTTP responses are always in JSON format. 

API Specifications 
List all data: kiosk id,address,duration of trip,date 
List specific data of all trips at given interval, given start and end times
Find the average trip time of a given month 
Create a graph of the data: average time of trip for given interval month
Add new ride information 
	Potentially
Use kiosk id to map the volume of how much the station is being used



(Copied from example website, the API specs. This is just a rough draft, please feel free to edit)

GET /kiosk
Gets all docking information from all kiosks

GET /kiosk/<kioskid>
Gets address of and dockings at a specific kiosk

GET /kiosk/<kioskid>/<date>
Gets info about all dockings at specific kiosk on specific date

GET /kiosk/<kioskid>/<date>/<time>
Gets info about dockings at a specifc kiosk on specific data at specific time



GET /average_time/<date_interval> ]
Gets the average time of trip per month given a date interval. 

GET /


Instructions


Chargeable Components 
The first hundred queries per month are free, after that we charge a certain amount per 1000 queries.
Don’t charge per query, charge per bandwidth
