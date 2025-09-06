# Import the required libraries for data manipulation and visualization
import pandas as pd          # pandas is used for data manipulation and analysis (e.g., handling DataFrames)
import matplotlib.pyplot as plt  # matplotlib.pyplot is used for creating visualizations like plots
import numpy as np           # numpy is used for numerical operations and array handling

# 1. Load the dataset from a CSV file into a pandas DataFrame
# - pd.read_csv("shows.csv") reads a CSV file named "shows.csv" into a DataFrame
# - The DataFrame 'shows' stores the data, where each row represents a TV show and columns represent attributes like title, year, episodes, etc.
# - Assumption: The CSV file "shows.csv" exists in the same directory as this script and has columns like 'title', 'year', and 'episodes'
shows = pd.read_csv("shows.csv")

# 2. Remove rows where the 'episodes' column has missing values (NaN)
# - dropna(subset=["episodes"]) removes rows where the 'episodes' column contains NaN (Not a Number, i.e., missing data)
# - This ensures the dataset only includes shows with valid episode counts, which is important for accurate analysis and plotting
# - The result is stored in a new DataFrame 'clean_shows'
clean_shows = shows.dropna(subset=["episodes"])

# 3. Remove duplicate rows based on the 'title' column, keeping the first occurrence
# - drop_duplicates(subset=["title"], keep="first") removes rows with duplicate values in the 'title' column
# - keep="first" ensures that only the first occurrence of each title is retained, discarding subsequent duplicates
# - This step prevents double-counting shows with the same title (e.g., due to data entry errors or multiple entries)
# - The result is stored in 'removed_duplicates'
removed_duplicates = clean_shows.drop_duplicates(subset=["title"], keep="first")

# 4. Sort the DataFrame by 'year' (ascending) and then by 'title' (alphabetically)
# - sort_values(by=["year", "title"], ascending=[True, True]) sorts the DataFrame first by the 'year' column and then by the 'title' column
# - ascending=[True, True] specifies that both 'year' and 'title' should be sorted in ascending order
# - Sorting by year ensures chronological order, and sorting by title within each year ensures alphabetical consistency
# - The sorted DataFrame is stored in 'sorted_shows'
sorted_shows = removed_duplicates.sort_values(by=["year", "title"], ascending=[True, True])

# 5. Reset the DataFrame index to a sequential range from 0 to N-1
# - reset_index(drop=True) resets the index of the DataFrame to a default integer index starting from 0
# - drop=True discards the old index (which may have become disordered due to sorting or dropping rows)
# - This ensures a clean, sequential index for the final dataset, making it easier to reference rows
sorted_shows = sorted_shows.reset_index(drop=True)

# 6. Convert the 'episodes' column to integer type
# - astype(int) converts the values in the 'episodes' column to integers
# - This is necessary because the 'episodes' column may have been read as floats (e.g., 10.0) or strings from the CSV
# - Converting to integers ensures consistent data types for calculations and avoids issues in further analysis
sorted_shows["episodes"] = sorted_shows["episodes"].astype(int)

# 7. Calculate summary statistics for the dataset
# - nunique() counts the number of unique values in the 'title' column, giving the total number of unique shows
# - This is stored in 'total_shows_overall'
total_shows_overall = sorted_shows["title"].nunique()
# - sum() calculates the total sum of the 'episodes' column, giving the total number of episodes across all shows
# - This is stored in 'total_episodes_overall'
total_episodes_overall = sorted_shows["episodes"].sum()

# 8. Group the data by 'year' to count the number of shows per year
# - groupby("year").size() groups the DataFrame by 'year' and counts the number of shows in each year
# - size() returns a Series with the count of rows (shows) for each unique year
# - reset_index(name="shows") converts the result to a DataFrame, naming the count column 'shows'
# - The resulting DataFrame 'num' has two columns: 'year' and 'shows' (the count of shows per year)
num = sorted_shows.groupby("year").size().reset_index(name="shows")

# 9. Extract years and counts for plotting
# - Extract the 'year' column as a list to use as x-axis values
years = num["year"].tolist()
# - Extract the 'shows' column (counts) as a list to use as y-axis values
counts = num["shows"].tolist()

# 10. Create a line plot to visualize the number of shows per year
# - plt.figure(figsize=(12,6)) creates a new figure with a width of 12 inches and height of 6 inches for better readability
plt.figure(figsize=(12,6))
# - plt.plot() creates a line plot with 'years' on the x-axis and 'counts' on the y-axis
# - marker="o" adds circular markers at each data point
# - linestyle="-" ensures a solid line connects the points
# - color="purple" sets the line and marker color to purple for visual appeal
plt.plot(years, counts, marker="o", linestyle="-", color="purple")

# 11. Annotate each data point with its value
# - Loop through each (x, y) pair in 'years' and 'counts'
# - plt.annotate(str(y), (x, y), ...) adds the count value (y) as text above each point
# - textcoords="offset points" and xytext=(0,10) place the text 10 points above the data point
# - ha="center" centers the text horizontally
# - fontsize=8 sets a smaller font size for the annotations to avoid clutter
for x, y in zip(years, counts):
    plt.annotate(str(y), (x, y), textcoords="offset points", xytext=(0,10), ha="center", fontsize=8)

# 12. Add a text box with summary statistics in the top-left corner
# - plt.text() adds text to the plot at the specified coordinates
# - 0.02, 0.95 are relative coordinates (0 to 1) in the axes, placing the text near the top-left
# - f"Total Shows = {total_shows_overall}\nTotal Episodes = {total_episodes_overall}" formats the text to show the total shows and episodes
# - transform=plt.gca().transAxes uses axes coordinates (relative to the plot area)
# - fontsize=10 sets the text size
# - ha="left" and va="top" align the text to the top-left of the specified coordinates
# - bbox=dict(...) adds a rounded box with a light yellow background and slight transparency (alpha=0.5) for visual distinction
plt.text(
    0.02, 0.95,  # relative coordinates (0-1)
    f"Total Shows = {total_shows_overall}\nTotal Episodes = {total_episodes_overall}",
    transform=plt.gca().transAxes,  # use axes coordinates
    fontsize=10,
    ha="left",
    va="top",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.5)
)

# 13. Add a grid to the plot for better readability
# - plt.grid(True, linestyle="--", alpha=0.6) adds a dashed grid with 60% opacity
# - The grid helps viewers visually align data points with the axes
plt.grid(True, linestyle="--", alpha=0.6)

# 14. Set axis labels and title
# - plt.xlabel() sets the x-axis label to "Year" with a font size of 12
plt.xlabel("Year", fontsize=12)
# - plt.ylabel() sets the y-axis label to "Number of Shows" with a font size of 12
plt.ylabel("Number of Shows", fontsize=12)
# - plt.title() sets the plot title to "TV Shows Aired per Year" with a bold font and size 14
plt.title("TV Shows Aired per Year", fontsize=14, fontweight="bold")

# 15. Customize the x-axis ticks
# - np.arange(min(years), max(years)+1, 5) creates an array of years from the minimum to the maximum year, with a step of 5
# - This ensures that x-axis ticks are shown at 5-year intervals for clarity
# - rotation=45 rotates the x-axis labels by 45 degrees to prevent overlap and improve readability
plt.xticks(np.arange(min(years), max(years)+1, 5), rotation=45)

# 16. Display the plot
# - plt.show() renders the plot and displays it to the user
# - This is the final step to visualize the line plot with all the configured settings
plt.show()