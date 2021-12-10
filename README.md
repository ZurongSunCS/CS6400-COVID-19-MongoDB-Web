# CS6400-COVID-19-MongoDB-Web

#SET UP STEP

For out project, we use Ubuntu 20.04 and Visual Studio Code.

In order to successfully deploy this application, you have to do the following.

sudo apt update

sudo apt install python3-pip

sudo apt install python3-virtualenv

pip install flask pymongo passlib numpy pandas

sudo apt install python3-flask

sudo apt-get install python-dnspython

pip3 install pymongo[srv]

1. To run the separate D3 file, in the terminal type "cd covid", and then "python3 -m http.server 8005 &". This allows you to access D3 graph in the New York Time pages
2. To run our application, in the root terminal, type "virtualenv -p python3 env" (This may be not necessary)
3. Then type "source env/bin/activate"
4. Finally type "./run" to run our application

Go to localhost:5000

We have 9 dashboards which contain 22 graphs. There are line graph, bar graph, the combination of line graph and bar graph, map graph and treemaps. The user can check confirmed_cases, death_cases, recovery_cases, # of people who are tested, Mortality. 
