import pandas as pd


# Read file csv
print ("...Reading file.csv")
csv = pd.read_csv("path/file.csv")

# Convert from CSV to PICKLE
print ("...Converting: file.csv -> file.pkl")
csv.to_pickle("path/file.pkl") # if file pkl exist, write dât in file. If not, create new file pkl and write

# Read file pkl
print ("...Reading file.pkl")
pkl = pd.read_pickle("path/file.pkl")
print(pkl)

print ("...Done")