![image](https://github.com/FrancoMuVa/holbertonschool-AirBnB_clone/assets/85513647/53e71b61-9690-4592-bf3e-82f7a5d86541)


# AirBnB clone: The console
This project is the first step towards building our own simple copy of the Airbnb website.


## The console
This is a command interpreter limited to a specific use-case to manage our AirBnB objects. 
In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object
## Installation

To use this console, follow these steps:

1. Clone this repository to your local machine:
```bash
  git clone https://github.com/FrancoMuVa/holbertonschool-AirBnB_clone.git
```

2. Run the program:
```bash
python3 console.py
```

3. Once the console is running, you can enter commands. The program will display the output of the commands and will wait for you to enter a new command.

**Example in interactive mode:**
```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```
**Example in non-interactive mode:**
```bash
echo "create BaseModel" | python3 console.py
(hbnb)
49faff9a-6318-451f-87b6-910505c55907
```
## Available commands

| Command | Functionality |
|-------------|-------------|
| create | Creates a new object of a specified class (BaseModel, User, Place, State, Review, City and Amenity) and prints the instance id |
| show | Shows the content of a specified object, takes name of the class and its respective instance id|
| destroy | Removes specified object, takes name of the class and its respective instance id|
| all | Displays all existent objects or the ones of a specified class|
| update | Updates attribute values of a specified object, taking class name and its respective instance id|
| quit | Exits the console|

## Running Tests

To run tests, run the following command

```bash
  python3 -m unittest discover tests
```


## Authors
This project was created by Holberton School Uruguay students:
- [@FrancoMuVa](https://www.github.com/FrancoMuva)
- [@FabianaTellechea](https://www.github.com/fabianatellechea)
