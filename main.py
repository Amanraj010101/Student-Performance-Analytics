#print("Student Performance Analysis System")
#print("Poject Started Successfully!")

# create student database using student.csv
#import pandas as pd
#data= pd.read_csv("students.csv")
#print(data)

#Identify data quality ,find miissing value
import numpy as np
import pandas as pd
data = pd.read_csv("students.csv")
print("Student Performance Analysis System")
print("_______________________")
print("\nStudent Data :")
print (data)
# FIND Missing Values
print ("\nMissing Values:")
print(data.isnull().sum())
#Average marks
print("\nAverage Marks:")
print("Maths:",data["Maths"].mean())
print("Science:",data["Science"].mean())
print("English:",data["English"].mean())
print("\nAttendence:",data["Attendence"].mean())
#calculate total marks
data["Total_Marks"]=data["Maths"]+ data["Science"]+ data["English"]
# Calculate Percentage
data["Percentage"]=(data["Total_Marks"]/300)*100
print ("\nStudent Performance:")
print (data[["Student_ID",  
  "Name",  "Total_Marks",
"Percentage"]]) 
#performance Category
def get_category(percentage):
    if percentage>=80 :
        return "Excellent"
    elif percentage>=60 :
        return "Good"
    elif percentage>=40 :
        return  "Average"
    else:
        return "Poor"

data["Performance"]= data["Percentage"].apply(get_category)
print("\nPerformance Category :")
print(data[["Student_ID",
"Name","Total_Marks",
"Percentage","Performance"]])
#Top 3 Students
top_students = data.sort_values(by="Percentage"
, ascending=False).head(3)

top_students.insert(0,"Serial_No", range(1,len(top_students) +1)) 

print("\nTop 3 Students :")
print(top_students[["Serial_No",
"Student_ID",
"Name",
"Total_Marks",
"Percentage"]])

# subject wise hightest marks

subjects =["Maths","Science","English"]
print("\nSubject-wise Perormance of Top 3 Students :")

for subject in subjects:
    highest_index =data[subject].idxmax()
    lowest_index = data[subject].idxmin()

    print(f"\n Subject :{subjects}")

    print(
        "Highest Marks:",
        data.loc[highest_index,"Name"],"-",
        data.loc[highest_index,subject]
    )

    print(
        "Lowest Marks:",
        data.loc[lowest_index,"Name"],"-",
        data.loc[lowest_index,subject]
    )

# Data Visualization
import matplotlib.pyplot as plt
#student total marks bar chart
plt.figure(figsize=(10,6))
plt.bar(data["Name"],
data["Total_Marks"])

plt.title("Student Total Marks")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.xticks(rotation=45,ha="right")

plt.tight_layout()
plt.savefig("student_chart.png")
plt.show()

#Subject-wise Performance chart
subjects=["Maths","Science","English"]
average_marks =[
   data["Maths"].mean(),
   data["Science"].mean(),
   data["English"].mean()
]

plt.figure(figsize=(10,6))
bars =plt.bar(subjects, average_marks)

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel('Average Marks')
plt.ylim(0,100)
#display marks on top of each bar
for bar in bars:
         height = bar.get_height()
         plt.text(
              bar.get_x()+
              bar.get_width()/2,
              height + 1,
              f"{height:.2f}",
         ha="center"
         )
plt.tight_layout()
plt.savefig("student_performance.png")
plt.show()
# Top 3 Students Chart

top_students = data.sort_values(
    by="Percentage",
    ascending=False
).head(3)

plt.figure(figsize=(8, 5))

bars = plt.bar(
    top_students["Name"],
    top_students["Percentage"]
)

plt.title("Top 3 Students Performance")
plt.xlabel("Student Name")
plt.ylabel("Percentage")
plt.ylim(0, 100)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        f"{height:.2f}%",
        ha="center"
    )

plt.tight_layout()
plt.savefig("top_3_students.png")
plt.show()
# Average Marks Chart
plt.figure(figsize=(8, 5))

subjects = ['Maths', 'Science', 'English']
average_marks = [
    data['Maths'].mean(),
    data['Science'].mean(),
    data['English'].mean()
]

plt.bar(subjects, average_marks)
plt.title('Average Marks by Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Marks')
plt.ylim(0, 100)

plt.show()
# Grade Distribution Chart
plt.figure(figsize=(8, 5))

grade_counts = data['Performance'].value_counts()

plt.bar(grade_counts.index, grade_counts.values)

plt.title('Student Grade Distribution')
plt.xlabel('Performance Category')
plt.ylabel('Number of Students')

plt.show()
# Save Top 3 Students Report
top_3_students = data.nlargest(3, 'Total_Marks')

top_3_students.to_csv(
    'top_3_students_report.csv',
    index=False
)

print("\nTop 3 Students report saved successfully!")
print("File name: top_3_students_report.csv")
# Pass/Fail Analysis
data['Result'] = np.where(
    (data['Maths'] >= 33) &
    (data['Science'] >= 33) &
    (data['English'] >= 33),
    'Pass',
    'Fail'
)

print("\nPass/Fail Statistics:")
print(data['Result'].value_counts())

print("\nStudent Results:")
print(data[['Name', 'Total_Marks', 'Percentage', 'Result']])

