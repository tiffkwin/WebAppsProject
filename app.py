import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, Response, render_template
import json
from project import app
from project.models.Zodiac import Zodiac
from project import db

def getAstrology(month, day, year):

    astro_sign = ""

    if month == 12:
        if day < 22:
            astro_sign = "Sagittarius"
        else:
         astro_sign ="Capricorn"
    elif month == 1:
        if day < 20:
            astro_sign = "Capricorn" 
        else:
            astro_sign = "Aquarius"
    elif month == 2:
        if day < 19:
            astro_sign = "Aquarius"
        else:
            astro_sign = "Pisces"
    elif month == 3:
        if day < 21:  
            astro_sign = "Pisces" 
        else:
            astro_sign = "Aries"
    elif month == 4:
        if day < 20:
            astro_sign = "Aries"
        else:
            astro_sign = "Taurus"
    elif month == 5:
        if day < 21:
            astro_sign = "Taurus"
        else:
            astro_sign = "Gemini"  
    elif month == 6:
        if day < 21:
            astro_sign = "Gemini"
        else:
            astro_sign = "Cancer"
    elif month == 7:
        if day < 23: 
            astro_sign = "Cancer"
        else:
            astro_sign = "Leo"
    elif month == 8:
        if day < 23:
            astro_sign = "Leo"
        else:   
         astro_sign = "Virgo"
    elif month == 9:
        if day < 23:
            astro_sign = "Virgo"
        else:
            astro_sign = "Libra"
    elif month == 10:
        if day < 23:
            astro_sign = "Libra"
        else:
            astro_sign = "Scorpio" 
    elif month == 11:
        if day < 22: 
            astro_sign = "Scorpio"
        else:
            astro_sign = "Sagittarius"

    return astro_sign; 

@app.route('/', methods=['GET'])
def homePage():
    return render_template('delphi.html')

@app.route('/about', methods=['GET'])
def aboutPage():
    return render_template('about.html')

@app.route('/profile', methods=['POST','GET'])
def profilePage():
    if request.method == "POST":
        try:
            data = json.loads(request.data)
            date_parts = data['date'].split('-')
            year = int(date_parts[0])
            month = int(date_parts[1])
            day = int(date_parts[2])

            sign = getAstrology(month, day, year)

            print(year, month, day)
            print(sign)
            return Response(sign, status=200)
        except Exception as e:
            print(e)
            return Response(e, status=500)
    if request.method == "GET":
        return render_template('profile.html')

@app.route('/results/<sign>', methods=['GET'])
def sign(sign):

    zodiac = Zodiac.query.filter_by(zodiac_name=sign).first()
    
    return """<!doctype html>
<html lang="en-US">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Profile</title>
  <link href="../static/css/delphi.css" rel="stylesheet" type="text/css">
  <script src="http://use.edgefonts.net/source-sans-pro:n2:default.js" type="text/javascript"></script>
</head>

<body>

  <div class="container">

    <header> <a href="/">
        <h4 class="logo">DELPHI</h4>
      </a>
      <nav>
        <ul>

          <li><a href="/">HOME</a></li>
          <li><a href="/team">THE TEAM</a></li>
          <li><a href="/about">ABOUT</a></li>
        </ul>
      </nav>
    </header>
    <section class="hero" id="hero">
      <h2 class="hero_header"> <span class="light">YOUR PROFILE</span></h2>
    </section>
    <section class="footer_banner">
    </section>

    <footer>
      <h3 style="text-align: center">HOROSCOPE</h3>
      <article class="footer_column">
        <p style="color:black;">Your sign is <b><b>{}</b>!</p>
        <p style="color:black;"><b><b>Dates:</b> {}</p>
        <p style="color:black;"><b>Strengths:</b> {}</p>
        <p style="color:black;"><b>Weaknesses:</b> {}</p>
        <p style="color:black;"><b>Likes:</b> {}</p>
        <p style="color:black;"><b>Dislikes:</b> {}</p>
      </article>
      <article class="footer_column">
        <p style="color:black;">{}</p>
      </article>
    </footer>
    <section class="footer_banner" id="contact">
    </section>
  </div>


</body>

</html>
    """.format(zodiac.zodiac_name, zodiac.dates, zodiac.strengths, zodiac.weaknesses, zodiac.likes, zodiac.dislikes, zodiac.description)

@app.route('/team', methods=['GET'])
def teamPage():
    return render_template('team.html')

if __name__ == "__main__":
    app.run()

    