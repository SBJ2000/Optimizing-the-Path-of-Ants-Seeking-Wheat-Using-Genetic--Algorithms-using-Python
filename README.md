# Optimizing the Path of Ants Seeking Wheat Using Genetic  Algorithms using Python
![Project Logo](https://github.com/SBJ2000/Optimizing-the-Path-of-Ants-Seeking-Wheat-Using-Genetic--Algorithms-using-Python/blob/main/Images/Logo.jpg)

## Introduction

 This project explores the use of genetic algorithms to optimize the paths of ants in a simulated environment. The objective is to develop an algorithm that evolves ant behavior to efficiently find wheat, overcoming obstacles in the process

## Objectives

* Implement a simulation environment with ants, wheat, and obstacles.
* Create a genetic representation of ant behavior in the form of genes.
* Use genetic algorithms to evolve ant strategies for optimizing the path to wheat.
* Analyze the results to evaluate the effectiveness of the genetic algorithm in solving the problem.

## Work Environment

The project was developed using the Python programming language, with the Pygame library employed to create an interactive simulation environment that includes ants, wheat, and obstacles, resembling a small ant game.

## Solution Coding
The code is organized into three main parts: the DNA class, the Ant class, and the Population class. These classes interact to simulate the evolution of ants seeking wheat.

### DNA Class
This class represents the genes of ants. Genes are vectors that define the direction of the ant’s movement at each stage of its life. The DNA class includes methods for the random creation of genes, crossover with another set of genes, and the possibility of mutation.

* Genes are represented as two-dimensional vectors. Each component represents the force applied by the ant in a specific direction.
* The genes of selected parents are crossed to create offspring, inheriting characteristics from both parents.
* A small mutation probability of 0.01 is introduced to ensure a wider exploration of the solution space.

### Ant Class
Each ant has an instance of the DNA class that determines its behavior. The Ant class has methods to apply force, update the ant’s position, calculate its fitness, and display its image.

* The fitness of each ant is evaluated based on its distance from the wheat. Bonuses or penalties are applied depending on whether the ant reaches the wheat or collides with obstacles.

### Population Class
This class represents the total ant population. It contains a list of instances of the Ant class and manages the evolution of the population through selection, crossover, mutation, and fitness evaluation.

* Ants are selected for breeding according to their fitness. The most successful ants have a greater chance of being selected.

## Main Program Structure

The main program includes five key elements:

1- Visual Interface:

Using Pygame to create a graphical interface makes the evolution process of ants and their quest towards wheat intuitive and visually appealing. Images of ants, wheat, and obstacles add an interactive aspect to the simulation.

2- Main Loop: 

The main loop handles Pygame events, refreshes the display at each iteration, and ensures smooth communication between the user and the simulation. It indicates each generation’s performance in relation to reaching the wheat and the final position of each ant in the generation.

3- Information Display: 

The display includes the number of generations, general fitness, and, at the end of the treatment, the best fitness function compared to all generations. This helps identify the best positions ants achieved with the genetic algorithm.

* The program stops in two cases: either the maximum number of generations is reached (the most likely case), displaying the best fitness function result of all generations, or all ants reach the wheat (a very rare case due to the lengthy process of iterating through thousands of generations).

4- Evaluation and Selection:

The evaluate method in the Population class is called at the end of each generation, calculating the fitness of each ant and preparing the population for the next generation. Selection and crossover are key steps in improving successive generations.

5- Best Result Display: 

The best general fitness of all generations is displayed at the end of the simulation, providing a clear indication of the overall performance of the genetic algorithm in solving the specific problem.

## Display and View
* The show method in the Ant class displays the image of each ant at its current position in the environment.
* The Pygame display shows the simulation environment, including obstacles, wheat, and ants, for interactive visualization.

## Parameters and Adjustments

Parameter adjustments such as population size, ant lifespan, and mutation probability can influence the overall performance of the genetic algorithm.

## Results and Tests

The results of this project are demonstrated in a short video, which can be accessed via the repo of this project. The video clearly shows the different stages of testing the program and the succession of generations.

Significant improvement in ant performance was observed over generations, with the general fitness of the population increasing, indicating successful adaptation to the problem's constraints.



## Conclusion

In conclusion, this project demonstrates the effectiveness of genetic algorithms in optimizing complex behaviors, such as the navigation path of ants. The results obtained open the door to potential applications of this approach in similar fields.