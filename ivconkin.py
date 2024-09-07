import matplotlib.pyplot as plt

# Line Graph
x=[1, 3, 5, 7, 9, 24]
y=[2, 4, 6, 1, 10, 36]
plt.plot(x, y)
plt.xlabel('X numbers')
plt.ylabel('Y numbers')
plt.title("Isaac's data test graph")
plt.show()


# Bar Graph
data = {'C':20, 'C++':15, 'Java':30, 'Python':35}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='maroon', width = 0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()