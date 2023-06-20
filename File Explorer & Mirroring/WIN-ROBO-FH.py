import tkinter as tk                                                # For Basic GUI
import requests
import pandas as pd
import numpy as np
import ctypes
import platform
from tkinter import ttk                                             # For Advanced GUI
from tkinter import messagebox                                      # To display Error Messages in a pop up window
from tkinter import filedialog
import PIL.Image                                                    # To read image files like logo
import PIL.ImageTk                                                  # To insert images in Tkinter window
import socket                                                       # To get computer Hostname
import os                                                           # To pass windows and CMD commands from Python script
import math
import win32com.client as win32                                     # To access and create Outlook Emails
import getpass                                                      # To get local user name
import time                                                         # To get current timestamp
import shutil                                                       # For file handling like copy, paste, delete etc.   
from pytube import YouTube
import win32api
from pathlib import Path
import cv2
from imdb import Cinemagoer
import pywintypes
import warnings
warnings.filterwarnings('ignore')


# Extract Host Name, vcn, start time, current date:
host = socket.gethostname()
vcn = getpass.getuser()
start_time = time.strftime("%H:%M:%S") 
curr_date = time.strftime("%d-%m-%Y")

global gui
gui = tk.Tk()

def quit():                                    
    gui.destroy()
    
    
def email_contact(id):  
    global e, vcn
    e=e+1    
    outlook = win32.gencache.EnsureDispatch('Outlook.Application')
    mail = outlook.CreateItem(0)                                                #create a new mail item
    mail.To = id
    mail.Subject = "Support needed by  " + vcn
    mail.Display(True)
        
