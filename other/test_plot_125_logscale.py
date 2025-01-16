import numpy as np
import matplotlib.pyplot as plt

# vals = [0.1, 0.2, 0.5, 1, 2, 5, 10]
vals = [ 0.1, 0.2, 0.5, 1, 2, 5, 10]

# Sample data
categories = [str(val) + 's' for val in vals]
values = list(range(1, len(categories) + 1))

# Define the logarithmic positions for each category
log_positions = np.log10(vals)

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Create bar plot with equal width
bar_width = 0.2  # Width of each bar
plt.bar(log_positions, values, width=bar_width, color='blue', alpha=0.7)

# Set x-axis ticks to follow the original values (not logarithmic)
plt.xticks(log_positions, categories)

# Add additional ticks for clarity
additional_ticks = np.arange(0.1,1.1,0.1)
additional_ticks = np.concatenate((additional_ticks, np.arange(2,11,1)))
plt.xticks(np.log10(additional_ticks), rotation=0)

# Adding labels and title
plt.xlabel('Time (seconds)')
plt.ylabel('Values')
plt.title('Bar Plot with Equal Width Bars and Logarithmic Progression on X-axis')

# Add grid lines for both axes
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.grid(axis='x', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()






# import numpy as np
# import matplotlib.pyplot as plt

# # Sample data
# # Define the categories (for example, time intervals)
# categories = ['0.1s', '0.2s', '0.5s', '1s', '2s', '5s', '10s']
# # Sample values for each category (can be any data you want to represent)
# values = [1, 3, 2, 5, 4, 6, 7]

# # Create a figure and axis
# plt.figure(figsize=(10, 6))

# # Create bar plot
# plt.bar(categories, values, alpha=1, zorder = 10)

# # Set x-axis to a logarithmic scale with 1-2-5 progression
# plt.xscale('log')

# # Customizing the ticks to follow the 1-2-5 progression
# ticks = [0.1, 0.2, 0.5, 1, 2, 5, 10]
# plt.xticks(ticks, labels=[f'{tick:.1f}' for tick in ticks])

# # Adding labels and title
# plt.xlabel('Time (seconds)')
# plt.ylabel('Values')
# plt.title('Bar Plot with 1-2-5 Logarithmic Progression on X-axis')
# plt.grid(axis='both', linestyle='--', linewidth=0.5, zorder = -10)

# # Show the plot
# plt.show()
