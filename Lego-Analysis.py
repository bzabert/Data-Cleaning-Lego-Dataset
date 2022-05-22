import pandas as pd

# Creating DataFrame for each Data Set
df_lego = pd.read_csv(
    "/Users/bzabert/Documents/Portfolio/Python/Lego Analysis/datasets/lego_sets.csv"
)
df_theme = pd.read_csv(
    "/Users/bzabert/Documents/Portfolio/Python/Lego Analysis/datasets/parent_themes.csv"
)

# Rename the key columns in order to have the same name
df_theme.rename(columns={"name": "parent_theme"}, inplace=True)

# Merging both DF
df_lego_merged = df_lego.merge(df_theme, on="parent_theme")

# Taking out the NaN and duplicates for the column 'set_num'
df_lego_merged = df_lego_merged.dropna(subset=["set_num"], inplace=False)
df_lego_merged = df_lego_merged.drop_duplicates(subset=["set_num"])

# Creating a DF for the Star Wars set and the licensed set
star_wars_set = df_lego_merged[df_lego_merged["parent_theme"] == "Star Wars"]
licensed_theme = df_lego_merged[df_lego_merged["is_licensed"] == True]

val_star_wars_set = star_wars_set["set_num"].count()
val_licensed_theme = licensed_theme["set_num"].count()

# Calculating the percentage of the Star Wars set over the licensed
the_force = int(val_star_wars_set / val_licensed_theme * 100)
print(the_force)

# -------------------------------------------------------------------------------------------------

# Crating a column for counting in the licensed DF
licensed_theme["count"] = 1

# Grouping by the year and the parent theme and sorting descending order
licensed_theme_group = pd.DataFrame(
    pd.DataFrame(
        licensed_theme.groupby(["year", "parent_theme",])["count"].sum().reset_index()
    )
)
licensed_theme_group = licensed_theme_group.sort_values(
    ["year", "count"], ascending=False
).reset_index()

# Creatung a DF only for the max row of each year
max_theme_by_year = licensed_theme_group.drop_duplicates(["year"])

# Taking the year in which Star Wars was not  sold theme.
year_not_satr_wars = max_theme_by_year[max_theme_by_year["parent_theme"] != "Star Wars"]
new_era = int(year_not_satr_wars.iloc[0]["year"])
print(new_era)

# -------------------------------------------------------------------------------------------------

# Searching for the year with the most set realized
df_lego_merged = df_lego.merge(df_theme, on="parent_theme")
df_lego_merged["count"] = 1
df_lego_merged.groupby(["year"])["count"].sum().sort_values(ascending=False)

