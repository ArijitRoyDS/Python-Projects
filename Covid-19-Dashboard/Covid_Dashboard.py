import requests
import tkinter as tk
from tkinter import ttk, Frame

def report(d):
    district = d.get()
    
    lf3 = ttk.LabelFrame(gui, text = "District Data: " + district, style = "Red.TLabelframe")
    lf3.place(x=690, y=350)
    Frame(lf3, width=670, height=380, background = 'Light Blue').pack()
    
    try:
        dist_pop = data[state_code]["districts"][district]["meta"]["population"]
        dist_v1 = data[state_code]["districts"][district]["total"]["vaccinated1"]
        dist_v2 = data[state_code]["districts"][district]["total"]["vaccinated2"]
        dist_v1_p = (dist_v1/dist_pop)*100
        dist_v2_p = (dist_v2/dist_pop)*100
    except:
        pass    
    
    yy = 430

    try:
        for key, value in data[state_code]["districts"][district]["delta"].items():
             tk.Label(gui, text="Today's Report: " + date1, font=('Calibri Bold', 16), fg="dark blue", bg="Light Blue").place(x=700, y=380)    
             p1 = key.replace('{', " ")
             p1 = p1.replace('}', " ")
             tk.Label(gui, text=p1, font=('Calibri Bold', 14), fg="Black", bg="Light Blue").place(x=700, y=yy)  
             tk.Label(gui, text=value, font=('Calibri', 14), fg="Black", bg="Light Blue").place(x=900, y=yy)  
             yy = yy+30
    except:
        tk.Label(gui, text="Today's Data Upload is in Progress\nPlease Try After Sometime", font=('Calibri Bold', 15), fg="red", bg="Light Blue").place(x=700, y=450)
    cnf, dead, rec = 0, 0, 0     
    yy = 430
    for key, value in data[state_code]["districts"][district]["total"].items():
         tk.Label(gui, text="Cumulative Till Date", font=('Calibri Bold', 16), fg="dark blue", bg="Light Blue").place(x=1050, y=380)          

         p1 = key.replace('{', " ")
         p1 = p1.replace('}', " ")
         
         if p1 == "confirmed":
             cnf = value
         if p1 == "deceased":
             dead = value
         if p1 == "recovered":
             rec = value
             
         tk.Label(gui, text=p1, font=('Calibri Bold', 14), fg="Black", bg="Light Blue").place(x=1050, y=yy)  
         tk.Label(gui, text=value, font=('Calibri', 14), fg="Black", bg="Light Blue").place(x=1250, y=yy)  
         yy = yy+30
    try:     
        active = cnf-dead-rec
        rec_rate = (rec/cnf)*100
    except:
        tk.Label(gui, text="District wise break up is not available", font=('Calibri Bold', 20), fg="Red", bg="Light Blue").place(x=700, y=650)
        return()
    tk.Label(gui, text="Active Caseload: " + str(active), font=('Calibri Bold', 20), fg="Red", bg="Light Blue").place(x=700, y=660)
    tk.Label(gui, text="Recovery Rate  : " + str(round(rec_rate,1)) + " %", font=('Calibri Bold', 20), fg="Dark Green", bg="Light Blue").place(x=700, y=700)
    tk.Label(gui, text="Population: " + str(dist_pop), font=('Calibri Bold', 20), fg="brown", bg="Light Blue").place(x=1020, y=660)
    tk.Label(gui, text="Vaccination: ", font=('Calibri Bold', 20), fg="Dark Green", bg="Light Blue").place(x=1020, y=700)    
    tk.Label(gui, text="Dose 1: " + str(round(dist_v1_p,1)) + " %" + "\nDose 2:   " + str(round(dist_v2_p,1)) + " %", font=('Calibri Bold', 14), fg="Dark Green", bg="Light Blue").place(x=1180, y=695)
              
    

