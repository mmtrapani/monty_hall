# Author: Matt Trapani
# Date: 9/19/19
"""
The Monty Hall Simulation plans to run a simulation of the well known Monty Hall problem. The program will take the number of simulations from the user
and run that number of times. The user has the choice of always switching, or always staying with their original choice. The program will total the number
of wins and plot both wins and loses on a pie chart.
"""
import random
import matplotlib.pyplot as plt

class MontyHall:
  def __init__(self):
    self.num = 0                                  # defines the number of iterations
    self.preference = 0                           # defines the preference of the simulation switch after first door is revealed
    self.counter = 0                              # record number of times contestant wins
    self.labels = []
    self.sizes = []
    self.colors = ['lightskyblue', 'lightcoral']

  def num_iterations(self):
    while self.num < 1:
      try:
        self.num = int(input("Enter the number of Monty Hall simulations (> or = to 1) that you would like to run: "))
      except ValueError:
        print("Please enter an integer for the number of simulations that you would like to run: ")

  def switch_pref(self):
    while self.preference < 1 or self.preference > 2:
     try:
       self.preference = int(input("Enter '1' if you would like the simulation to always switch from its initial choice or '2' if you would like it to stay with its original choice: "))
     except ValueError:
       print("You must enter a valid integer.")

  def play(self):   
    if self.preference == 1:
       for i in range(self.num):
          self.chosen_door = random.randint(1,3)        # set contestant door to random integer 1 to 3 inclusive
          self.winning_door = random.randint(1,3)       # set winning door to random integer 1 to 3 inclusive

          if self.winning_door != self.chosen_door:
            self.counter += 1

    else:
      for i in range(self.num):
          self.chosen_door = random.randint(1,3)
          self.winning_door = random.randint(1,3)
          if self.winning_door == self.chosen_door:
            self.counter += 1
    print('There were a total of ' + str(self.counter) + ' wins out of a total ' + str(self.num) + ' games.')

  def displayPieChart(self):
    #data to plot
    self.labels = ['Wins', 'Loses']
    self.sizes = [self.counter, self.num - self.counter]
    # plot
    plt.pie(self.sizes, labels = self.labels, colors = self.colors, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

monty = MontyHall()
monty.num_iterations()
monty.switch_pref()
monty.play()
monty.displayPieChart()
            
