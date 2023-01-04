# Airplane seat reservation system - Snakes on a Plane
***
In this project we coded a website that can be used to reserve seats 
on different imaginary flights.
## Table of content
***
1. [General Info](#general-info)
2. [Admin Info](#admin-info)
3. [Installation](#installation)
4. [Requirements](#requirements)
5. [Running The App](#running-the-app)

## General Info
***
This Flask and Python based webpage can be used for the reservation of
seats on imaginary flights. Users can sign up with their email, name, birtdate
and a passwort in order to create an account. Afterwards users can reserve or
cancel seats after choosing a flight via the booking-system page of the website.
Reserving and cancelling flights is possible via clicking on the requested seat.
A popup will ask for confirmation of the reservation or cancellation of a seat
before executing the request.
## Admin Info
***
New flights can be added by providing chartIn.txt 
files in the Input_Data folder inside the project folder. <br>
The admin of this webpage can acquire statistical output in form 
of a Statistics.txt file. Statistical output is saved in the Output_Data 
folder inside the project folder. The statistical output contains the percentage 
of occupied seats and the percentage of available seats over all available 
flights. Furthermore, a list of all occupied and all available seats can be 
found inside the statistical output. <br>
Every time a user logs out of the system or every time the user asks for the 
statistical data in the admin are of our webpage, the statistical output is 
updated and the newest version of statistical data is appended to the 
statistics.txt file. <br>
The admin can change the email, name and role of a user in the user area 
inside the admin area. Changing the role of a user can be used 
in order to change a users role from user to admin. An admin can also delete 
users. In case a user has reserved seats, the reserved seats will be made available
again when the admin deletes the respective user. <br>
Inside the seats area of the admin area the admin can change the user associated
with a reserved seat in order to reserve a seat for a user or to manually cancel
a reserved seat. In the latter case, the seat will become available again.
## Installation
***
You can clone this repository using the following shell command.
```
$ git clone <https://github.com/maiteboehm/snakes_on_a_plane>
```
## Requirements
***
The project was created using Pyton 3.11. Please, make sure you have the latest
version of Python installed. <br>
All other required Python Packages can be found in the requirements.txt <br>
```
$ pip install -r requirements.txt
```
## Running The App
***
You can run the app by using the following shell command in the website folder 
of our project folder.
```
$ python main.py
```