def contact():
    global vcn, root3
    # Frame for Contact Details
    lf2 = ttk.LabelFrame(root3, text = "Contact Information", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf2.place(x=10, y=10)
    tk.Frame(lf2, width=1400, height=570, bg = 'grey30').pack()
    
    tk.Label(root3, text="WIN-Robo-FH Application Developer", font=('Halvetica', 12, 'bold'), fg="yellow", bg="grey30").place(x=550, y=150)
    tk.Label(root3, text=" Arijit Roy Chowdhury \n Automation Expert \n Bangalore, India \n\n E-Mail: rc.arijit@gmail.com \n\n GIT-Hub: https://github.com/ArijitRoyDS" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey30").place(x=565, y=180)
    
def Help():
    global root5
    lf2 = ttk.LabelFrame(root5, text = "Help", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf2.place(x=10, y=10)
    tk.Frame(lf2, width=1400, height=570, bg = 'grey30').pack()
    tk.Label(root5, text="WINDOWS ROBUST FILE HANDLING", font=('Halvetica', 16, 'bold'), fg="yellow", bg='grey30').place(x=530, y=150)
    tk.Label(root5, text="Version: V-2022.3.1\n\nRelease Date: 12-03-2022\n\nApplications Available: Disk Space Availability, Robo-Copy, Mirroring & Backup\nFile Filtering, IMDB Database Synchronization, Synology DSM Access", font=('Halvetica', 12, 'bold'), fg="white", bg='grey30').place(x=410, y=200)

    tk.Label(root5, text="Link to Synology DDNS Server:", font=('Halvetica', 16, 'bold'), fg="yellow", bg='grey30').place(x=560, y=350)
    link70 = tk.Label(root5, text = 'https://arijitrc.synology.me:5001', font=('calibri', 12, 'bold'), fg="light blue", bg = "grey30",
             width=75, height=1, anchor='nw', cursor="hand2")
    link70.place(x=610, y=380)    
    link70.bind("<Button-1>", lambda event: os.startfile('https://arijitrc.synology.me:5001'))
    
    link71 = tk.Label(root5, text = 'http://arijitrc.synology.me:5000', font=('calibri', 12, 'bold'), fg="light blue", bg = "grey30",
             width=75, height=1, anchor='nw', cursor="hand2")
    link71.place(x=615, y=405)    
    link71.bind("<Button-1>", lambda event: os.startfile('http://arijitrc.synology.me:5000'))

####################################################################################################################################################
# IMDB Ratings
####################################################################################################################################################

def choose_dir1():
    global root6, lf50, filter_dir2, lf57
    filter_dir2 = filedialog.askdirectory()
    fil.set(filter_dir2)
    print("IMDB Search set for: ", filter_dir2)
    # lf52 = ttk.LabelFrame(root6, text = "Search Path: ", style="TLabelframe", 
    #                      labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    # lf52.place(x=540, y=130)
    
    lf57 = ttk.LabelFrame(lf50, text = "IMDB Sync Menu", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf57.place(x=1000, y=60)
    frame30 = tk.Frame(lf57, width=400, height=380, bg = 'grey30').pack()
    
    tk.Label(root6, text = "Folder Selected: ", font=('calibri', 11, 'bold'), fg="dark green").place(x=30, y=10)
    link5 = tk.Label(root6, text = filter_dir2, font=('calibri', 11, 'bold'), fg="dark green", 
             width=145, height=1, wraplength=1000, anchor='nw', cursor="hand2")
    link5.place(x=150, y=10)    
    fp2 = os.path.realpath(filter_dir2)
    link5.bind("<Button-1>", lambda event: os.startfile(fp2))  
    
    if "Hindi Movies" in filter_dir2:
        tk.Label(lf57, text = "Step 1: Hindi Movies Database: ", font=('calibri', 11, 'bold'), fg="white", bg = "grey30").place(x=20, y=20)
        button51 = ttk.Button(lf57, text="Create", style = 'C.TButton', command = local_hindi)
        button51.place(x=250, y=20)
        
    elif "English Movies" in filter_dir2:
        tk.Label(lf57, text = "Step 1: English Movies Database: ", font=('calibri', 11, 'bold'), fg="white", bg = "grey30").place(x=20, y=20)
        button51 = ttk.Button(lf57, text="Create", style = 'C.TButton', command = local_english)
        button51.place(x=250, y=20)
        
    elif "Bengali Movies" in filter_dir2:
        tk.Label(lf57, text = "Step 1: Bengali Movies Database: ", font=('calibri', 11, 'bold'), fg="white", bg = "grey30").place(x=20, y=20)
        button51 = ttk.Button(lf57, text="Create", style = 'C.TButton', command = local_bengali)
        button51.place(x=250, y=20)
        
    tk.Label(lf57, text = "Step 2: Refresh IMDB Database: ", font=('calibri', 11, 'bold'), fg="white", bg = "grey30").place(x=20, y=80)
    button52 = ttk.Button(lf57, text="Refresh", style = 'C.TButton', command = refresh_imdb)
    button52.place(x=250, y=80)
    
    tk.Label(lf57, text = "Step 3: Update English Database: ", font=('calibri', 11, 'bold'), fg="white", bg = "grey30").place(x=20, y=140)
    button53 = ttk.Button(lf57, text="Update", style = 'C.TButton', command = update_english)
    button53.place(x=250, y=140)
    
    tk.Label(lf57, text = "Step 4: Update Hindi Database: ", font=('calibri', 11, 'bold'), fg="white", bg = "grey30").place(x=20, y=200)
    button54 = ttk.Button(lf57, text="Update", style = 'C.TButton', command = update_hindi)
    button54.place(x=250, y=200)
    
    tk.Label(lf57, text = "Step 5: Update Bengali Database: ", font=('calibri', 11, 'bold'), fg="white", bg = "grey30").place(x=20, y=260)
    button54 = ttk.Button(lf57, text="Update", style = 'C.TButton', command = update_bengali)
    button54.place(x=250, y=260)
    
    tk.Label(lf57, text = "Step 6: Synchronize Metadata: ", font=('calibri', 11, 'bold'), fg="white", bg = "grey30").place(x=20, y=320)
    button54 = ttk.Button(lf57, text="Update", style = 'C.TButton', command = update_metadata)
    button54.place(x=250, y=320)
    
def update_metadata():
    ia = Cinemagoer()  
    met1 = pd.read_csv('English-Movies-Database-updated.csv')
    met2 = pd.read_csv('Hindi-Movies-Database-updated.csv') 
    met3 = pd.read_csv('Bengali-Movies-Database-updated.csv')        
    met = pd.concat([met1, met2, met3], axis=0)
    
    met = met.reset_index()  # make sure indexes pair with number of rows    
    df = pd.DataFrame(columns = ['primaryTitle_x', 'Year', 'Local-Path', 'pkey', 'tconst', 'primaryTitle_y', 'startYear', 'genres',
                                 'averageRating', 'movie-code', 'Director', 'IMDB-Rating', 'Duration', 'Genre', 'Cast', 'Plot', 
                                 'Cover-url', 'Certification'])
    for index, row in met.iterrows():
        row_data = [[]]
        #print(row['movie-code'])        
        try:    
            met = ia.get_movie(int(row['movie-code']))            
            movie_name = met['title']
            year = met['year']
            gen = met['genres']
            rating = met['rating']
            director = []
            try:     director = [c['name'] for c in met['director']]
            except:  director = "No Data"  
        except:  
            movie_name = "No Data"
            year = "No Data"
            gen = ["No Data"]
            director = ["No Data"]
            rating = "No Data"    
        cast = []
        
        try:
            certify = [cert.split(':')[1] for cert in met['certificates'] if cert.startswith('United States')][0]  
            if certify == 'Not Rated' or certify == 'Unrated' or certify == 'NA' or certify == '':
                certify = [cert.split(':')[1] for cert in met['certificates'] if cert.startswith('India')][0]
                
        except:
            try:
                certify = [cert.split(':')[1] for cert in met['certificates']][0]
            except:
                certify = 'NA'   
        
        try:     
            cast = [c['name'] for c in met['cast'][0:7]]
        except:  
            cast = ["No Data"]    
        try:     
            cover = met['cover url'].replace("'", '')
        except:  
            cover = "No Data"    
        try:
            plot = met['plot outline']
        except:
            try:
                plot = met['plot']
            except:
                plot = "No Data"    
        try:
            time = met['runtimes']
        except:
            time = ["No Data"]    
        
        print("\n-----------------------------------------------------------------------------------")
        print("Movie: ", movie_name)
        print("Year: ", year) 
        print("Star Cast: ", cast)
        print("Certification: ", certify)
        print("Plot: ", plot)
     
        row_data = [row['primaryTitle_x'], row['Year'], row['Local-Path'], row['pkey'], row['tconst'], row['primaryTitle_y'],
                        row['startYear'], row['genres'], row['averageRating'], row['movie-code'], ', '.join(director), rating, 
                        ', '.join(time), ', '.join(gen), ', '.join(cast), plot, cover, certify]
        
        row_dat = pd.DataFrame([row_data], columns = df.columns)
        df = pd.concat([df, row_dat])
        
        try:
            response = requests.get(cover, verify=False)
            if response.status_code:
                fp = open("Movie_Database\\Cover_Images\\" + str(row['movie-code']) + ".png", 'wb')
                fp.write(response.content)
                fp.close()      
        except Exception as e:
            print("Error E1: ", e)

    df.to_csv('Master-Meta-Data.csv', index = None) 
    
    
def update_english():    
    df1 = pd.read_csv('IMDB-Movie-Database.csv') 
    df2 = pd.read_csv('English-Movies-Database.csv') 
    
    df1['pkey'] = df1['pkey'].astype(str)
    df1['pkey'] = df1['pkey'].str.replace('\W', '', regex=True)
    df1['pkey'] = df1['pkey'].str.lower()
    
    df2['pkey'] = df2['pkey'].astype(str)
    df2['pkey'] = df2['pkey'].str.replace('\W', '', regex=True)
    df2['pkey'] = df2['pkey'].str.lower()
    
    df3 = pd.merge(df2, df1, on ='pkey', how ='inner')
    df3['movie-code'] = df3['tconst'].str[2:]    
    
    df3.to_csv("English-Movies-Database-updated.csv")
    print(df3.head(3))

def update_hindi():
    df1 = pd.read_csv('IMDB-Movie-Database.csv') 
    df2 = pd.read_csv('Hindi-Movies-Database.csv') 
    
    df1['pkey'] = df1['pkey'].astype(str)
    df1['pkey'] = df1['pkey'].str.replace('\W', '', regex=True)
    df1['pkey'] = df1['pkey'].str.lower()
    
    df2['pkey'] = df2['pkey'].astype(str)
    df2['pkey'] = df2['pkey'].str.replace('\W', '', regex=True)
    df2['pkey'] = df2['pkey'].str.lower()
    
    df3 = pd.merge(df2, df1, on ='pkey', how ='inner')
    df3['movie-code'] = df3['tconst'].str[2:]
    
    df3.to_csv("Hindi-Movies-Database-updated.csv")
    print(df3.head(3))
    
def update_bengali():
    df1 = pd.read_csv('IMDB-Movie-Database.csv') 
    df2 = pd.read_csv('Bengali-Movies-Database.csv') 
    
    df1['pkey'] = df1['pkey'].astype(str)
    df1['pkey'] = df1['pkey'].str.replace('\W', '', regex=True)
    df1['pkey'] = df1['pkey'].str.lower()
    
    df2['pkey'] = df2['pkey'].astype(str)
    df2['pkey'] = df2['pkey'].str.replace('\W', '', regex=True)
    df2['pkey'] = df2['pkey'].str.lower()
    
    df3 = pd.merge(df2, df1, on ='pkey', how ='inner')
    df3['movie-code'] = df3['tconst'].str[2:]
    
    df3.to_csv("Bengali-Movies-Database-updated.csv")
    print(df3.head(3))
    
def refresh_imdb():
    
    # # Movie Title & Language:
    # tsv_file='Movie_Database\\title.akas.tsv\\data.tsv'
    # lang=pd.read_table(tsv_file, sep='\t')
    
    # lang['tconst'] = lang['titleId']
    # # lang = lang[['tconst', 'title', 'region', 'language']]
    # # lang = lang[(lang['region'] == 'IN') | (lang['language'] == 'en')]
    # lang = lang[['tconst', 'title', 'language']]
    
    # Movie Title, Year and Genre:
    tsv_file='Movie_Database\\title.basics.tsv\\data.tsv'
    genre=pd.read_table(tsv_file, sep='\t')
    #genre = genre[(genre['titleType'] == 'movie') | (genre['titleType'] == 'tvMovie') | (genre['titleType'] == 'video')]
    
    genre = genre[(genre['titleType'] != 'tvEpisode')]
    genre = genre[['tconst', 'primaryTitle', 'startYear', 'genres', 'isAdult']]
    genre = genre.replace(r'\\N', 0, regex=True) 
    genre = genre[genre['startYear'].astype(int) >= 1900]
    
    #merge1 = pd.merge(genre, lang, on ='tconst', how ='inner')
    merge1 = genre
    
    # IMDB Rating:
    tsv_file='Movie_Database\\title.ratings.tsv\\data.tsv'
    ratings=pd.read_table(tsv_file, sep='\t')
    ratings = ratings[['tconst', 'averageRating']]
    
    merge1 = pd.merge(merge1, ratings, on ='tconst', how ='left')
    merge1 = merge1.replace(r'\\N', np.nan, regex=True) 
    merge1 = merge1.dropna()
    merge1 = merge1.drop_duplicates(subset=['tconst'], keep='first')
    
    merge1['pkey'] = merge1['primaryTitle'].astype(str) + merge1['startYear'].astype(str)
    
    merge1['isAdult'] = merge1['isAdult'].replace(0, '[G]')
    merge1['isAdult'] = merge1['isAdult'].replace(1, '[X]')
    merge1['isAdult'] = merge1['isAdult'].replace('0', '[G]')
    merge1['isAdult'] = merge1['isAdult'].replace('1', '[X]')
    
    merge1.to_csv("IMDB-Movie-Database.csv", index = None)
    
    
def local_hindi():
    # Hindi Movies
    global imdb_dir, filter_dir2
    df = pd.DataFrame(columns = ["primaryTitle", "Year", "Local-Path"])
    movie_names = []
    video_fmt = ['.webm', '.mkv', '.flv', '.vob', '.avi', '.mov', '.wmv', '.rm', '.rmvb', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', 
           '.mp2', '.mpeg', '.mpe', '.mpv', '.m2v', '.svi', '.3gp', '.3g2', '.flv', '.f4v', '.f4p', '.f4a', '.f4b', 
           '.dat', '.divx']
    for dirs, sub_dirs, files in os.walk(filter_dir2):
        for file in files:
    #         print(file)
            if any(vid.lower() in file.lower() for vid in video_fmt):  
                try:
                    temp1 = file.split('(')        
                    temp2 = temp1[1].split(')')   
                    temp3 = temp1[0].split(') ')  
                    movie_names.append(file)
                    temp = [temp3[-1].strip(), temp2[0].strip(), file]                    
                    new_df = pd.DataFrame([temp], columns=df.columns)
                    df = pd.concat([df, new_df])
                except:
                    pass
                
    print(df)
    df['pkey'] = df['primaryTitle'].astype(str) + df['Year'].astype(str)
    df['pkey'] = df['pkey'].str.replace('\W', '', regex=True)
    df['pkey'] = df['pkey'].str.lower()
    df.to_csv("Hindi-Movies-Database.csv")

def local_english():
    # English Movies
    global imdb_dir, filter_dir2
    df = pd.DataFrame(columns = ["primaryTitle", "Year", "Local-Path"])
    movie_names = []
    video_fmt = ['.webm', '.mkv', '.flv', '.vob', '.avi', '.mov', '.wmv', '.rm', '.rmvb', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', 
           '.mp2', '.mpeg', '.mpe', '.mpv', '.m2v', '.svi', '.3gp', '.3g2', '.flv', '.f4v', '.f4p', '.f4a', '.f4b', 
           '.dat', '.divx']
    
    #file_paths1 = [os.path.join(path, name) for path, subdirs, files in os.walk(filter_dir2) for name in files] 
    
    for dirs, sub_dirs, files in os.walk(filter_dir2):
        
        for file in files:
            if any(vid.lower() in file.lower() for vid in video_fmt):  
                try:
                    temp1 = file.split('(')        
                    temp2 = temp1[1].split(')')   
                    temp3 = temp1[0].split(') ')  
                    movie_names.append(file)
                    temp = [temp3[-1].strip(), temp2[0].strip(), file]                    
                    new_df = pd.DataFrame([temp], columns=df.columns)
                    df = pd.concat([df, new_df])
                except:
                    pass
    print(df)        
    df['pkey'] = df['primaryTitle'].astype(str) + df['Year'].astype(str)
    df['pkey'] = df['pkey'].str.replace('\W', '', regex=True)
    df['pkey'] = df['pkey'].str.lower()
    df.to_csv("English-Movies-Database.csv")
    
def local_bengali():
    # Bengali Movies
    global imdb_dir, filter_dir2
    df = pd.DataFrame(columns = ["primaryTitle", "Year", "Local-Path"])
    movie_names = []
    video_fmt = ['.webm', '.mkv', '.flv', '.vob', '.avi', '.mov', '.wmv', '.rm', '.rmvb', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', 
           '.mp2', '.mpeg', '.mpe', '.mpv', '.m2v', '.svi', '.3gp', '.3g2', '.flv', '.f4v', '.f4p', '.f4a', '.f4b', 
           '.dat', '.divx']
    
    #file_paths1 = [os.path.join(path, name) for path, subdirs, files in os.walk(filter_dir2) for name in files] 
    
    for dirs, sub_dirs, files in os.walk(filter_dir2):
        
        for file in files:
            #print(file)
            if any(vid.lower() in file.lower() for vid in video_fmt):  
                try:
                    temp1 = file.split('(')        
                    temp2 = temp1[1].split(')')   
                    temp3 = temp1[0].split(') ')  
                    movie_names.append(file)
                    temp = [temp3[-1].strip(), temp2[0].strip(), file]                    
                    new_df = pd.DataFrame([temp], columns=df.columns)
                    df = pd.concat([df, new_df])
                except:
                    pass
    
    print(df)
    df['pkey'] = df['primaryTitle'].astype(str) + df['Year'].astype(str)
    df['pkey'] = df['pkey'].str.replace('\W', '', regex=True)
    df['pkey'] = df['pkey'].str.lower()
    df.to_csv("Bengali-Movies-Database.csv")

    
def imdb():
    global root6, lf50, lf57, imdb_dir   
    
    # Create Frame for IMDB Ratings
    lf50 = ttk.LabelFrame(root6, text = "IMDB Ratings and Metadata", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf50.place(x=10, y=40)
    tk.Frame(lf50, width=1420, height=570, bg = 'grey20').pack()
    
    tk.Label(lf50, text = 'Steps to synchronize with IMDB Dataset: ', font=('Halvetica', 12, 'bold'), fg="yellow", bg="grey20").place(x=50, y=150) 
    tk.Label(lf50, text = 'Step 1: Click on the links to download IMDB Datasets: \t ', font=('Halvetica', 11, 'bold'), fg="light green", bg="grey20").place(x=50, y=190) 
    
    
    link51 = tk.Label(lf50, text = 'https://datasets.imdbws.com/name.basics.tsv.gz', font=('calibri', 10, 'bold'), fg="light blue", bg = "grey20",
              width=75, height=1, anchor='nw', cursor="hand2")
    link51.place(x=450, y=190)    
    link51.bind("<Button-1>", lambda event: os.startfile('https://datasets.imdbws.com/name.basics.tsv.gz')) 
    
    link52 = tk.Label(lf50, text = 'https://datasets.imdbws.com/title.akas.tsv.gz', font=('calibri', 10, 'bold'), fg="light blue", bg = "grey20",
              width=75, height=1, anchor='nw', cursor="hand2")
    link52.place(x=450, y=210)    
    link52.bind("<Button-1>", lambda event: os.startfile('https://datasets.imdbws.com/title.akas.tsv.gz'))
    
    # link53 = tk.Label(lf50, text = 'https://datasets.imdbws.com/title.basics.tsv.gz', font=('calibri', 10, 'bold'), fg="light blue", bg = "grey20",
    #          width=75, height=1, anchor='nw', cursor="hand2")
    # link53.place(x=450, y=230)    
    # link53.bind("<Button-1>", lambda event: os.startfile('https://datasets.imdbws.com/title.basics.tsv.gz'))
    
    # link54 = tk.Label(lf50, text = 'https://datasets.imdbws.com/title.ratings.tsv.gz', font=('calibri', 10, 'bold'), fg="light blue", bg = "grey20",
    #          width=75, height=1, anchor='nw', cursor="hand2")
    # link54.place(x=450, y=250)    
    # link54.bind("<Button-1>", lambda event: os.startfile('https://datasets.imdbws.com/title.ratings.tsv.gz'))
    
    tk.Label(lf50, text = 'Step 2: Unzip the contents into \\Movie_Database\\ maintaining the same folder structure', 
             font=('Halvetica', 11, 'bold'), fg="light green", bg="grey20").place(x=50, y=300) 
    
    tk.Label(lf50, text = 'Step 3: Click on "Browse" to choose the movie folder to synchronize with IMDB Database', 
             font=('Halvetica', 11, 'bold'), fg="light green", bg="grey20").place(x=50, y=340) 
    
    tk.Label(lf50, text = 'Step 4: Follow steps 1 - 5 in IMDB Sync Menu frame on the right. Repeat it for all languages.', 
             font=('Halvetica', 11, 'bold'), fg="light green", bg="grey20").place(x=50, y=380) 
    
    tk.Label(lf50, text = 'Browse Directory: ', font=('Halvetica', 12, 'bold'), fg="white", bg="grey20").place(x=5, y=15)    
    imdb_dir = tk.StringVar()
    button10 = ttk.Button(lf50, text="Browse", style = 'C.TButton', command = choose_dir1)
    button10.place(x=160, y=15)
    
    button7 = ttk.Button(root6, text="Refresh", style = 'C.TButton', command = imdb)
    button7.place(x=1330, y=10)

####################################################################################################################################################
# Filter Specific Files
####################################################################################################################################################

def filter_files():
    global root2, fil, lf40
    
    # Create Frame for File Filter
    lf40 = ttk.LabelFrame(root2, text = "File Filter", style="TLabelframe", 
                         labelanchor=tk.NW, height=55, width=150, relief=tk.SUNKEN)
    lf40.place(x=5, y=5)
    tk.Frame(lf40, width=1425, height=620, bg = 'grey20').pack()
    
    tk.Label(lf40, text = 'Browse Directory: ', font=('Halvetica', 12, 'bold'), fg="white", bg="grey20").place(x=5, y=10)    
    fil = tk.StringVar()
    button10 = ttk.Button(lf40, text="Browse", style = 'C.TButton', command = choose_dir)
    button10.place(x=160, y=10)
    
    # button7 = ttk.Button(root2, text="Refresh", style = 'C.TButton', command = filter_files)
    # button7.place(x=1340, y=3)
    
def choose_dir():
    global root2, lf40, lf27, resolution, genre
    filter_dir1 = filedialog.askdirectory()
    fil.set(filter_dir1)
    print("Filter set for: ", filter_dir1)
    # lf42 = ttk.LabelFrame(root2, text = "Filter Results: ", style="TLabelframe", 
    #                      labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    # lf42.place(x=540, y=130)
    browse_dir(filter_dir1)
    
    
def browse_dir(filter_dir):
    global root2, lf40, lf27, resolution, genre, note   
    note.select(root2)
    
    # tk.Label(root2, text = "Folder Selected: ", font=('calibri', 11, 'bold'), fg="dark green").place(x=100, y=5)
    link5 = tk.Label(root2, text = filter_dir, font=('calibri', 10, 'bold'), fg="light green", bg = "grey20",
             width=35, height=3, wraplength=250, anchor='nw', cursor="hand2")
    link5.place(x=8, y=70)    
    fp1 = os.path.realpath(filter_dir)
    link5.bind("<Button-1>", lambda event: os.startfile(fp1))    
    
    # lf42 = ttk.LabelFrame(root2, text = "Filter Results: ", style="TLabelframe", 
    #                       labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    # lf42.place(x=540, y=130)
    
    lf27 = ttk.LabelFrame(root2, text = "Filter Parameters", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=1050, relief=tk.SUNKEN)
    lf27.place(x=270, y=5)
    frame30 = tk.Frame(lf27, width=1160, height=135, bg = 'grey20').pack()
    
    tk.Label(lf27, text = 'Filter by Size (MB): ', font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20").place(x=5, y=25)
    tk.Label(lf27, text =                 'Min: ', font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=150, y=10)
    tk.Label(lf27, text =                 'Max: ', font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=150, y=40)
    
    min1 = tk.StringVar(root2)  
    max1 = tk.StringVar(root2)    
    minimum = [i for i in range(0, 20000, 1000)]
    maximum = [i for i in range(1000, 21000, 1000)]
    maximum.append(99999) 
    
    dd1 = ttk.Combobox(lf27, textvariable=min1, width=7, height=8, values=minimum, font=('Halvetica', 10))
    dd1.place(x=200, y=10)
    dd1.current(0)
    
    dd2 = ttk.Combobox(lf27, textvariable=max1, width=7, height=8, values=maximum, font=('Halvetica', 10))
    dd2.place(x=200, y=40)
    dd2.current(len(maximum)-1)
    
    tk.Label(lf27, text = 'Filter by Extension: ', font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20").place(x=540, y=10)
    ext = tk.StringVar(root2)
    extensions = ['All Audio', 'All Video', 'All Documents', 'All Pictures', 'All Files',
                  '.webm', '.mkv', '.flv', '.vob', '.avi', '.mov', '.wmv', '.rm', '.rmvb', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv',
                  '.m2v', '.svi', '.3gp', '.3g2', '.flv', '.f4v', '.f4p', '.f4a', '.f4b', '.dat', '.divx', '.mp3', '.wma', '.aac', '.wav', '.flac', '.m4a',
                  '.jpg', '.jpeg', '.tiff', '.png', '.gif', '.webp', '.psd', '.raw', '.bmp', '.heif', '.indd', '.cr2', '.jpe', '.jif', ',jfif', '.jfi', '.tif', '.svg',
                  '.pdf', '.docx', '.doc', '.docm', '.xlsx', '.xls', '.xlsm', '.pptx', '.py', '.ipynb', '.txt', '.html', '.htm', '.db', '.xml', '.csv', '.xls',
                  '.xps', '.ppt']
    extensions.sort(reverse=True)
    dd3 = ttk.Combobox(lf27, textvariable=ext, width=12, height=10, values=extensions, font=('Halvetica', 10))
    dd3.place(x=710, y=10)
    dd3.current(0)
    
    kw1 = tk.StringVar(root2)  
    kw21 = tk.StringVar(root2) 
    kw22 = tk.StringVar(root2) 
    kw3 = tk.StringVar(root2) 
    kw4 = tk.StringVar(root2)

    
    resolution = ['320', '360', '480', '560', '720', '800', '1080', '1440', '2160']  
    resolution.append('Any')
    tk.Label(lf27, text = 'Minimum Resolution: ', font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20").place(x=540, y=70)
    dd4 = ttk.Combobox(lf27, textvariable=kw1, width=5, height=10, values=resolution, font=('Halvetica', 10))
    dd4.place(x=710, y=70)
    dd4.current(len(resolution)-1)
    
    year = [i for i in range(1900, 2025)]  
    # year.append('Any')
    tk.Label(lf27, text = 'Filter by Year: ', font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20").place(x=290, y=25)
    tk.Label(lf27, text =           'From: ', font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=405, y=10)
    dd4 = ttk.Combobox(lf27, textvariable=kw21, width=5, height=15, values=year, font=('Halvetica', 10))
    dd4.place(x=460, y=10)
    dd4.current(0)
    
    tk.Label(lf27, text =             'To: ', font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=405, y=40)
    dd41 = ttk.Combobox(lf27, textvariable=kw22, width=5, height=15, values=year, font=('Halvetica', 10))
    dd41.place(x=460, y=40)
    dd41.current(len(year)-1)
    
    language = ['All', 'Hindi', 'English', 'Bengali', 'Other Languages'] 
    tk.Label(lf27, text = 'Filter by Language: ', font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20").place(x=540, y=40)
    dd4 = ttk.Combobox(lf27, textvariable=kw3, width=12, height=15, values=language, font=('Halvetica', 10))
    dd4.place(x=710, y=40)
    dd4.current(0)
    
    genre = ['Adventure', 'Drama', 'Crime', 'Action', 'War', 'Horror', 'Thriller', 'Romance', 'Legal', 'Comedy', 'Family', 'Fantasy', 'History',
             'Fiction', 'Spy', 'Dance', 'Musical', 'SciFi', 'Superhero', 'Sports', 'Violence', 'Psychological', 'Suspense', 'Tragedy', 'Political', 
             'Classic', 'Old', 'Monster', 'Disaster', 'Animated', 'Biography']
    genre.sort()
    genre.append('All')
    tk.Label(lf27, text = 'Genre: ', font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20").place(x=860, y=70)
    dd5 = ttk.Combobox(lf27, textvariable=kw4, width=12, height=15, values=genre, font=('Halvetica', 10))
    dd5.place(x=1020, y=70)
    dd5.current(len(genre)-1)
    
    kw5 = tk.StringVar()
    tk.Label(lf27, text = 'Filter by Keyword: ', font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20").place(x=5, y=100)
    kw = tk.Entry(lf27, textvariable = kw5, width=30, font=('Halvetica', 11), highlightthickness=1, highlightbackground = "white", 
                  highlightcolor= "white").place(x=200, y=100)
    tk.Label(lf27, text = "**Separate values by Semicolon", font=('Halvetica', 10), fg="white", bg="grey20").place(x=450, y=100)
    
    kw6 = tk.StringVar()    
    imdb = [i for i in range(25, 251, 25)]
    imdb.append('All')
    tk.Label(lf27, text = 'IMDB Rank:   Top: ', font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20").place(x=860, y=10)
    dd6 = ttk.Combobox(lf27, textvariable=kw6, width=5, height=15, values=imdb, font=('Halvetica', 10))
    dd6.place(x=1020, y=10)
    dd6.current(len(imdb)-1)
    
    kw8 = tk.StringVar()
    rating = [round(i,1) for i in np.arange(10,0,-0.5)]
    rating.append('All')
    tk.Label(lf27, text = 'IMDB Rating:   Min:', font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20").place(x=860, y=40)
    dd8 = ttk.Combobox(lf27, textvariable=kw8, width=5, height=15, values=rating, font=('Halvetica', 10))
    dd8.place(x=1020, y=40)
    dd8.current(len(rating)-1)
    
    kw7 = tk.StringVar()
    df5 = pd.read_excel('Star_Cast.xlsx')
    actors = list(df5['English'])    
    if 'English' in filter_dir:
        actors = list(df5['English'])
    elif 'Hindi' in filter_dir:
        actors = list(df5['Hindi'])
    elif 'Bengali' in filter_dir:
        actors = list(df5['Bengali'])
    else:
        actors = list(df5['English']) + list(df5['Hindi']) + list(df5['Bengali'])
    actors = [x for x in actors if x != 'X']
    #actors.sort()
    actors.append('All')
        
    tk.Label(lf27, text = 'Filter by Star Cast: ', font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20").place(x=5, y=70)
    dd4 = ttk.Combobox(lf27, textvariable=kw7, width=22, height=15, values=actors, font=('Halvetica', 10))
    dd4.place(x=200, y=70)
    dd4.current(len(actors)-1)  
    
    kw9 = tk.StringVar()
    op = ['Yes', 'No']
    # Button1 = tk.Checkbutton(lf27, text = "Show File Size", variable = kw9, font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20", 
    #                          onvalue = 1, offvalue = 0, height = 1, width = 10, highlightcolor = 'black', disabledforeground="grey20").place(x=700, y=100)
    tk.Label(lf27, text = 'Show File Size?: ', font=('Halvetica', 11, 'bold'), fg="yellow", bg="grey20").place(x=680, y=100)
    dd4 = ttk.Combobox(lf27, textvariable=kw9, width=5, height=2, values=op, font=('Halvetica', 10))
    dd4.place(x=815, y=100)
    dd4.current(1)    
    
    button11 = ttk.Button(lf27, text="Filter", style = 'C.TButton', command = lambda: filter_results(filter_dir, min1, max1, ext, kw1, kw21, kw22, kw3, kw4, kw5, kw6, kw7, kw8, kw9))
    button11.place(x=1020, y=100)    
    
# Function to filter based on usr entered keywords
def on_keyrelease5(event3):
    global filter_result, listbox5
    value = event3.widget.get()
    value = value.strip().lower()    
    if value == '':
        data = filter_result
    else:
        data = []
        for item in filter_result:
            if value.lower() in item.lower():
                data.append(item)         
    listbox_update5(data)
    
# Function to display searched items
def listbox_update5(data5):  
    global listbox5, item3, data6
    data6=data5
    listbox5.delete(0, 'end')    
    for item3 in data5:
        play1  = item3.split('\\')[-1]   
        listbox5.insert('end', play1)
    listbox5.bind('<Button-3>', metadata)
    listbox5.bind('<Double-1>', launch_file)
    
    listbox5.pack(side=tk.LEFT, fill=tk.BOTH)  

def metadata(event4):
    global lf7, gui
    name = listbox5.get(listbox5.curselection())
    
    try:
        temp1 = name.split('(')        
        temp2 = temp1[1].split(')')   
        temp3 = temp1[0].split(') ')  
        
        movie_name_year = temp3[-1].strip() + temp2[0].strip()
        movie_name_year = movie_name_year.lower()
        movie_name_year = ''.join(e for e in movie_name_year if e.isalnum())

    except:
        pass
    
    #print("Movie Name + Year: ", movie_name_year)      
    met = pd.read_csv('Master-Meta-Data.csv')    
    cover = ''        
    
    try:    
            code       = met[met['pkey'] == movie_name_year]['movie-code'].iloc[0]   
            cover      = "Movie_Database\\Cover_Images\\" + str(code) + ".png"
    except: 
            code       = "No Data"
            cover      = "Movie_Database\\Cover_Images\\no_data.png"
            
    if not os.path.isfile(cover):
        cover = "Movie_Database\\Cover_Images\\no_data.png"
    
    try:    movie_name = met[met['pkey'] == movie_name_year]['primaryTitle_x'].iloc[0]  
    except: movie_name = "No Data"    
        
    try:    year       = met[met['pkey'] == movie_name_year]['startYear'].iloc[0] 
    except: year       = "No Data"    
    
    try:    cert       = met[met['pkey'] == movie_name_year]['Certification'].iloc[0] 
    except: cert       = "NA"  
        
    try:    gen        = met[met['pkey'] == movie_name_year]['Genre'].iloc[0]  
    except: gen        = "No Data"    
        
    try:    rating     = met[met['pkey'] == movie_name_year]['IMDB-Rating'].iloc[0]  
    except: rating     = "NA"    
        
    try:    director   = met[met['pkey'] == movie_name_year]['Director'].iloc[0]  
    except: director   = "No Data"    
        
    try:    cast       = met[met['pkey'] == movie_name_year]['Cast'].iloc[0]
    except: cast       = "No Data"    
        
    try:    time       = met[met['pkey'] == movie_name_year]['Duration'].iloc[0]
    except: time       = "No Data" 
    
    try:    plot       = met[met['pkey'] == movie_name_year]['Plot'].iloc[0]
    except: plot       = "No Data"
    
    plot = plot.replace('[', '')
    plot = plot.replace(']', '')
    plot = plot.replace("'", '')
       
    lf7 = ttk.LabelFrame(root2, text = "Movie Metadata", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf7.place(x=910, y=160)
    frame = tk.Frame(lf7, width=520, height=460, bg = 'grey20')
    frame.pack()  
    
    try:
        image3 = PIL.Image.open(cover)
        cvr = PIL.ImageTk.PhotoImage(image3)
        label3 = tk.Label(frame, image = cvr)
        label3.image = cvr
        label3.place(x=400, y=10)
    except:
        pass      
    
    link52 = tk.Label(frame, text = 'Play Movie', font=('Halvetica', 11, 'bold'), fg="blue", bg="grey20", 
                      justify="center", anchor='nw', cursor="hand2")
    link52.place(x=410, y=170)  
    
    ftp = listbox5.get(listbox5.curselection()).split('  ==>> ')[0]
    #print(ftp)
    file_to_play = [i for i in data6 if ftp in i]
    ftp1 = file_to_play[0].split('  ==>> ')[0]
    ftp1 = ftp1.split('\\')
    del ftp1[-1]
    ftp1 = os.path.join(*ftp1)
    #print("Movie Selected: ", ftp1)        
    link52.bind("<Button-1>", lambda event: launch_file2())
    
    link51 = tk.Label(frame, text = movie_name, font=('Halvetica', 18, 'bold'), fg="yellow", bg="grey20", 
                      wraplength=400, justify="center", anchor='nw', cursor="hand2")
    link51.place(x=10, y=10)    
    link51.bind("<Button-1>", lambda event: os.startfile(ftp1)) 
    
    tk.Label(frame, text = "Year\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=90)
    tk.Label(frame, text = str(year), font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=100, y=90)
    
    tk.Label(frame, text = "IMDB Rating: " , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=235, y=90)
    tk.Label(frame, text = rating, font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=500, justify="left").place(x=325, y=90)
       
    tk.Label(frame, text = "Certificate: " , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=235, y=120)
    tk.Label(frame, text = cert, font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=500, justify="left").place(x=325, y=120)
    
    tk.Label(frame, text = "Length\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=120)
    tk.Label(frame, text = time + ' Minutes', font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=500, justify="left").place(x=100, y=120)
    
    tk.Label(frame, text = "Director\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=150)
    tk.Label(frame, text = director, font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=300, justify="left").place(x=100, y=150)   
    
    tk.Label(frame, text = "Genre\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=190)
    tk.Label(frame, text = gen, font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=500, justify="left").place(x=100, y=190)
    
    tk.Label(frame, text = "Cast\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=220)
    tk.Label(frame, text = cast, font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=400, justify="left").place(x=100, y=220)
   
    tk.Label(frame, text = "Plot\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=280)
    txt = tk.Text(frame, wrap=tk.WORD, height = 10, width = 58, bg = "grey20", font = ("Helvetica", 10), fg = "white") # wrap=CHAR, wrap=NONE
    txt.place(x=100, y=280)
    txt.insert(tk.END, plot)

    
  
def launch_file(event3):
    ftp = listbox5.get(listbox5.curselection()).split('  ==>> ')[0]
    #print(ftp)
    file_to_play = [i for i in data6 if ftp in i]
    print("Playing: ", ftp)
    os.startfile(file_to_play[0].split('  ==>> ')[0])    
    
def launch_file2():
    ftp = listbox5.get(listbox5.curselection()).split('  ==>> ')[0]
    #print(ftp)
    file_to_play = [i for i in data6 if ftp in i]
    print("Playing: ", ftp)
    os.startfile(file_to_play[0].split('  ==>> ')[0]) 
    
def scrollbar5(x, y):
    global listbox5
    listbox5.yview(x,y)   
    
    
def filter_results(fp5, min1, max1, ext, kw1, kw21, kw22, kw3, kw4, kw5, kw6, kw7, kw8, kw9):
    global lf40, listbox5, filter_result, lf27, resolution, genre, ss
    min1 = min1.get()
    max1 = max1.get()
    e = ext.get()
    res = kw1.get()
    
    yr1 = kw21.get()
    yr2 = kw22.get()
    if "english movies" in fp5.lower() or "hindi movies" in fp5.lower() or "bengali movies" in fp5.lower():
        yr = [str(x) for x in range(int(yr1), int(yr2)+1)]    
    else:
        yr = ['']
        
    lang = kw3.get()
    if lang == 'All':
        lang = ''

    actors1 = kw7.get()
    if actors1 == 'All':
        actors1 = ''
        
    gen = kw4.get()
    keyword = kw5.get().split(";")
    keyword = [i.strip() for i in keyword]
    cast = kw7.get()
    
    imdb2 = []
    imdb_rate = kw8.get()
    if imdb_rate == 'All':
        imdb2 = ['']
        imdb3 = ['']
    else:
        imdb2 = ['IMDB ' + str(round(i-0.05, 1)) for i in np.arange(float(imdb_rate), 10, 0.1)]
        imdb3 = [' [' + str(round(i-0.05, 1)) + ']}' for i in np.arange(float(imdb_rate), 10, 0.1)]
        
    rank = []
    imdb1 = kw6.get()
    if imdb1 == 'All':
        rank = ['']
    else:
        rank = ['IMDB #' + str(i)  + ' ' for i in range(1, int(imdb1)+1)]         # Format = {IMDB #102 [8.1]}
    ss = kw9.get()    
    
    print('\nFilter Folder Path: ', fp5)
    print('Minimum Size      : ', min1)
    print('Maximum Size      : ', max1)
    print('File Extension    : ', e)
    print('Resolution        : ', res)
    print('Year              : ', yr)
    print('Cast              : ', cast)
    print('IMDB Ranks        : ', rank)
    print('IMDB Rating       : ', imdb2)    
    print('Language          : ', kw3.get())
    print('Genre             : ', gen)
    print('Keyword           : ', keyword)
    print('Show Filesize     : ', ss)
    
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nFilter Results:')    
    
    file_paths = [os.path.join(path, name) for path, subdirs, files in os.walk(fp5) for name in files]   
    
    for file in file_paths:  
        if len(file) > 253:
            print("Filename: ", file)
            print("Character Length: ", len(file))
            
    vid = ['.webm', '.mkv', '.flv', '.vob', '.avi', '.mov', '.wmv', '.rm', '.rmvb', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', '.mpv',
            '.m2v', '.m4v', '.svi', '.3gp', '.3g2', '.flv', '.f4v', '.f4p', '.f4a', '.f4b', '.dat', '.divx']
    
    aud = ['.mp3', '.wma', '.aac', '.wav', '.flac', '.m4a']
    
    pic = ['.jpg', '.jpeg', '.tiff', '.png', '.gif', '.webp', '.psd', '.raw', '.bmp', '.heif', '.indd', '.cr2', '.jpe', '.jif', ',jfif', '.jfi', '.tif', '.svg']
    
    doc = ['.pdf', '.docx', '.doc', '.docm', '.xlsx', '.xls', '.xlsm', '.pptx', '.py', '.ipynb', '.txt', '.html', '.htm', '.db', '.xml', '.csv', '.xls',
           '.xps', '.ppt']
    
    height=0
    filter_result = []
    
    df1 = pd.read_csv('English-Movies-Database-updated.csv') 
    df2 = pd.read_csv('Hindi-Movies-Database-updated.csv')
    df3 = pd.read_csv('Bengali-Movies-Database-updated.csv')
    
    for file in file_paths:  
        # if len(file) > 253:
        #     continue    
    
        if any(kwd.lower() not in file.lower() for kwd in keyword):
            continue                 
        
        file1 = Path(file)
        
        if ss == 'Yes':
            s = round(os.path.getsize(file1)) 
            file_size = s/1024/1024
            
            if round(s/1024/1024/1024, 1) >= 1:
                file_size1 = '  ==>> ' + str(round(s/1024/1024/1024, 1)) + ' GB'
            elif round(s/1024/1024, 1) >= 1 and round(s/1024/1024/1024, 1) <1:
                file_size1 = '  ==>> ' + str(round(s/1024/1024, 1)) + ' MB'
            else:
                file_size1 = '  ==>> ' + str(round(s/1024, 1)) + ' KB'
        else:
            min1 = 0
            max1 = 9999999
            file_size = 1
            file_size1 = ''
                
                
        genres = ''
        imdb_rating = ''
        meta = ''
        ############################################################################################################
        # Filter Videos:
        ############################################################################################################
        if any(yer in file for yer in yr):
            if file_size >= int(min1) and file_size <= int(max1) and lang in file and actors1.lower() in file.lower() and '.vsmeta'.lower() not in file.lower() and'Thumbs.db'.lower() not in file.lower() and '_.ini' not in file.lower() and 'desktop.ini' not in file.lower():      
                try:
                    if "English Movies" in file:
                        genres = df1.loc[df1['Local-Path'] == file.split('\\')[-1], 'genres'].values[0]
                        imdb_rating = df1.loc[df1['Local-Path'] == file.split('\\')[-1], 'averageRating'].values[0]
                        viewer_rating = df1.loc[df1['Local-Path'] == file.split('\\')[-1], 'isAdult'].values[0]
                        imdb_rating = '[IMDB ' + str(imdb_rating) + ']'                        
                                                
                    elif "Hindi Movies" in file:
                        genres = df2.loc[df2['Local-Path'] == file.split('\\')[-1], 'genres'].values[0]
                        imdb_rating = df2.loc[df2['Local-Path'] == file.split('\\')[-1], 'averageRating'].values[0]
                        viewer_rating = df2.loc[df2['Local-Path'] == file.split('\\')[-1], 'isAdult'].values[0]
                        imdb_rating = '[IMDB ' + str(imdb_rating) + ']'
                        
                    elif "Bengali Movies" in file:
                        genres = df3.loc[df3['Local-Path'] == file.split('\\')[-1], 'genres'].values[0]
                        imdb_rating = df3.loc[df3['Local-Path'] == file.split('\\')[-1], 'averageRating'].values[0]
                        viewer_rating = df3.loc[df3['Local-Path'] == file.split('\\')[-1], 'isAdult'].values[0]
                        imdb_rating = '[IMDB ' + str(imdb_rating) + ']'
                        
                    meta = "  ==>> " + genres + ' - ' + imdb_rating 
                    
                except:
                    pass
                #print("Meta = ", meta)
                if any(imd.lower() in meta.lower() for imd in imdb2) or any(imd1.lower() in file.lower() for imd1 in imdb3):
                    if any(rnk in file for rnk in rank):
                                          
                        # Filter Video Files by Extension, Resolution and Year
                        if e in vid or e == 'All Video':
                            if gen in file or gen == 'All':
                                for file_format in vid:
                                    if file_format in file.lower() and e == 'All Video':
                                        if res != 'Any' and res in file:
                                            filter_result.append(file + meta + file_size1)      
                                        elif res != 'Any' and res not in file:
                                            try:
                                                v = cv2.VideoCapture(file)
                                                height = v.get(cv2.CAP_PROP_FRAME_HEIGHT)
                                            except:
                                                height = 0
                                            if height >= int(res)*0.8 or res in file:
                                                filter_result.append(file + meta + file_size1)     
                                        elif res == 'Any':
                                            filter_result.append(file + meta + file_size1)
                                            
                                if e in file:                        
                                    if res != 'Any' and res in file:
                                        filter_result.append(file + meta + file_size1)   
                                    elif res != 'Any' and res not in file:
                                        try:
                                            v = cv2.VideoCapture(file)
                                            height = v.get(cv2.CAP_PROP_FRAME_HEIGHT)
                                        except:
                                            height = 0
                                        if height >= int(res)*0.8 or res in file:
                                            filter_result.append(file + meta + file_size1 )   
                                    elif res == 'Any':
                                        filter_result.append(file + meta + file_size1)                     

        ############################################################################################################
        # Filter Audios:
        ############################################################################################################
        if file_size >= int(min1) and file_size <= int(max1) and lang in file and 'Thumbs.db'.lower() not in file.lower() and actors1.lower() in file.lower() and '_.ini' not in file.lower() and 'desktop.ini' not in file.lower():      
            # Filter Audio Files by Extension
            if e in aud or e == 'All Audio':
                if e in file.lower():
                    filter_result.append(file + file_size1)
                elif e == 'All Audio':
                    for file_format in aud:
                        if file_format in file.lower():
                            filter_result.append(file + file_size1)
            
        ############################################################################################################
        # Filter All Files:
        ############################################################################################################
        if file_size >= int(min1) and file_size <= int(max1) and e == 'All Files' and actors1.lower() in file.lower() and 'Thumbs.db'.lower() not in file.lower() and '_.ini' not in file.lower() and 'desktop.ini' not in file.lower():
            filter_result.append(file + file_size1)
            
            
        ############################################################################################################
        # Filter All Pictures:
        ############################################################################################################
        if file_size >= int(min1) and file_size <= int(max1) and 'Thumbs.db'.lower() not in file.lower() and '_.ini' not in file.lower() and 'desktop.ini' not in file.lower():
            # Filter Image Files by Extension
            if e in pic or e == 'All Pictures':
                if e in file.lower():
                    filter_result.append(file + file_size1)
                elif e == 'All Pictures':
                    for file_format in pic:
                        if file_format in file.lower():
                            filter_result.append(file + file_size1)
                        
        ############################################################################################################
        # Filter All Documents:
        ############################################################################################################
        if file_size >= int(min1) and file_size <= int(max1) and 'Thumbs.db'.lower() not in file.lower() and '_.ini' not in file.lower() and 'desktop.ini' not in file.lower():
            # Filter Document Files by Extension
            if e in doc or e == 'All Documents':
                if e in file.lower():
                    filter_result.append(file + file_size1)
                elif e == 'All Documents':
                    for file_format in doc:
                        if file_format in file.lower():
                            filter_result.append(file + file_size1)

                        
        ############################################################################################################
                            
    # for f in filter_result:                        
    #     print(f)
    
    fil = []
    for f1 in filter_result:
        files1 = f1.split('\\')[-1]
        if files1[1] == ')':
            files1 = files1[3:]
        elif files1[2] == ')':
            files1 = files1[4:]
        elif files1[3] == ')':
            files1 = files1[5:]
        fil.append(files1)
    fil.sort()
    print(fil)
    
    sorted_filter_result = []
    for f2 in fil:
        for f3 in filter_result:
            if f2 in f3:
                sorted_filter_result.append(f3)
            
        
           
    tk.Label(lf27, text = 'Files Found: ' + str(len(filter_result)), font=('Halvetica', 10, 'bold'), fg="light green", bg="grey20").place(x=890, y=105)
        
    lf42 = ttk.LabelFrame(root2, text = "Filter Results: ", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf42.place(x=5, y=160)
    frame35 = tk.Frame(lf42, width=780, height=400, bg = 'grey30')
    frame35.pack()
    
    # Auto Complete Listbox for Application Search based on key words entered by user
    tk.Label(root2, text="Search:", font=('Halvetica', 12, 'bold'), fg="yellow", bg="grey20").place(x=10, y=130)
    entry5 = tk.Entry(root2, width=25, font=('Helvetica', 10), bg='white', fg='black',
                     highlightthickness=1, highlightbackground = "white", highlightcolor= "white")
    entry5.place(x=80, y=130)
    entry5.bind('<KeyRelease>', on_keyrelease5)

    scroll5 = tk.Scrollbar(frame35)
    listbox5 = tk.Listbox(frame35, width=126, height=24, font=('Calibri', 11, 'bold'), bg='grey30', fg='white', yscrollcommand = scroll5.set)
    
    listbox_update5(sorted_filter_result)
    
    listbox5.pack(side=tk.LEFT, fill=tk.BOTH)        
    scroll5.config(command = scrollbar5)
    scroll5.pack(side=tk.RIGHT, fill=tk.Y) 
    
    lf7 = ttk.LabelFrame(root2, text = "Movie Metadata", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf7.place(x=910, y=160)
    frame = tk.Frame(lf7, width=520, height=460, bg = 'grey20')
    frame.pack() 
    
    link51 = tk.Label(frame, text = "No Data - Right click a movie to display metadata", font=('Halvetica', 18, 'bold'), fg="yellow", bg="grey20", 
                      wraplength=400, justify="center", anchor='nw', cursor="hand2")
    link51.place(x=10, y=10)    
    link51.bind("<Button-1>", lambda event: launch_file2()) 
    
    tk.Label(frame, text = "Year\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=90)
    tk.Label(frame, text = "No Data", font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=100, y=90)
    
    tk.Label(frame, text = "IMDB Rating: " , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=235, y=90)
    tk.Label(frame, text = "NA", font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=500, justify="left").place(x=325, y=90)
    
    tk.Label(frame, text = "Certificate: " , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=235, y=120)
    tk.Label(frame, text = "NA", font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=500, justify="left").place(x=325, y=120)
    
    tk.Label(frame, text = "Length\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=120)
    tk.Label(frame, text = "No Data", font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=500, justify="left").place(x=100, y=120)
    
    tk.Label(frame, text = "Director\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=150)
    tk.Label(frame, text = "No Data", font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=300, justify="left").place(x=100, y=150)   
    
    tk.Label(frame, text = "Genre\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=190)
    tk.Label(frame, text = "No Data", font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=500, justify="left").place(x=100, y=190)
    
    tk.Label(frame, text = "Cast\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=220)
    tk.Label(frame, text = "No Data", font=('Halvetica', 10, 'bold'), fg="white", bg="grey20", wraplength=400, justify="left").place(x=100, y=220)
   
    tk.Label(frame, text = "Plot\t:" , font=('Halvetica', 10, 'bold'), fg="white", bg="grey20").place(x=10, y=260)
    txt = tk.Text(frame, wrap=tk.WORD, height = 12, width = 57, bg = "grey20", font = ("Helvetica", 10), fg = "white") # wrap=CHAR, wrap=NONE
    txt.place(x=100, y=260)
    txt.insert(tk.END, "No Data")

    notCovered = list(set(file_paths) - set(filter_result))            
    print(notCovered, len(notCovered))
    
    df5 = pd.DataFrame(notCovered)
    df5.to_csv('not covered.csv')    

####################################################################################################################################################
# Search for a specific folder
####################################################################################################################################################

# Function to filter based on usr entered keywords
def on_keyrelease1(event11):
    global available_drives, volume_labels, data1, drive_paths, dirs, paths
    value1 = event11.widget.get()
    print(value1)
    
    print(paths)
    di = []
    for directory in paths:
        di.append(directory)
    print(di)
            
    value1 = value1.strip().lower()    
    if value1 == '':
        data1 = di
    else:
        data1 = []
        for item1 in di:
            if value1 in item1.lower():
                data1.append(item1)         
    listbox_update1(data1)
    
# Function to display searched items
def listbox_update1(data2):  
    global listbox1
    listbox1.delete(0, 'end')    
    for item1 in data2:
        listbox1.insert('end', item1)
    listbox1.bind('<Double-1>', select_directory)
    listbox1.pack(side=tk.LEFT, fill=tk.BOTH)
    
def properties(folder_path):
    global root4    
    # Create Frame to get folder size
    lf15 = ttk.LabelFrame(root4, text = "Folder Properties", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf15.place(x=850, y=140)
    frame10 = tk.Frame(lf15, width=550, height=430, bg = 'grey30').pack()    
 
    folder_count = 0
    file_count = 0
    for home, dirs, files in os.walk(folder_path):
        folder_count += len(dirs)
        file_count += len(files)            
    print("Number of Folders inside selected Directory: ", folder_count, type(folder_count))
    print("Number of Files inside selected Directory  : ", file_count, type(file_count))
           
    root_directory = Path(folder_path)
    size = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())
 
    # display size
    p = math.pow(1024, 3)
    s = round(size / p, 3)
    print("Size of Source Directory                 : " + str(s) + " GB")
    tk.Label(lf15, text = "Path\t: ", font=('calibri', 12, 'bold'), fg='yellow', bg="grey30").place(x=10, y=10)
    link5 = tk.Label(lf15, text = folder_path, font=('calibri', 12, 'bold'), fg='yellow', bg="grey30", 
             width=50, height=5, wraplength=400, anchor='nw', cursor="hand2")
    link5.place(x=90, y=10)    
    fp = os.path.realpath(folder_path)
    link5.bind("<Button-1>", lambda event: os.startfile(fp))    
    
    tk.Label(lf15, text = "Folders\t:   " + str(folder_count), font=('calibri', 12, 'bold'), fg="white", bg="grey30").place(x=10, y=150)
    tk.Label(lf15, text = "Files\t:   " + str(file_count), font=('calibri', 12, 'bold'), fg="white", bg="grey30").place(x=10, y=180)
    tk.Label(lf15, text = "Size\t:   " + str(s) + " GB", font=('calibri', 12, 'bold'), fg="white", bg="grey30").place(x=10, y=210)
    
def launch(fp2):
    os.startfile(fp2)
    
def delete(fp3):
    
    delet = messagebox.askquestion("Warning!", "ALL FILES WILL BE LOST.\nAre you sure you want to proceed?", icon = 'warning')                                 
    if delet == 'yes':
        try:
            shutil.rmtree(fp3)
        except OSError as e:
            print("Error: %s : %s" % (fp3, e.strerror))
        back()
    global lf26, lf19

    
def create_folder(pf1, f2):
    global lf19, s
    print(pf1)
    print(f2.get())
    
    if not os.path.exists(pf1+f2.get()):
        os.makedirs(pf1+f2.get())
        tk.Label(lf19, text="Folder created successfully", font=('Halvetica', 12, 'bold'), fg="dark green", 
                 bg="grey30", width=40, height=2, wraplength=400).place(x=70, y=260)
        button25 = ttk.Button(lf19, text="Open", style = 'C.TButton', command = lambda: launch(pf1+f2.get()))
        button25.place(x=180, y=300)
        button26 = ttk.Button(lf19, text="Delete", style = 'E.TButton', command = lambda: delete(pf1+f2.get()))
        button26.place(x=280, y=300)
    else:
        tk.Label(lf19, text="Error: Folder already exists or you do not have write permission", font=('Halvetica', 12, 'bold'), fg='yellow', 
                 bg="grey30", width=40, height=2, wraplength=400).place(x=70, y=260)
        
def delete_folder(fp4):
    global lf26
    # Create Frame to get folder size
    lf26 = ttk.LabelFrame(root4, text = "Delete Entire Directory", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf26.place(x=850, y=140)
    frame12 = tk.Frame(lf26,width=550, height=430, bg = 'grey30').pack()
    
    tk.Label(lf26, text = "This operation will delete the Folder and all it's contents\nAre you sure you want to proceed?",
             font=('calibri', 14, 'bold'), fg='yellow', bg="grey30").place(x=30, y=10)
    button27 = ttk.Button(lf26, text="No", style = 'C.TButton', command = lambda: select_directory(0))
    button27.place(x=180, y=100)
    button28 = ttk.Button(lf26, text="Yes", style = 'E.TButton', command = lambda: delete(fp4))
    button28.place(x=280, y=100)
    
    
def new_folder(pf3):
    global root4, lf19
    # Create Frame to get folder size
    lf19 = ttk.LabelFrame(root4, text = "Create New Folder", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf19.place(x=850, y=140)
    frame11 = tk.Frame(lf19, width=550, height=430, bg = 'grey30').pack()
    
    tk.Label(lf19, text = "Folder will be created here: ", font=('calibri', 14, 'bold'), fg='yellow', bg="grey30").place(x=10, y=10)
    tk.Label(lf19, text = pf3, font=('calibri', 12, 'bold'), fg="white", bg="grey30", 
             width=50, height=5, wraplength=400, anchor='nw', cursor="hand2").place(x=10, y=40)  
    
    tk.Label(lf19, text="Enter Folder Name:", font=('Halvetica', 12, 'bold'), fg="white", bg="grey30").place(x=10, y=150)
    new_fol= tk.StringVar()

    tk.Entry(lf19, textvariable = new_fol, width=50, highlightthickness=2, highlightbackground = "black", highlightcolor= "black").place(x=180, y=150)
    print(new_fol.get())
    button18 = ttk.Button(lf19, text="Create Folder", style = 'S.TButton', command = lambda: create_folder(pf3, new_fol))
    button18.place(x=180, y=200)
    
        
    
def back():
    global path, listbox1
    print("Directory to crop: ", path)  
    if len(path) == 3:
        search()
    else:        
        pos = path.count('\\')
        c=1
        new_path = ''
        for letter in path:
            if letter == '\\':
                if c<pos-1:
                    new_path = new_path + letter
                else:
                    break
                c=c+1            
            else:
                new_path = new_path + letter            
        new_path = new_path + '\\'      
        path = new_path    
        print('Path after crop: ', path)
        listbox1 = None
        select_directory(0)

def scrollbar2(x, y):
    global listbox1
    listbox1.yview(x,y)
    
def interim(event1):
    global listbox, root4, listbox1, dirs, drive_selected, directory_selected, path, paths, lf10
    drive_selected = listbox.get(tk.ANCHOR)
    select_directory(0)
        

def select_directory(event11):    
    global listbox, root4, listbox1, dirs, drive_selected, directory_selected, path, paths, lf10
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')       
    
    # Create Frame to get folder size
    lf15 = ttk.LabelFrame(root4, text = "Folder Operations", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf15.place(x=850, y=140)
    frame10 = tk.Frame(lf15, width=550, height=430, bg = 'grey30').pack()
    
    if directory_selected == '':
        path = drive_selected[1:3] + '\\'
        
    tk.Label(root4, text='Drive Selected: ' + drive_selected[1:3] + '\\', font=('Halvetica', 12, 'bold'), fg='yellow', bg="grey20").place(x=40, y=110)
    
    lf20 = ttk.LabelFrame(root4, text = "Disk Utilization", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf20.place(x=40, y=457)
    frame5 = tk.Frame(lf20, width=196, height=110, bg = 'grey20')
    frame5.pack() 
    
    stats1 = shutil.disk_usage(drive_selected[1:3] + '\\')
    total1 = round(stats1[0] /1024 / 1024 / 1024 , 1)
    used1 = round(stats1[1] /1024 / 1024 / 1024 , 1)
    free1 = round(stats1[2] /1024 / 1024 / 1024 , 2)
    percent_free1 = round((free1/total1)*100, 1)

    tk.Label(frame5, text = 'Total: ' + str(total1) + ' GB', font=('Halvetica', 10, 'bold'), fg="yellow", bg="grey20").place(x=5, y=5)
    tk.Label(frame5, text = 'Free : ' + str(free1) + ' GB  (' + str(percent_free1) + ' %)', font=('Halvetica', 10, 'bold'), fg="yellow", bg="grey20").place(x=5, y=25)
    
    fr = '#'*int(20*((100-percent_free1)/100))
    to = '#'*20

    tk.Label(frame5, text = to, font=('Halvetica', 12, 'bold'), fg="green", bg="green").place(x=5, y=65)
    tk.Label(frame5, text = fr, font=('Halvetica', 12, 'bold'), fg="red", bg="red").place(x=5, y=65)
    
    try:
        directory_selected = listbox1.get(tk.ANCHOR)
        path = path +  directory_selected + '\\'        
        print("Directory Selected: ", path)
        paths = os.listdir(path)
        
    except:
        try:
            paths = os.listdir(path)
            print("Drive Selected: ", path)
        except:
            os.startfile(path)
            back()

    dirs = []
    for directory in paths:
        if directory[0].isalnum():
            dirs.append(directory)    
    print(dirs)
        
    # Auto Complete Listbox for Application Search based on key words entered by user
    tk.Label(root4, text="Search:", font=('Halvetica', 12, 'bold'), fg="white", bg="grey20").place(x=270, y=70)
    entry = tk.Entry(root4,width=25,font=('Helvetica', 13), bg='grey30', 
                     highlightthickness=2, highlightbackground = "black", highlightcolor= "black")
    entry.place(x=350, y=70)
    entry.bind('<KeyRelease>', on_keyrelease1)
    
    lf = ttk.LabelFrame(root4, text = "Directories / Files", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=180, relief=tk.SUNKEN)
    lf.place(x=270, y=140)
    frame1 = tk.Frame(lf, width=300, height=500, bg = 'grey30')
    frame1.pack()    

    scroll = tk.Scrollbar(frame1)
    listbox1 = tk.Listbox(frame1,width=55,height=25,font=('Helvetica',10, 'bold'), bg='grey30', fg='white', yscrollcommand = scroll.set)
    
    listbox_update1(dirs)
    
    listbox1.pack(side=tk.LEFT, fill=tk.BOTH)        
    scroll.config(command = scrollbar2)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)  
    
    # Back Button  
    choose = ttk.Button(root4, text="Back", style = 'C.TButton', command = back)    
    choose.place(x=605,y=70)
    
    tk.Label(root4, text="Path: " + path, width=100, height=1, font=('Halvetica', 12, 'bold'), fg='dark blue', anchor="w").place(x=270, y=10)
    tk.Label(root4, text="Current Folder: " + path.split('\\')[-2] + '\\', width=40, height=1, font=('Halvetica', 12, 'bold'), fg='yellow', bg="grey20", anchor="w").place(x=270, y=110)
          
    fp1 = os.path.realpath(path)
    button10 = ttk.Button(root4, text="Open", style = 'C.TButton', command = lambda: launch(path))
    button10.place(x=725, y=200)
    
    button10 = ttk.Button(root4, text="Filter", style = 'C.TButton', command = lambda: browse_dir(path))
    button10.place(x=725, y=250)
    
    button10 = ttk.Button(root4, text="Properties", style = 'C.TButton', command = lambda: properties(path))
    button10.place(x=725, y=300)
    
    button10 = ttk.Button(root4, text="New Folder", style = 'C.TButton', command = lambda: new_folder(path))
    button10.place(x=725, y=350)
    
    button10 = ttk.Button(root4, text="Delete", style = 'E.TButton', command = lambda: delete_folder(path))
    button10.place(x=725, y=400)
    
#########################################################################################################################    

# Function to filter application based on usr entered keywords
def on_keyrelease(event):
    global available_drives, volume_labels, data, drive_paths, directory_selected
    directory_selected=''
    value = event.widget.get()
    value = value.strip().lower()    
    if value == '':
        data = drive_paths
    else:
        data = []
        for item in drive_paths:
            if value in item.lower():
                data.append(item)         
    listbox_update(data)
    
# Function to display searched items in Application List Box   
def listbox_update(data):    
    global directory_selected
    listbox.delete(0, 'end')    
    for item in data:
        listbox.insert('end', item)
    directory_selected=''
    listbox.bind('<Double-1>', interim)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)
    
def scrollbar(x1, y1):
    global listbox
    listbox.yview(x1,y1)
    
def browse_directory():    
    global fol, browse_folder, path, drive_selected, listbox1, directory_selected
    fol = filedialog.askdirectory()
    browse_folder.set(fol)
    print("Browsed Folder: ", fol)
    path=fol
    drive_selected=fol
    select_directory(0)    

def search():    
    global root0, root, root1, root2, root3, root4, root5, root6, s, available_drives, volume_labels
    global listbox, drive_paths, directory_selected, path, paths, drive_selected, lf10, browse_folder
    directory_selected=''
    try: del path
    except: pass
    try: del paths
    except: pass
    try: del drive_selected
    except: pass
    try: del listbox
    except: pass
       
    s = ttk.Style()
    s.configure('TLabelframe.Label', font=('Arial Bold', 12), foreground ='dark blue')
    
    button9 = ttk.Button(root4, text="Reset", style = 'E.TButton', command = search)
    button9.place(x=1330, y=10)
    
    # Create Frame to Search by Folder Name
    lf10 = ttk.LabelFrame(root4, text = "File Explorer", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf10.place(x=10, y=40)
    tk.Frame(lf10, width=1420, height=570, bg = 'grey20').pack()   
        
    tk.Label(root4, text='Drive Selected: NA' , font=('Halvetica', 12, 'bold'), fg='yellow', bg="grey20").place(x=40, y=110)
    tk.Label(root4, text="Path: NA", width=100, height=1, font=('Halvetica', 12, 'bold'), fg='red', anchor="w").place(x=270, y=10)
    
    # Auto Complete Listbox for Application Search based on key words entered by user
    tk.Label(root4, text="Search:", font=('Halvetica', 12, 'bold'), fg="white", bg="grey20").place(x=40, y=70)
    entry = tk.Entry(root4,width=13,font=('Helvetica', 13), bg='grey30', fg='white', highlightthickness=2, highlightbackground = "black", highlightcolor= "black")
    entry.place(x=120, y=70)
    entry.bind('<KeyRelease>', on_keyrelease)
    
    lf1 = ttk.LabelFrame(root4, text = "Drives", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=180, relief=tk.SUNKEN)
    lf1.place(x=40, y=140)
    frame2 = tk.Frame(lf1, width=200, height=500, bg = 'grey30')
    frame2.pack()    

    scroll2 = tk.Scrollbar(frame2)
    
    listbox = tk.Listbox(frame2,width=25, height=16,font=('Helvetica',10,'bold'), bg='grey30', fg='light blue', yscrollcommand=scroll2.set)
    listbox_update(drive_paths)
    
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)        
    scroll2.config(command = scrollbar)
    scroll2.pack(side=tk.RIGHT, fill=tk.Y) 
    

####################################################################################################################################################
# Youtube-Downloader
####################################################################################################################################################

def open_folder(): 
    os.system('start "dir" """C:\\Youtube_Downloads')

def download(url):
    from urllib.request import build_opener
    opener = build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    global root1
    print(url.get())
    SAVE_PATH = "c:\\Youtube_Downloads" 
    
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)
        
    try:
        YouTube(url.get()).streams[0].download(SAVE_PATH)
    except:
        tk.Label(root1, text="HTTP Error 503: Service Unavailable!!", font=('Halvetica', 12, 'bold'), fg="white").place(x=540, y=200)
    else:    
        tk.Label(root1, text="Downloaded!!", font=('Halvetica', 12, 'bold'), fg="white").place(x=600, y=200)
    finally:
        ttk.Button(root1, text = "Open Folder", command = open_folder, style = "S.TButton").place(x=600, y=250)
    

def youtube():
    global root1
    url= tk.StringVar()
    tk.Label(root1, text="Enter Video URL: ", font=('Halvetica', 12, 'bold'), fg="white").place(x=250, y=50)
    tk.Entry(root1, textvariable = url, width=100).place(x=420, y=50)
    print(url.get())
    button8 = ttk.Button(root1, text="Download", style = 'S.TButton', command = lambda: download(url))
    button8.place(x=600, y=100)
    

####################################################################################################################################################
# Robo-Copy
####################################################################################################################################################
              
def browse_source():

    global source_folder_path, dest_folder_path
    global root, filename, ll1, ll2, ll3, lbl2, button3
    
    ll1 = tk.Label(root, text = "Number of Sub-Folders                                                  : " , font=('calibri', 12, 'bold'), fg="grey20", bg="grey20").place(x=650, y=125)
    ll2 = tk.Label(root, text = "Number of Files                                                        : " , font=('calibri', 12, 'bold'), fg="grey20", bg="grey20").place(x=650, y=150)
    ll3 = tk.Label(master=root, text = "Total Size                                                      : " , font=('calibri', 12, 'bold'), fg="grey20", bg="grey20").place(x=650, y=175)
        
    filename = filedialog.askdirectory()
    source_folder_path.set(filename)
    print("Source Folder Path                       : ", filename)
    
    # Get number of files and folders in the chosen directory
    source_folder_count = 0
    source_file_count = 0
    for home, dirs, files in os.walk(filename):
        source_folder_count += len(dirs)
        source_file_count += len(files)
        
    print("Number of Folders inside Source Directory: ", source_folder_count, type(source_folder_count))
    print("Number of Files inside Source Directory  : ", source_file_count, type(source_file_count))
       
    root_directory = Path(filename)
    size = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())
 
    # display size
    p = math.pow(1024, 3)
    s = round(size / p, 3)
    print("Size of Source Directory                 : " + str(s) + " GB")
    ll1 = tk.Label(root, text = "Number of Sub-Folders: " + str(source_folder_count), font=('calibri', 12, 'bold'), fg="white", bg="grey20").place(x=650, y=125)
    ll2 = tk.Label(root, text = "Number of Files             : " + str(source_file_count), font=('calibri', 12, 'bold'), fg="white", bg="grey20").place(x=650, y=150)
    ll3 = tk.Label(master=root, text = "Total Size                       : " + str(s) + " GB", font=('calibri', 12, 'bold'), fg="white", bg="grey20").place(x=650, y=175)
    
    # Browse Destination Folder
    tk.Label(root, text = "Browse Destination Folder :", font=('calibri', 14, 'bold'), fg="white", bg="grey20").place(x=130, y=240)
    dest_folder_path = tk.StringVar()
    lbl2 = tk.Label(master=root, textvariable=dest_folder_path, font=('calibri', 12, 'bold'), fg="white", bg="grey20")
    lbl2.place(x=650, y=240)
    button3 = ttk.Button(root, text="Browse", style = 'S.TButton', command = browse_dest)
    button3.place(x=400, y=235)
    
    
def get_free_space(dirname):
    
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return round(free_bytes.value / 1024 / 1024 / 1024, 3)
    else:
        st = os.statvfs(dirname)
        return round(st.f_bavail * st.f_frsize / 1024 / 1024, 3)
    
def copy():
    global filename1, filename
    print("Source      : ", filename)
    print("Destination : ", filename1)
    copy = 'start cmd /K robocopy ' + '"' + filename + '" "' + filename1 + '" /Z /E'    
    print(copy)
    try:
        os.system(copy)
    except:
        tk.Label(root, text="Error: Please check for necessary permissions and/or available disk space", font=('calibri', 14, 'bold'), fg='yellow', bg="grey20").place(x=400, y=365)
    else:
        tk.Label(root, text="Copy Initiated", font=('calibri', 14, 'bold'), fg='yellow', bg="grey20").place(x=400, y=365)
        
def copy_delete():
    global filename1, filename
    print("Source      : ", filename)
    print("Destination : ", filename1)
    
    copy_and_delete = 'start cmd /K robocopy ' + '"' + filename + '" "' + filename1 + '" /MIR'    
    print(copy_and_delete)
    try:
        os.system(copy_and_delete)
    except:
        tk.Label(root, text="Error: Please check for necessary permissions and/or available disk space", font=('calibri', 14, 'bold'), fg='yellow', bg="grey20").place(x=400, y=365)
    else:
        tk.Label(root, text="Mirroring Initiated", font=('calibri', 14, 'bold'), fg='yellow', bg="grey20").place(x=400, y=460)
    
    
def browse_dest():
    global dest_folder_path, filename1
    global root
    filename1 = filedialog.askdirectory()
    dest_folder_path.set(filename1)
    free_space = get_free_space(filename1)
    tk.Label(master=root, text="Available space in Destination: " + str(free_space) + " GB", font=('calibri', 12, 'bold'), fg="white", bg="grey20").place(x=650, y=270)
    button4 = ttk.Button(root, text="Initiate Copy", style = 'S.TButton', command = copy)
    button4.place(x=400, y=330)
    tk.Label(root, text="Only copies delta files from Source to Destination. Does not delete Extra Files from Destination", 
             font=('calibri', 12, 'bold'), fg="orange", bg="grey20", anchor='nw').place(x=650, y=330)
    tk.Label(root, text="Use this only for First / Initial Mirroring", 
             font=('calibri', 12, 'bold'), fg='yellow', bg="grey20", anchor='nw').place(x=650, y=360)
    button5 = ttk.Button(root, text="Initiate Mirroring", style = 'S.TButton', command = copy_delete)
    button5.place(x=400, y=425)
    tk.Label(root, text="Copies delta files from Source to Destination. Deletes Extra Files from Destination, not present in Source", 
             font=('calibri', 12, 'bold'), fg="orange", bg="grey20", anchor='nw').place(x=650, y=425)
    tk.Label(root, text="Use this for Subsequent Mirroring", 
             font=('calibri', 12, 'bold'), fg='yellow', bg="grey20", anchor='nw').place(x=650, y=455)
    
    
def robo_copy():    
    global root0, root, root1, root2, root3, root4, root5, root6, s
    global source_folder_path, dest_folder_path, ll1, ll2, ll3, lbl2, button3

    s = ttk.Style()
    s.configure('TLabelframe.Label', font=('Arial Bold', 12), foreground ='dark blue')
    
    # Create Frame to browse Folder Path
    lf5 = ttk.LabelFrame(root, text = "Robust File Copy for Windows", style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf5.place(x=10, y=40)
    tk.Frame(lf5, width=1420, height=570, bg = 'grey20').pack()
    
    # Browse Source Folder
    tk.Label(root, text = "Browse Source Folder :", font=('calibri', 14, 'bold'), fg="white", bg="grey20").place(x=130, y=100)
    source_folder_path = tk.StringVar()
    
    lbl1 = tk.Label(master=root, textvariable=source_folder_path, font=('calibri', 12, 'bold'), fg="white", bg="grey20")
    lbl1.place(x=650, y=100)
    
    button2 = ttk.Button(root, text="Browse", style = 'S.TButton', command = browse_source)
    button2.place(x=400, y=95)
    
    button3 = ttk.Button(root, text="Refresh", style = 'C.TButton', command = robo_copy)
    button3.place(x=1330, y=10)
    

####################################################################################################################################################
# Home Screen
####################################################################################################################################################

def scrollbar(x, y):                                                            # Scrollbar for Volume Label Textbox
    global textbox_license
    textbox_license.yview(x,y)
    
def home_screen():    
    
    global c, yy, name, site, country, dept, drives, available_drives, volume_labels, drive_paths
    s = ttk.Style()
    # s.theme_use('default')
    s.configure('TLabelframe.Label', font=('Arial Bold', 10), foreground ='dark blue')
 
    drives = ['c:', 'd:', 'e:', 'f:', 'g:', 'h:', 'i:', 'j:', 'k:', 'l:', 'm:', 'n:', 'o:', 'p:', 'q:', 'r:', 's:', 't:', 'u:', 'v:', 'w:', 'x:', 'y:', 'z:']
    drives = [d.upper() for d in drives]
    df = pd.DataFrame(columns = ['Drive', 'Volume Label', 'Total Space (TB)', 'Used (TB)', 'Free (TB)', '% Free'])
    available_drives = []
    volume_labels = []
    drive_paths = []
    for drive in drives:
      
        try:
            stats = shutil.disk_usage(drive)
            available_drives.append(drive)
            volume_label = win32api.GetVolumeInformation(drive + "\\")
            volume_labels.append(volume_label[0])
            drive_path = '(' + drive + ')'
            vol = volume_label[0]
            drive_paths.append(drive_path + '   ' + volume_label[0])
       
            total = round(stats[0] /1024 / 1024 / 1024 , 1)
            used = round(stats[1] /1024 / 1024 / 1024 , 1)
            free = round(stats[2] /1024 / 1024 / 1024 , 2)
            percent_free = round((free/total)*100, 1)
            new_row = [drive_path, vol, total, used, free, percent_free]
            df.loc[len(df)] = new_row
            
        except:
            pass
        
    print(df)    
    
    # Frame for Volume Label Info
    tim = time.strftime("%d-%m-%Y  %H:%M:%S")    
    lf6 = ttk.LabelFrame(root0, text = "Volume Label Information at  " + tim, style="TLabelframe", 
                         labelanchor=tk.NW, height=50, width=150, relief=tk.SUNKEN)
    lf6.place(x=10, y=40)
    frame = tk.Frame(lf6, width=1420, height=570, bg = 'grey20')
    frame.pack()  
    
    lists = df.values.tolist()
    r=1
    c=1
    n=1
    for row in lists:
        
        if row[2] > 1024:
            tk.Label(lf6, text= str(round(row[4]/1024, 2)) + ' TB of ' + str(round(row[2]/1024, 2)) + ' TB Free', font=('arial bold', 10, 'bold'), fg="white", bg="grey20").place(x=-180 + (225*c), y= -50 + (125)*r)
        else:
            tk.Label(lf6, text= str(row[4]) + ' GB of ' + str(row[2]) + ' GB Free', font=('arial bold', 10, 'bold'), fg="white", bg="grey20").place(x=-180 + (225*c), y= -50 + (125)*r)
        
        fr = '.'*int(50*((100-row[5])/100))
        to = '.'*50
        dr=row[0][1:3] + '\\'
    
        l00 = tk.Label(lf6, text = to, font=('Halvetica', 12, 'bold'), fg="light grey", bg="light grey", borderwidth=1, relief="solid", cursor="hand2")
        l00.place(x=-180 + (225*c), y=-75 + (125)*r) 
        l00.bind("<Button-1>", lambda e, url = dr:os.startfile(url))
            
        if row[5] >= 20:
            l11 = tk.Label(lf6, text = fr, font=('Halvetica', 12, 'bold'), fg="dark green"  , bg="dark green" , borderwidth=1, relief="solid" , cursor="hand2")
            l11.place(x=-180 + (225*c), y=-75 + (125)*r)   
            l11.bind("<Button-1>", lambda e, url = dr:os.startfile(url))
        elif row[5] < 20 and row[5] >= 10:
            l22 = tk.Label(lf6, text = fr, font=('Halvetica', 12, 'bold'), fg="orange"  , bg="orange" , borderwidth=1, relief="solid" , cursor="hand2")
            l22.place(x=-180 + (225*c), y=-75 + (125)*r)   
            l22.bind("<Button-1>", lambda e, url = dr:os.startfile(url))
        else:
            l33 = tk.Label(lf6, text = fr, font=('Halvetica', 12, 'bold'), fg='red'  , bg="red" , borderwidth=1, relief="solid", cursor="hand2" )
            l33.place(x=-180 + (225*c), y=-75 + (125)*r)   
            l33.bind("<Button-1>", lambda e, url = dr:os.startfile(url))
        
        link55 = tk.Label(lf6, text = row[0] + '  ' + row[1], font=('arial bold', 10, 'bold'), fg="white", bg="grey20", cursor="hand2",
                          width=22, height=1, wraplength=100, anchor='nw')
        link55.place(x=-180 + (225*c), y= -100 + (125)*r)
        link55.bind("<Button-1>", lambda e, url = dr:os.startfile(url))  
                
        n = n+1
        if c == 6:
            r += 1
            c = 1
        else:
            c += 1            
        
    button7 = ttk.Button(root0, text="Refresh", style = 'C.TButton', command = home_screen)
    button7.place(x=1330, y=10)   

####################################################################################################################################################
# Define Tabs
####################################################################################################################################################

def tabs():    
    global root0, root, root1, root2, root3, root4, root5, root6, s, note

    noteStyle = ttk.Style()
    noteStyle.theme_use('winnative')
    noteStyle.configure("TNotebook", background="grey12", borderwidth=1)
    noteStyle.configure("TNotebook.Tab", background="grey12", borderwidth=3, font=('Arial Bold', 10))

    noteStyle.map('TNotebook.Tab', background=[('selected', 'Grey'), ('active', 'grey30'), ('!active', 'grey80')])    
    note =  ttk.Notebook(gui, width = 1440, height = 640, style = "TNotebook") 
    
    root0 = ttk.Frame(note)
    root  = ttk.Frame(note) 
    #root1 = ttk.Frame(note)
    root2 = ttk.Frame(note)
    root3 = ttk.Frame(note)
    root4 = ttk.Frame(note)
    root5 = ttk.Frame(note)
    root6 = ttk.Frame(note)
    
    note.add(root0, text = '       Home      ')
    note.add(root,  text = '    Mirroring    ') 
    note.add(root4, text = '  File Explorer  ')          
    note.add(root2, text = '   File Filter   ') 
    #note.add(root1, text = 'Youtube-Downloader')
    note.add(root6, text = '    IMDB Sync    ')
    note.add(root3, text = '     Contact     ') 
    note.add(root5, text = '       Help      ')

    note.place(x=0, y=150) 

    home_screen()
    robo_copy()
    search()
    filter_files()
    #youtube()  
    imdb()
    contact()
    
    Help()
    
    # Configure Button Styles
    s = ttk.Style()
    s.theme_use('winnative')
    s.configure('D.TButton', font =('calibri', 14, 'bold'), foreground = 'black',  borderwidth = '10', width = 10)
    s.configure('I.TButton', font =('calibri', 14, 'bold'), foreground = 'grey75', borderwidth = '10', width = 13)
    s.configure('E.TButton', font =('calibri', 12, 'bold'), foreground = 'grey75', borderwidth = '10', width = 10)
    s.configure('C.TButton', font =('calibri', 12, 'bold'), foreground = 'grey75', borderwidth = '10', width = 10)
    s.configure('S.TButton', font =('calibri', 14, 'bold'), foreground = 'grey75', borderwidth = '10', width = 17, background = "grey30")
    
    s.map('D.TButton', foreground=[('!active', 'black'),  ('pressed', 'red'), ('active', 'blue')], background=[('pressed', 'green'), ('active', 'black') ])
    s.map('I.TButton', foreground=[('!active', 'grey75'), ('pressed', 'red'), ('active', 'blue')], background=[('pressed', 'green'), ('active', 'grey75')])
    s.map('E.TButton', foreground=[('!active', 'red'),  ('pressed', 'blue'), ('active', 'red')],  background=[('pressed', 'green'), ('active', 'grey75')])
    s.map('C.TButton', foreground=[('!active', 'blue'),  ('pressed', 'red'), ('active', 'blue')], background=[('pressed', 'green'), ('active', 'grey75')])
    s.map('S.TButton', foreground=[('!active', 'blue'),   ('pressed', 'red'), ('active', 'blue')], background=[('pressed', 'green'), ('active', 'black') ])
   

####################################################################################################################################################
# Main Code
####################################################################################################################################################

global application, listbox, graph_type, frame1, main_frame, lf

gui.geometry("1440x875")
gui.resizable(0,0)                     # Disables Maximise Button
gui.wm_iconbitmap(r"Images\bkp.ico")

gui.title("WIN-RoboFH")

gui.configure(bg="grey12")
tk.Label(gui, text="WIN-Robo-FH", font=('arial bold', 44, 'bold'), fg="yellow", bg="grey12").place(x=535, y=1)
tk.Label(gui, text="WINDOWS ROBUST FILE HANDLING", font=('ariel', 30, 'bold'), fg="yellow", bg="grey12").place(x=365, y=80)

# Set Status Bar at the bottom of the screen
statusvar = tk.StringVar()
statusvar.set(" Welcome to WIN-RoboFH - Windows Robust File Handling Tool" + "\t\t\t\t\t\t\t\t\t\t\t\t\t\tHost Name: " + host + "\t\tVCN ID: " + vcn)

sbar_l=tk.Label(gui, textvariable=statusvar,relief=tk.SUNKEN, anchor="w")
sbar_l.pack(side=tk.BOTTOM, fill="x")

image1 = PIL.Image.open("Images\\IMDB.jpg")
volvo = PIL.ImageTk.PhotoImage(image1)
label1 = tk.Label(image = volvo)
label1.image = volvo
label1.place(x=2, y=2)

image3 = PIL.Image.open("Images\\Synology.jpg")
cae = PIL.ImageTk.PhotoImage(image3)
label3 = tk.Label(image = cae)
label3.image = cae
label3.place(x=1202, y=2)

ttk.Button(gui, text="Exit", style = 'E.TButton', command = quit, width = 8).place(x=1360, y=820)

tabs()
gui.mainloop()