def select_district(s):
    state = s.get()
    global key, data, gui, state_code, date1
    
    lf2 = ttk.LabelFrame(gui, text = "State Data: " + state, style = "Red.TLabelframe")
    lf2.place(x=10, y=350)
    Frame(lf2, width=670, height=380, background = 'Light Blue').pack()
    
    lf3 = ttk.LabelFrame(gui, text = "District Data", style = "Red.TLabelframe")
    lf3.place(x=690, y=350)
    Frame(lf3, width=670, height=380, background = 'Light Blue').pack()
    
    if   state == "Andaman & Nicobar Islands":          state_code = "AN"
    elif state == "Andhra Pradesh":                     state_code = "AP"
    elif state == "Arunachal Pradesh":                  state_code = "AR"
    elif state == "Assam":                              state_code = "AS"
    elif state == "Bihar":                              state_code = "BR"
    elif state == "Chandigarh":                         state_code = "CH"
    elif state == "Chattisgarh":                        state_code = "CT"
    elif state == "Dadra & Nagar Haveli \ Daman & Diu": state_code = "DN"
    elif state == "Delhi":                              state_code = "DL"
    elif state == "Goa":                                state_code = "GA"
    elif state == "Gujarat":                            state_code = "GJ"
    elif state == "Haryana":                            state_code = "HR"
    elif state == "Himachal Pradesh":                   state_code = "HP"
    elif state == "Jammu & Kashmir":                    state_code = "JK"
    elif state == "Jharkhand":                          state_code = "JH"
    elif state == "Karnataka":                          state_code = "KA"
    elif state == "Kerala":                             state_code = "KL"
    elif state == "Ladakh":                             state_code = "LA"
    elif state == "Lakshadweep":                        state_code = "LD"
    elif state == "Madhya Pradesh":                     state_code = "MP"
    elif state == "Maharashtra":                        state_code = "MH"
    elif state == "Manipur":                            state_code = "MN"
    elif state == "Meghalaya":                          state_code = "ML"
    elif state == "Mizoram":                            state_code = "MZ"
    elif state == "Nagaland":                           state_code = "NL"
    elif state == "Odisha":                             state_code = "OR"
    elif state == "Puducherry":                         state_code = "PY"
    elif state == "Punjab":                             state_code = "PB"
    elif state == "Rajasthan":                          state_code = "RJ"
    elif state == "Sikkim":                             state_code = "SK"
    elif state == "Tamil Nadu":                         state_code = "TN"
    elif state == "Telangana":                          state_code = "TG"
    elif state == "Tripura":                            state_code = "TR"
    elif state == "Uttar Pradesh":                      state_code = "UP"
    elif state == "Uttarakhand":                        state_code = "UT"
    elif state == "West Bengal":                        state_code = "WB"   
        
    p1 = []
    dist = data[state_code]['districts']
    dist = list(dist.keys())    

    selected_dist = tk.StringVar(gui)      
    tk.Label(gui, text="Select District: ", font=('Calibri Bold', 16), fg="Black", bg="Light Blue").place(x=380, y=190)    
    cb1 = ttk.Combobox(gui, textvariable=selected_dist, width=35, height=20, values=dist, font=('Halvetica', 12))
    cb1.place(x=550, y=195)
    cb1.current(0)
    tk.Button(gui, text = "Submit", command = lambda: report(selected_dist), font=('Calibri Bold', 12), fg="white", bg="Dark Blue", width = 10).place(x=950, y=190)

    cnf, dead, rec = 0, 0, 0
    yy = 430
    try:
        state_pop = data[state_code]["meta"]["population"]
        state_v1 = data[state_code]["total"]["vaccinated1"]
        state_v2 = data[state_code]["total"]["vaccinated2"]
        state_v1_p = (state_v1/state_pop)*100
        state_v2_p = (state_v2/state_pop)*100
    except:
        pass
    try:
        for key, value in data[state_code]['delta'].items():
             date1 = data[state_code]["meta"]["date"]
             tk.Label(gui, text="Today's Report: " + date1, font=('Calibri Bold', 16), fg="dark blue", bg="Light Blue").place(x=20, y=380)
             
             p1 = key.replace('{', " ")
             p1 = p1.replace('}', " ")
  
             tk.Label(gui, text=p1, font=('Calibri Bold', 14), fg="Black", bg="Light Blue").place(x=20, y=yy)  
             tk.Label(gui, text=value, font=('Calibri', 14), fg="Black", bg="Light Blue").place(x=220, y=yy)  
             yy = yy+30
    except:
        tk.Label(gui, text="Today's Data Upload is in Progress\nPlease Try After Sometime", font=('Calibri Bold', 15), fg="red", bg="Light Blue").place(x=20, y=450)
         
    yy = 430
    for key, value in data[state_code]['total'].items():
         tk.Label(gui, text="Cumulative Till Date", font=('Calibri Bold', 16), fg="dark blue", bg="Light Blue").place(x=350, y=380)
         
         p1 = key.replace('{', " ")
         p1 = p1.replace('}', " ")         
                      
         if p1 == "confirmed":
             cnf = value
         if p1 == "deceased":
             dead = value
         if p1 == "recovered":
             rec = value

         tk.Label(gui, text=p1, font=('Calibri Bold', 14), fg="Black", bg="Light Blue").place(x=350, y=yy)  
         tk.Label(gui, text=value, font=('Calibri', 14), fg="Black", bg="Light Blue").place(x=550, y=yy)  
         yy = yy+30
         
    active = cnf-dead-rec
    rec_rate = (rec/cnf)*100
    tk.Label(gui, text="Active Caseload: " + str(active), font=('Calibri Bold', 20), fg="Red", bg="Light Blue").place(x=20, y=660)
    tk.Label(gui, text="Recovery Rate  : " + str(round(rec_rate,1)) + " %", font=('Calibri Bold', 20), fg="Dark Green", bg="Light Blue").place(x=20, y=700)
    tk.Label(gui, text="Population: " + str(state_pop), font=('Calibri Bold', 20), fg="brown", bg="Light Blue").place(x=350, y=660)
    tk.Label(gui, text="Vaccination: ", font=('Calibri Bold', 20), fg="Dark Green", bg="Light Blue").place(x=350, y=700)    
    tk.Label(gui, text="Dose 1: " + str(round(state_v1_p,1)) + " %" + "\nDose 2:   " + str(round(state_v2_p,1)) + " %", font=('Calibri Bold', 14), fg="Dark Green", bg="Light Blue").place(x=520, y=695)
         

