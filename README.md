# Adam's Benchmark Game
## Introduction
Hello, I'm Adam! Thank you for taking your time to read this. I've wanted to create my own personal project for quite a while now, but studies has kept me very busy. Finally I have created my first ever personal project. For the past year, I have had many university projects that required me to make simple games using both Python and Java, so I decided to make my own during my reading week.

**This project is the first step in my journey to discovering myself in the world of programming and computer science!**

## Overview
This repository contains the files of my very own game, "Adam's Benchmark Game", which is written completely in Python 3.9 (using the pygame library). Additionally, this repository contains a text file containing over 370,000 words which is taken from [this repository.](https://github.com/dwyl/english-words) 

This game contains 3 minigames:
1. Reaction Game

2. Number Game

3. Verbal Game

### Reaction Game
How to play:
1. Click on the main large button to start the game.
2. Wait some random (pseudorandom) interval of time.
3. When the button turns green, click as fast as you can.
4. Display the reaction time.

*Notes*:
- To program this minigame I used the `time` library to record the intervals of time between events.
- I designed a class called `ReactionGame` that manages the internal workings of the reaction game.

### Number Game
How to play:
1. Click on the textbox and write "start" to initiate the game.
2. A number will pop up on screen for a certain amount of time, memorize that number.
3. Once the number is gone, write down the number that was shown on screen.
4. If you get it correct, your score increases by 1. If you do not get it correct, the game restarts and the score resets.

*Notes*:
- To program this minigame I used the `time` library to show the numbers for a set amount of time.
- I also used the `random` class to calculate a random number in a certain boundary to display on screen.
- The bigger the number, the longer it will stay on screen.
- I designed a class called `NumberGame` that manages the internal workings of the number game.

### Verbal Game
How to play:
1. A random word will show up on the screen, if the word has been shown before, click new; otherwise, click shown.
2. If you get it correct, your score increases by 1. If you do not get it correct, the game restarts and the score resets.

*Notes*:
- To program this game I used the `random` class to shuffle the words on screen before they are presented.
- If the game restarts, the set of words that show on the screen will be different.
- I designed a class called `VerbalGame` that manages the internal workings of the verbal game.
- The set of words that are shown are taken from [this repository.](https://github.com/dwyl/english-words) 


## Inspiration
This entire game was hevaily inspired by [Human Benchmark.](https://humanbenchmark.com/)

Basically, I was on this Human Benchmark with a couple of friends and I was wondering if I could program the minigames on my own. So I wrote down the ways that I could program this using my prior knowledge in Python and OOP/Class-based programming. 

Finally, I found slots of time where I could program the game, and alas, I did it.
