# 🎮 Adam's Benchmark Game
## 📜 Introduction
Hello, I'm Adam! 👋 Thank you for taking your time to read this. I've wanted to create my own personal project for quite a while now, but studies has kept me very busy. Finally, during my reading week, I embarked on this journey and crafted my first ever personal project. Over the past year, university projects introduced me to the world of game development using Python and Java. So, why not make my own? 🚀

**This project is the first step in my journey to discovering myself in the world of programming and computer science!** 🌍💡

## Overview
This repository contains the files of my very own game, "Adam's Benchmark Game", which is written completely in Python 3.9. 🐍 Additionally, this repository contains a text file containing over 370,000 words sourced from [this repository.](https://github.com/dwyl/english-words) 

The game is a trio of minigames:
1. 🚦 Reaction Game
2. 🔢 Number Game
3. 📚 Verbal Game

### 🚦 Reaction Game
**How to play:**
1. Click the main button to kick things off.
2. Hold tight for a random interval.
3. As soon as the button turns green, click it!
4. Boom! Your reaction time is displayed

*Notes*:
- Used the `time` library for timing magic.
- Crafted a `ReactionGame` class to manage the game's mechanics.

### 🔢 Number Game
**How to play:**
1. Click on the textbox and type "start" to initiate the game.
2. A number will flash on the screen for a bit, memorize that number.
3. Once it vanishes, jot down the number.
4. Nail it, and your score ticks up. Miss it, the game restarts and the score resets.

*Notes*:
- The `time` library helps in showing numbers for a set duration.
- The `random` class conjures up numbers to challenge you.
- The bigger the number, the longer it will stay on screen.
- A `NumberGame` class manages the game's flow.

### 📚 Verbal Game
**How to play:**
1. A word pops up. If it's a déjà vu, click "new"; else, "shown".
2. Get it right, and your score climbs. Slip up, and it's back to square one.

*Notes*:
- To program this game I used the `random` class to shuffle the words on screen before they appear.
- A game restart brings a fresh set of words to the table.
- The `VerbalGame` class is the brain behind the game.
- Word list sourced from [this repository.](https://github.com/dwyl/english-words) 

## 💡 Inspiration
This entire game draws inspiration from [Human Benchmark.](https://humanbenchmark.com/)

One day, while benchmarking my human skills with friends, a thought struck - could I recreate these minigames? Writing down ideas and leveraging my Python skills, I found pockets of time and brought this game to life. 🌟

Enjoy! 😁