def home():
    
    global data
    response = requests.get("https://api.covid19india.org/v4/min/data.min.json", verify=False)
    data = response.json()
    # key1 = list(data.keys())
    # key1.remove('TT')
    
    india_cnf = data['TT']["total"]["confirmed"]
    india_rec = data['TT']["total"]["recovered"]
    india_dead = data['TT']["total"]["deceased"]
    india_oth = data['TT']["total"]["other"]
    india_active = india_cnf-india_rec-india_dead-india_oth
    v1 = data['TT']["total"]["vaccinated1"]
    v2 = data['TT']["total"]["vaccinated2"]
    dat = data['TT']["meta"]["date"]
    pop = data['TT']["meta"]["population"]
    
    pv1 = (v1/pop)*100
    pv2 = (v2/pop)*100
    
    try:
        india_cnf_today = data['TT']["delta"]["confirmed"]
        india_dead_today = data['TT']["delta"]["deceased"]
        india_rec_today = data['TT']["delta"]["recovered"]
        india_active_today = india_cnf_today-india_dead_today-india_rec_today
    except:
        india_cnf_today = 0
        india_dead_today = 0
        india_rec_today = 0
        india_active_today = 0
        

    
    global s
    s = ttk.Style()  
    s.configure('Red.TLabelframe.Label', font=('Arial Bold', 16), foreground ='Dark Blue')
    
    lf1 = ttk.LabelFrame(gui, text = "Choose State and District", style = "Red.TLabelframe")
    lf1.place(x=10, y=100)
    Frame(lf1, width=1346, height=210, background = 'Light Blue').pack()
    
    lf2 = ttk.LabelFrame(gui, text = "State Data", style = "Red.TLabelframe")
    lf2.place(x=10, y=350)
    Frame(lf2, width=670, height=380, background = 'Light Blue').pack()
    
    lf3 = ttk.LabelFrame(gui, text = "District Data", style = "Red.TLabelframe")
    lf3.place(x=690, y=350)
    Frame(lf3, width=670, height=380, background = 'Light Blue').pack()
    
    tk.Label(gui, text="Select State: ", font=('Calibri Bold', 16), fg="Black", bg="Light Blue").place(x=380, y=150)
    
    states_list = ["Andaman & Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh", "Chattisgarh", "Dadra & Nagar Haveli \ Daman & Diu",
              "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh",
              "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim",
              "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    
    selected_state = tk.StringVar(gui)  
    
    cb1 = ttk.Combobox(gui, textvariable=selected_state, width=35, height=20, values=states_list, font=('Halvetica', 12))
    cb1.place(x=550, y=155)
    cb1.current(0)
    
    tk.Label(gui, text="Last Updated:\n" + str(dat), font=('Calibri Bold', 16), fg="brown", bg="Light Blue").place(x=150, y=150) 
    tk.Label(gui, text="Population:\n" + str(pop), font=('Calibri Bold', 16), fg="brown", bg="Light Blue").place(x=1140, y=150) 
    
    tk.Label(gui, text="Confirmed: " + str(india_cnf), font=('Calibri Bold', 16), fg="brown", bg="Light Blue").place(x=20, y=250)  
    tk.Label(gui, text="Active   : " + str(india_active), font=('Calibri Bold', 16), fg="dark blue", bg="Light Blue").place(x=300, y=250)  
    tk.Label(gui, text="Recovery: " + str(india_rec), font=('Calibri Bold', 16), fg="dark green", bg="Light Blue").place(x=550, y=250)  
    tk.Label(gui, text="Deceased : " + str(india_dead), font=('Calibri Bold', 16), fg="red", bg="Light Blue").place(x=820, y=250)  
    tk.Label(gui, text="Vaccine  : " + str(v1+v2), font=('Calibri Bold', 16), fg="green", bg="Light Blue").place(x=1070, y=250) 
    
    tk.Label(gui, text=str(india_cnf_today), font=('Calibri Bold', 12), fg="brown", bg="Light Blue").place(x=100, y=280)  
    tk.Label(gui, text=str(india_active_today), font=('Calibri Bold', 12), fg="dark blue", bg="Light Blue").place(x=350, y=280)  
    tk.Label(gui, text=str(india_rec_today), font=('Calibri Bold', 12), fg="dark green", bg="Light Blue").place(x=620, y=280)  
    tk.Label(gui, text=str(india_dead_today), font=('Calibri Bold', 12), fg="red", bg="Light Blue").place(x=900, y=280)  
    tk.Label(gui, text="Dose 1: " + str(v1) + " (" + str(round(pv1, 1)) + " %)", font=('Calibri Bold', 12), fg="green", bg="Light Blue").place(x=1070, y=280) 
    tk.Label(gui, text="Dose 2: " + str(v2) + " (" + str(round(pv2, 1)) + " %)", font=('Calibri Bold', 12), fg="green", bg="Light Blue").place(x=1070, y=305) 
    
    tk.Button(gui, text = "Submit", command = lambda: select_district(selected_state), font=('Calibri Bold', 12), fg="white", bg="Dark Blue", width = 10).place(x=950, y=150)
    tk.Button(gui, text = "Refresh", command = lambda: home(), font=('Calibri Bold', 12), fg="white", bg="Dark Blue").place(x=1250, y=50)
    response.close()  

global gui
gui = tk.Tk()
gui.title("COVID-19 INDIA")
gui.geometry("1366x768")
gui.resizable(0,0)   
gui.configure(background='Light Blue')
tk.Label(gui, text="COVID-19 DASHBOARD", font=('Arial Bold', 54), fg="dark blue", bg="Light Blue").place(x=300, y=1)
home()
gui.mainloop() 

