# SelfQuant Outline

## Overview
- ### What is SelfQuant?
  - SelfQuant is a quantified self dashboard that allows you to track your daily activities and visualize them in a 
    meaningful way.
    - This means that everything from health data to screen time will be tracked in a single dashboard.
    - Analysis will take place locally, determining correlations between all of your metrics on-device, for privacy, 
      convenience, and cost-efficiency.
      - The goal here is to have data processed efficiently enough to be able to run on a mobile device or Raspberry Pi.

## Features
- ### Importing data from other sources
  - SelfQuant will be able to import data from other sources, such as Apple Health and Screen Time, ActivityWatch, etc.
    - This will allow you to have a single dashboard for all of your data, rather than having to use multiple apps.
    - This will also allow you to have a single source of truth for your data, rather than having to trust multiple 
      apps and keep track of them all.

- ### Calculating correlations between metrics
  - SelfQuant will be able to calculate correlations between all of your metrics, allowing you to see how your 
    activities affect each other.
    - This will allow you to see how your sleep affects your productivity, or how your screen time affects your 
      sleep, etc.
    - This will also allow you to see how your activities affect your mood, and vice versa.

- ### Visualizing data
  - The thought behind data visualization is that it'll be much easier for the user to digest in a simplistic and 
    elegant format. Both visualization and using plain English, possibly derived from a machine learning model, will 
    help clarify the results of the analysis to the user.

______________________________

# Code Outline

## Main Functionality Overview
- Data Import
  - Data Syncing from other sources
  - Potentially built-in desktop/mobile tracking?
- Data Analysis
- Visualization
- User Interface
- Data Storage (SQL?)
- Language Model
- Machine Learning Model (self-learning)
  - Create a baseline from the user's data and then use that to predict future data
 
## Other Functionality
- Notifications when a metric hasn't been updated in a while?
- Possible work tracking

TODO:
- [ ] Make note of all health metrics and algorithms to calculate
- [ ] Figure out where to fit in the machine learning model
- [ ] Determine whether I'll use R at all
- [ ] Create files for each of the above sections
