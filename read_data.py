import pandas as pd

# Define the path to your Excel file
#TODO: Add path to your Excel File
excel_file = ""

# Define the sheet name for "Order details KB"
sheet_name_order_details = "Order details KB"

# Define the range of columns to read for the required number of stevedores (G3-G5)
stevedores_column = "G"

# Read the required number of stevedores from the Excel sheet
required_stevedores = pd.read_excel(excel_file, sheet_name=sheet_name_order_details, usecols=stevedores_column,
                                   skiprows=[0])

# Remove NaN values (if any)
required_stevedores = required_stevedores.dropna()

# Convert the Pandas DataFrame to a list
required_stevedores_data = required_stevedores.values.flatten().tolist()
n = required_stevedores_data

# Print the required number of stevedores
print("Required Number of Stevedores:")
print(required_stevedores_data)

# Define the sheet names for Order 1, Order 2, and Order 3
sheet_names = ["Order 1", "Order 2", "Order 3"]

# Define the start rows for each order
start_rows = [4, 4, 4]

# Define the range of columns to read for worker preferences and resilience (adjust these as needed)
worker_columns = "M"
central_allocation_columns = "L"

# Create lists to store data for worker preferences and central_allocation for all orders
worker_pref_data = []
central_allocation = []

for sheet_name in sheet_names:
    # Read worker preference data from the Excel sheet
    worker_data = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=worker_columns,
                                skiprows=range(1, start_rows[sheet_names.index(sheet_name)]))

    # Read resilience data from the Excel sheet
    central_data = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=central_allocation_columns,
                               skiprows=range(1, start_rows[sheet_names.index(sheet_name)]))

    # Remove NaN values (if any) for both data types
    worker_data = worker_data.dropna()
    central_data = central_data.dropna()

    # Convert Pandas DataFrames to lists and append them to the respective lists
    worker_pref_data.append(worker_data.values.flatten().tolist())
    central_allocation.append(central_data.values.flatten().tolist())

worker_pref_data1 = worker_pref_data[0]
worker_pref_data2 = worker_pref_data[1]
worker_pref_data3 = worker_pref_data[2]

central_allocation1 = central_allocation[0]
central_allocation2 = central_allocation[1]
central_allocation3 = central_allocation[2]

# Clear the lists for reusing them
worker_pref_data = []
central_allocation = []

# Use a loop to append the list 'n' times
for i, count in enumerate(n):
    if i == 0:
        # Append list1 'count' times
        for _ in range(count):
            worker_pref_data.append(worker_pref_data1)
            central_allocation.append(central_allocation1)
    elif i == 1:
        # Append list2 'count' times
        for _ in range(count):
            worker_pref_data.append(worker_pref_data2)
            central_allocation.append(central_allocation2)
    elif i == 2:
        # Append list3 'count' times
        for _ in range(count):
            worker_pref_data.append(worker_pref_data3)
            central_allocation.append(central_allocation3)


# Print the separated data for worker preferences and central_allocation
# print("Worker Preferences for All Orders:")
filtered_central_allocations = []

for data in central_allocation:
    # Filter out "RULES (BOC)" if it's present in the list
    filtered_data = [item for item in data if item != 'RULES (BOC)']
    filtered_central_allocations.append(filtered_data)

print(filtered_central_allocations)



# # Print the separated data for worker preferences and central_allocation
# print("Worker Preferences for All Orders:")
# for data in central_allocation:
#     print(data)


# print("Duplicated Preferences for All Orders:")
# # Duplicate and add duplicates behind their original lists
# for i in range(len(worker_pref_data)):
#     if i == 0:
#         for _ in range(n[0]-1):
#             worker_pref_data.insert(1, worker_pref_data[i])
#             resilience_data.insert(1, worker_pref_data[i])
#         print(worker_pref_data)
#
#     elif i == 1:
#         x = n[0]
#         y = n[0] + 1
#         print(y)
#         for _ in range(n[1]-1):
#             worker_pref_data.insert(x, worker_pref_data[y])
#             resilience_data.insert(x, worker_pref_data[y])
#     # else:
#     #     worker_pref_data.extend([worker_pref_data[i]] * n[2])
#     #     resilience_data.extend([resilience_data[i]] * n[2])
#
# # print(worker_pref_data)

# # Print the separated data for worker preferences and resilience
# print("Worker Preferences for All Orders:")
# for data in worker_pref_data:
#     print(data)
#
# # print("Resilience Data for All Orders:")
# # for data in resilience_data:
# #     print(data)
#
# # print(worker_pref_data)
# # print(resilience_data)
#
