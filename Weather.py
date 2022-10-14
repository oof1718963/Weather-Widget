from tkinter import *
import requests
import json

root = Tk()
root.title("Country API")
root.geometry("500x500")
root.configure(background = "Black")

city_name_label = Label(root,text = "Capital City Name",font = ("Arial",18,"bold"),bg = "#from tkinter import *
import requests
import json

root = Tk()
root.title("Country API")
root.geometry("500x500")
root.configure(background = "#7267f0")

city_name_label = Label(root,text = "Capital City Name",font = ("Arial",18,"bold"),bg = "#7267f0",fg = "white")
city_name_label.place(relx = 0.1,rely = 0.1,anchor = W)

city_entry = Entry(root)
city_entry.place(relx = 0.1,rely = 0.18,anchor = W)

country_name = Label(root,text = "Country:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
country_name.place(relx = 0.1,rely = 0.34,anchor = W)

region = Label(root,text = "Region:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
region.place(relx = 0.1,rely = 0.42,anchor = W)

languages = Label(root,text = "Language:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
languages.place(relx = 0.1,rely = 0.5,anchor = W)

population = Label(root,text = "Population:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
population.place(relx = 0.1,rely = 0.58,anchor = W)

area = Label(root,text = "Area:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
area.place(relx = 0.1,rely = 0.66,anchor = W)

def city_details():
    api_request = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    api_json_content = json.loads(api_request.content)
    
    country = api_json_content[0]["name"]
    reg = api_json_content[0]["region"]
    lang = api_json_content[0]["languages"][0]["name"]
    popn = api_json_content[0]["population"]
    country_area = api_json_content[0]["area"]
    
    country_name["text"] = "Country:" + str(country)
    region["text"] = "Region:" + str(reg)
    languages["text"] = "Language:" + str(lang)
    population["text"] = "Population:" + str(popn)
    area["text"] = "Area" + str(country_area)

search_btn = Button(root,text = "City Details",command = city_details,relief = FLAT,bg = "yellow")
search_btn.place(relx = 0.1,rely = 0.26,anchor = W)

root.mainloop()",fg = "white")
city_name_label.place(relx = 0.1,rely = 0.1,anchor = W)

city_entry = Entry(root)
city_entry.place(relx = 0.1,rely = 0.18,anchor = W)

country_name = Label(root,text = "Country:",font = ("Arial",10,"bold"),bg = "#from tkinter import *
import requests
import json

root = Tk()
root.title("Country API")
root.geometry("500x500")
root.configure(background = "#7267f0")

city_name_label = Label(root,text = "Capital City Name",font = ("Arial",18,"bold"),bg = "#7267f0",fg = "white")
city_name_label.place(relx = 0.1,rely = 0.1,anchor = W)

city_entry = Entry(root)
city_entry.place(relx = 0.1,rely = 0.18,anchor = W)

country_name = Label(root,text = "Country:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
country_name.place(relx = 0.1,rely = 0.34,anchor = W)

region = Label(root,text = "Region:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
region.place(relx = 0.1,rely = 0.42,anchor = W)

languages = Label(root,text = "Language:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
languages.place(relx = 0.1,rely = 0.5,anchor = W)

population = Label(root,text = "Population:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
population.place(relx = 0.1,rely = 0.58,anchor = W)

area = Label(root,text = "Area:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
area.place(relx = 0.1,rely = 0.66,anchor = W)

def city_details():
    api_request = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    api_json_content = json.loads(api_request.content)
    
    country = api_json_content[0]["name"]
    reg = api_json_content[0]["region"]
    lang = api_json_content[0]["languages"][0]["name"]
    popn = api_json_content[0]["population"]
    country_area = api_json_content[0]["area"]
    
    country_name["text"] = "Country:" + str(country)
    region["text"] = "Region:" + str(reg)
    languages["text"] = "Language:" + str(lang)
    population["text"] = "Population:" + str(popn)
    area["text"] = "Area" + str(country_area)

search_btn = Button(root,text = "City Details",command = city_details,relief = FLAT,bg = "yellow")
search_btn.place(relx = 0.1,rely = 0.26,anchor = W)

root.mainloop()",fg = "white")
country_name.place(relx = 0.1,rely = 0.34,anchor = W)

region = Label(root,text = "Region:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
region.place(relx = 0.1,rely = 0.42,anchor = W)

languages = Label(root,text = "Language:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
languages.place(relx = 0.1,rely = 0.5,anchor = W)

population = Label(root,text = "Population:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
population.place(relx = 0.1,rely = 0.58,anchor = W)

area = Label(root,text = "Area:",font = ("Arial",10,"bold"),bg = "#7267f0",fg = "white")
area.place(relx = 0.1,rely = 0.66,anchor = W)

def city_details():
    api_request = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    api_json_content = json.loads(api_request.content)
    
    country = api_json_content[0]["name"]
    reg = api_json_content[0]["region"]
    lang = api_json_content[0]["languages"][0]["name"]
    popn = api_json_content[0]["population"]
    country_area = api_json_content[0]["area"]
    
    country_name["text"] = "Country:" + str(country)
    region["text"] = "Region:" + str(reg)
    languages["text"] = "Language:" + str(lang)
    population["text"] = "Population:" + str(popn)
    area["text"] = "Area" + str(country_area)

search_btn = Button(root,text = "City Details",command = city_details,relief = FLAT,bg = "yellow")
search_btn.place(relx = 0.1,rely = 0.26,anchor = W)

root.mainloop()
