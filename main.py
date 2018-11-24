#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:42:37 2018

@author: comrade
"""
import requests
import tmdbsimple as tmdb
import pandas
api_key="Enter your API Key here"

tmdb.API_KEY =api_key
search=tmdb.Search()
userquery=input("Enter your query : ")
response = search.movie(query=userquery)

for s in search.results:
    print(s['title'],s['id'])
    
movieid=input("Enter the id of the movie :")
print("What information do you want : ")
print("1.Primary info")
print("2.Cast")
print("3.Altrnative Titles")
print("4.Crew")
print("5.Images (posters, backdrops)")
print("6.Plot keywords")
print("7.Release information")
print("8.Trailers")
print("9.Reviews")
print ("10.Search new movie")
print("11.Exit")
choice = input("Enter the query no : ")

def caller(choice):
    switcher={
            "1":"https://api.themoviedb.org/3/movie/"+movieid+"?" + "api_key="+api_key +"&language=en-US",
            "2":"https://api.themoviedb.org/3/movie/"+movieid+"/credits?" + "api_key="+api_key +"&language=en-US",
            "3":"https://api.themoviedb.org/3/movie/"+movieid+"/alternativetitles?" + "api_key="+api_key +"&language=en-US",
            "4":"https://api.themoviedb.org/3/movie/"+movieid+"?" + "api_key="+api_key +"&language=en-US",
            "5":"https://api.themoviedb.org/3/movie/"+movieid+"/images?" + "api_key="+api_key +"&language=en-US",
            "6":"https://api.themoviedb.org/3/movie/"+movieid+"/keywords?" + "api_key="+api_key +"&language=en-US",
            "7":"https://api.themoviedb.org/3/movie/"+movieid+"/release_dates?" + "api_key="+api_key +"&language=en-US",
            "8":"https://api.themoviedb.org/3/movie/"+movieid+"/videos?" + "api_key="+api_key +"&language=en-US",
            "9":"https://api.themoviedb.org/3/movie/"+movieid+"/reviews?" + "api_key="+api_key +"&language=en-US",
            
            }
    return switcher.get(choice)

response=requests.get(caller(choice))
data=response.json()
data_df=data['cast']
columns = ['name']
df = pandas.DataFrame(columns=columns)

for name in data_df:
     df.loc[len(df)]=[name['name']]
     
df.head()

