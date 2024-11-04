import matplotlib.pyplot as plt

def show_histogram(data, nameOx, nameOy, title):
    plt.figure(figsize=(12, 6))
    plt.bar(data.index, data.values, color='skyblue', edgecolor='black')
    plt.xlabel(nameOx)
    plt.ylabel(nameOy)
    plt.title(title)
    plt.xticks(rotation=90) 
    plt.tight_layout()  
    plt.show()