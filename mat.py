import numpy as np
import matplotlib.pyplot as plt


# print(np.empty(3))
# print(np.array([3.14, 42.]))
# print(np.arange(5))
# print(np.array([0,1,2,3]))
# x=np.array([[1,2],[3,4]])
# y=np.array([[5,6]])
# print(np.concatenate((x,y), axis=0))


# 1.
time = [0, 1, 2, 3, 4, 5]
temperature = [22, 24, 25, 28, 30, 32]
plt.figure(figsize=(5, 3))
plt.plot(time, temperature, marker='o')
plt.title('Time vs Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.grid(True)
plt.show()

# 2. 
genres = ['Fiction', 'Non-Fiction', 'Sci-Fi', 'Fantasy']
books_sold = [50, 40, 35, 25]
plt.figure(figsize=(5, 3))
plt.bar(genres, books_sold, color='skyblue')
plt.title('Books Sold by Genre')
plt.xlabel('Genre')
plt.ylabel('Books Sold')
plt.show()

# 3. 
ages = [25, 32, 40, 60, 22, 35, 27, 29, 52, 45]
plt.figure(figsize=(5, 3))
plt.hist(ages, bins=5, color='lightgreen', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 4. 
labels = ['Apple', 'Samsung', 'Huawei', 'Others']
shares = [45, 30, 15, 10]
colors = ['red', 'blue', 'green', 'gray']
plt.figure(figsize=(5, 5))
plt.pie(shares, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Tech Company Market Share')
plt.axis('equal')
plt.show()

# 5. 
x_vals = [1, 2, 3, 4, 5, 6, 7]
y_vals = [3, 5, 7, 2, 6, 8, 9]
plt.figure(figsize=(5, 3))
plt.scatter(x_vals, y_vals, color='purple')
plt.title('Scatter Plot Example')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.grid(True)
plt.show()
