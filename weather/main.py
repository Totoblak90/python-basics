import pandas

data = pandas.read_csv("weather_data.csv")

temp_col = data["temp"]
avg_temp_from_pandas = temp_col.mean()
print(avg_temp_from_pandas)


temp_list = temp_col.tolist()
add = 0
for temp in temp_list:
    add += temp

avg_temp_from_list = add / len(temp_list)

print(avg_temp_from_list)

print(temp_col.max())


print(data[temp_col == temp_col.max()])

monday = data[data.day == "Monday"]
monday_temp_in_c = monday.temp
monday_temp_in_f = monday_temp_in_c * 9/5 + 32
print(monday_temp_in_f)

# Create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_df = pandas.DataFrame(data_dict)
print(data_df)
data_df.to_csv("new_data.csv")
