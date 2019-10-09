import pandas as pd
import tkinter as tk
from tkinter import filedialog
import numpy as np

root = tk.Tk()
root.withdraw()

def getStaffDownload():
    df = pd.read_excel(filedialog.askopenfilename(initialdir = "W:\Staff Downloads\\"))

    print("File opening - Please wait.")
    return df

def addAgeGroup(df):
    bins = [0, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 100]
    labels = ['Under 20', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65+']
    df['Age Group'] = pd.cut(df['Age'], bins = bins, labels = labels, right = False)

    return df

addAgeGroup(getStaffDownload()).to_csv('W:/1 - Sandbox Downloads/agegroups.csv', index=False)
