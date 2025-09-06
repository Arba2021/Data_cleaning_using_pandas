My First Data Science Project: TV Shows Analysis
Overview

This is my first data science project. I worked with a CSV file (shows.csv) containing TV shows data, cleaned it, and visualized the number of shows aired per year. This project helped me learn how to work with data, clean it, and create simple plots in Python.

The dataset has:

title – TV show name

year – Year the show aired

episodes – Number of episodes

What I Learned

Reading CSV files with pandas

Cleaning data (removing missing values and duplicates)

Sorting and converting data types

Grouping data and simple analysis

Creating line plots with matplotlib

Annotating plots and showing totals

Features

Remove rows with missing episodes

Remove duplicate titles

Sort shows by year and title

Convert episodes to integers

Count total shows and episodes

Show number of shows per year in a line plot

Display a summary box with total shows and episodes

Requirements

Python 3

Libraries: pandas, matplotlib, numpy

Install with:

pip install pandas matplotlib numpy

Files

shows.csv – CSV file with TV shows data

tv_shows_analysis.py – Python script for analysis and plotting

How to Use

Put shows.csv in the same folder as the script.

Run the script:

python tv_shows_analysis.py


The plot will show:

Number of shows per year (line plot)

Markers with number of shows

Summary box with total shows and episodes

X-axis years at 5-year intervals

You can also save the plot by adding:

plt.savefig("tv_shows_plot.png")


before plt.show().

Notes

Make sure shows.csv exists and the data is valid.

The script converts episodes to integers automatically.

You can customize colors, figure size, and fonts in the script.

Future Improvements

Add error handling for missing or invalid CSV files

Add more charts (bar chart, histogram)

Analyze more columns (genres, ratings)

About Me

This is my first project in data science, learning Python, pandas, and visualization. Feedback and suggestions are welcome!
