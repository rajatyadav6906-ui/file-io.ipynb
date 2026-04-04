import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Data_analysis:
 def __init__(self):
  pass
 def load_dataset(self):
  print("Load dataset")
  self.file_name = input("Enter the path of the data set: ")
  self.data = pd.read_csv(self.file_name)
  print(self.data)
  print("dataset loaded successfully")
  
 def Display_the_frist_5_rows(self):
   print("=====Display the frist 5 rows=====")
   self.rows = (self.data.head(5))
   print(self.rows)

 def Display_the_last_5_rows(self):
  print("=======Display the last 5 rows========")
  self.last_rows = (self.data.tail(5))
  print(self.last_rows)

 def Display_the_column_name(self):
  print("=======Column name ======")
  self.Column_name = (self.data.columns)
  print(self.Column_name)
  

 def bar_plot(self):
  print("============bar plot===========")
  print("available columns: ",self.data.columns.tolist())

  self.x_col = self.data.columns()
  self.y_col = self.data.columns()
  plt.show()

 
  

da = Data_analysis()

class Explore_Data:
 def __init__(self):
  pass
while True:
 print("===============Data Analysis & Visualization Program====================")
 print("Plase select an option: ")
 print("1. Load Dataset")
 print("2. Explore Data")
 print("3. Perform Dataframe Operation")
 print("4. Handle Missing Data")
 print("5. Generate Discriptive Statistics")
 print("6. Data Visualization")
 print("7. Save Visualization")
 print("8. Exit")

 choice = int(input("Enter your choice: "))
 match choice:
  case 1:
   da.load_dataset()
  case 2:
   while True:
    print("=======Explore Data========")
    print("1. Display the frist 5 rows")
    print("2. Display the last 5 rows")
    print("3. Display column names")
    print("4. Display data type")
    print("5. Display basic info")
    print("6. back to main menu")
     
    sub_choice = int(input("Enter your choice: "))
    match sub_choice:
     case 1:
      da.Display_the_frist_5_rows()
     case 2:
      da.Display_the_last_5_rows()
     case 3:
      da.Display_the_column_name()
     case 4:
      pass
     case 5:
      pass
     case 6:
      break
  case 3:
   pass
  case 4:
   while True:
    print("========Handle missing data=========")
    print("1. Display rows with missing values ")
    print("2. Fill missing values with mean")
    print("3. Drop rows with missing values")
    print("4. Replase missing values with a specific value")
    print("5. back to main menu ")

    sub_choice = int(input("Enter your choice: "))
    match sub_choice:
     case 1:
      pass
     case 2:
      pass
     case 3:
      pass
     case 4:
      pass
     case 5:
      break
  case 5:
   pass
  case 6:
   while True:
    print("======Data visualization ============")
    print("1. Bar plot")
    print("2. Line plot")
    print("3. Scatter plot")
    print("4. pie chart")
    print("5. Histograme")
    print("6. stack plot")
    print("7. back to main menu")

    sub_choice = int(input("Enter your choice: "))
    match sub_choice:
     case 1:
      da.bar_plot()
     case 2:
      pass
     case 3:
      pass
     case 4:
      pass
     case 5:
      pass
     case 6:
      pass
     case 7:
      break
  case 7:
   pass
  case 8:
   break
     
      
 
     