# import pandas as pd

# squirrel_df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# grey_squirrels_count = len(squirrel_df[squirrel_df["Primary Fur Color"] == "Gray"])
# black_squirrels_count = len(squirrel_df[squirrel_df["Primary Fur Color"] == "Black"])
# cinnamon_squirrels_count = len(squirrel_df[squirrel_df["Primary Fur Color"] == "Cinnamon"])

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
# }

# df = pd.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

import pandas as pd

squirrel_df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Filtrar el DataFrame para excluir las filas donde fur_color es 'false'
filtered_df = squirrel_df[squirrel_df['Primary Fur Color'] != 'false']

squirrels_by_colors = filtered_df['Primary Fur Color'].value_counts()

squirrels_by_colors.to_csv("squirrel_count.csv")