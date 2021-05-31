import csv
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
def write_data(file_name,row):
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Student","Maths", "Computers","Physics","Chemistry"]) #Takes the Subjest names and saves in first row 
        for i in range(1,row+1):
            student=input("Enter the name of the "+str(i)+" student ")
            maths=float(input("enter the  maths marks of "+student+" "))
            computers=float(input("enter the  computers marks of "+student+" "))
            physics=float(input("enter the  physics marks of "+student+" "))
            chemistry=float(input("enter the  chemistry marks of "+student+" "))
            writer.writerows([[student,maths,computers,physics,chemistry]])



def display_data(file_name,n):
    df=pd.read_csv(file_name) #python -m pip install pandas  # raeding .csv file from pandas
    print(df) #printing the file
    # code for bargraph
    names = df['Student'].values
    #print(names)
    x = np.arange(len(names))    #same as [0,1,2_,_,_]   for x axis from which bar starts
    w = 0.1
    plt.bar(x-w, df['Maths'].values, width=w, label='Maths')  #syntx  plt.bar(x,height,width,bottom,align,data,**keywords)
    plt.bar(x, df['Computers'].values, width=w, label='Computers')
    plt.bar(x+w, df['Physics'].values, width=w, label='Physics')
    plt.bar(x+w+w, df['Chemistry'].values, width=w, label='Chemistry')
    plt.xticks(x, names)
    plt.ylim([0,100])   # limits y axis upto 100 only
    plt.xlabel('Students')
    plt.ylabel('Marks')
    plt.legend(bbox_to_anchor =(0.75, 1.15),ncol=4)
    figure=n+".png"    # to convert filename into image format
    plt.savefig(figure, bbox_inches="tight")  # to save the image of result bar graph
    plt.show()    #To show the bar graph


def main():
    n=input("enter the file name to save data in .csv format ")
    file_name=n+".csv"    # convert file name in csv format
    row=int(input("enter how many student data you want to enter ")) #how many students data to enter
    write_data(file_name,row)
    display_data(file_name,n)
    


if __name__ == "__main__":
    main()