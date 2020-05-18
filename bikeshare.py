#Final

#Librerias
import pandas as pd
import numpy as np
import time
from scipy import stats
import multiprocessing
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
# TO DO: get user input for month (all, january, february, ... , june)
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
Dias_Semana= {'Lunes': 'Monday','Martes':'Tuesday','Miercoles':'Wednesday','Jueves':'Thursday','Viernes':'Friday','Sabado':'Saturday','Domingo':'Sunday'}
Ciudades =['Chicago','New York', 'Washington']
mensajes =['Vamos a ver los de datos de '+Ciudades[0],'Vamos a ver los de datos de '+Ciudades[1], 'Vamos a ver los de datos de '+Ciudades[2], 'No tenemos datos para su ciudad ¿Por qué no intenta con: Chicago New York o Washington?']
ciudad=""
Resultado=""
week = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
search_city = input('bienvenido a las estadisticas de Bikeshare por ciudad, mes y dia ingrese su ciudad ')
ciudad = search_city.lower() 
while search_city.lower() == "chicago" or "new york" or "washington":
    if search_city.lower() == "chicago":
      Resultado  = (mensajes[0])
    elif search_city.lower() == "new york":
      Resultado  = (mensajes[1])
    elif search_city.lower() == "washington":
      Resultado  = (mensajes[2])
    else:
      Resultado  =(mensajes[3])
      print(ciudad)
      print(Resultado) 
      search_city = input('Ingrese su ciudad ')  
    break 
    if search_city == "chicago":
      Resultado = (mensajes[0])
    elif search_city == "new york":
      Resultado = (mensajes[1]) 
    elif search_city == "washington":
      Resultado = (mensajes[2])
    break

print(Resultado) 
     
ciudad = search_city.lower() 
Input_Fecha = input('Ingrese el mes del primer semestre de 2017 ')
month = Input_Fecha.lower()

Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
df = pd.read_csv(Datos_Ciudades[ciudad])
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['dia_semana'] = df['Start Time'].dt.day_name()
df['month'] = df['Start Time'].dt.month
if month != 'all':
  months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
  month = months.index(month) + 1
  df = df[df['month'] == month]
Dias_Semana= {'Lunes': 'Monday','Martes':'Tuesday','Miercoles':'Wednesday','Jueves':'Thursday','Viernes':'Friday','Sabado':'Saturday','Domingo':'Sunday'}
Input_day = input('Ingrese el día de la semana ')
day_es=Input_day.capitalize()

if Dias_Semana[day_es] != 'all':
   df = df[df['dia_semana'] == Dias_Semana[day_es]]

# TO DO: display the most common month
# TO DO: display the most common day of week
# TO DO: display the most common start hour
#Volví a cargar la data porque si la dejo filtrada no me traerá el mes mas común si no el mes filtrado, al igual que el dia y la hora lo cual no responde a la pregunta realizada

Estadistica_Meses = input('¿Quiere ver los datos de las estadisticas de los meses?')
if Estadistica_Meses == 'si':
  Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
  df = pd.read_csv(Datos_Ciudades[ciudad])  
  df['Start Time'] = pd.to_datetime(df['Start Time'])
  df['month'] = df['Start Time'].dt.month
  df['day'] = df['Start Time'].dt.dayofweek
  df['hour'] = df['Start Time'].dt.hour
  month= df['month'].mode()[0]
  pop_mont = months[month - 1]
  popday= df['Start Time'].dt.dayofweek.mode()[0]
  pop_day = week[popday]
  pophour =df['hour'] = df['Start Time'].dt.hour.mode()[0]
  pop_hour= str(pophour)
  print('El mes que mas se repite en '+ciudad+' es '+pop_mont)
  print('El dia que mas se repite en '+ciudad+' es '+pop_day)
  print('La hora que mas se repite en '+ciudad+' es '+pop_hour+':00')

else:

# TO DO: display most commonly used start station
# TO DO: display most commonly used end station
# TO DO: display most frequent combination of start station and end station trip

  Estadistica_Estaciones = input('¿Quiere ver los datos de las estadisticas de las estaciones?')
  if Estadistica_Estaciones == 'si':
    month = Input_Fecha.lower()
    Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
    df = pd.read_csv(Datos_Ciudades[ciudad])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['dia_semana'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
      months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
      month = months.index(month) + 1
      df = df[df['month'] == month]
      Dias_Semana= {'Lunes': 'Monday','Martes':'Tuesday','Miercoles':'Wednesday','Jueves':'Thursday','Viernes':'Friday','Sabado':'Saturday','Domingo':'Sunday'}
    if Dias_Semana[day_es] != 'all':
      df = df[df['dia_semana'] == Dias_Semana[day_es]]
      Start_Station=df['Start Station'].mode()[0]
      End_Station=df['End Station'].mode()[0]
      df['Comb_Station'] ='De '+df['Start Station']+' a '+df['End Station']
      Comb_Station = df['Comb_Station'].mode()[0]
      print('La estación en donde mas se inician viajes es: '+Start_Station)
      print('La estación en donde mas se terminan viajes es: '+End_Station)
      print('El viaje que mas se repite es: '+Comb_Station)

# TO DO: display total travel time
# TO DO: display mean travel time

  else:
    Estadistica_viajes = input('¿Quiere ver los datos de las estadisticas de los viajes?')
    if Estadistica_viajes == 'si':
      month = Input_Fecha.lower()
      Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
      df = pd.read_csv(Datos_Ciudades[ciudad])
      df['Start Time'] = pd.to_datetime(df['Start Time'])
      df['End Time'] = pd.to_datetime(df['End Time'])
      df['dia_semana'] = df['Start Time'].dt.day_name()
      df['month'] = df['Start Time'].dt.month
      if month != 'all':
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        day_es=Input_day.capitalize() 
      if Dias_Semana[day_es] != 'all':
        df = df[df['dia_semana'] == Dias_Semana[day_es]]  
        df['duracion'] = df['End Time'] - df['Start Time']
        Viaje_total=df['duracion'].sum()
        Promedio_viaje=df['duracion'].mean()
        print('El promedio de duración de viajes es: '+str(Promedio_viaje))
        print('El total de duración de los viajes es: '+str(Viaje_total))

# TO DO: Display counts of user types
# TO DO: Display counts of gender
    else:
      Estadistica_generos = input('¿Quiere ver los datos de las estadisticas de los usuarios?')
      if Estadistica_generos == 'si':
        month = Input_Fecha.lower()
        Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
        df = pd.read_csv(Datos_Ciudades[ciudad])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['dia_semana'] = df['Start Time'].dt.day_name()
        df['month'] = df['Start Time'].dt.month
        if month != 'all':
          month = Input_Fecha.lower()
          months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
          month = months.index(month) + 1
          df = df[df['month'] == month]
 
          
        if Dias_Semana[day_es] != 'all':
          day_es=Input_day.capitalize() 
          df = df[df['dia_semana'] == Dias_Semana[day_es]]  
          Suma_Tipos = df['User Type'].value_counts()
          Suma_Generos = df['Gender'].value_counts() 
          print('Por tipo de usuarios: ')     
          print(Suma_Tipos)
          print('Por tipo de generos: ')     
          print(Suma_Generos)

# TO DO: Display earliest, most recent, and most common year of birth

      else: 
        Estadistica_nacimientos = input('¿Quiere ver los datos de las estadisticas de las fechas de nacimiento?')
        if Estadistica_nacimientos == 'si':
          Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
          df = pd.read_csv(Datos_Ciudades[ciudad])
          month = Input_Fecha.lower()
          df['Start Time'] = pd.to_datetime(df['Start Time'])
          df['dia_semana'] = df['Start Time'].dt.day_name()
          df['month'] = df['Start Time'].dt.month
          if month != 'all':
            month = Input_Fecha.lower()
            months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
            month = months.index(month) + 1
            df = df[df['month'] == month]
          if Dias_Semana[day_es] != 'all':
            day_es=Input_day.capitalize() 
            primer_nacimiento = df['Birth Year'].min()
            ultimo_nacimiento= df['Birth Year'].max()
            moda_nacimientos=df['Birth Year'].mode()[0]
            print('La persona con el mayor año de fecha de nacimiento es: '+str(primer_nacimiento)[0:4])
            print('La persona con el menor año de fecha de nacimiento es: '+str(ultimo_nacimiento)[0:4])
            print('El año de nacimiento que mas se repite es: '+str(moda_nacimientos)[0:4])
            print("Gracias por visitarnos")
        else:
            print("Gracias por visitarnos")
#Display contents of the CSV file to the display as requested by the user.           
def muestra_data(df):
              inicio_loc = 0
              fin_loc = 5
              data_cruda = input("¿Quiere ver la data cruda?: ").lower()
              if data_cruda  == 'si':
                while fin_loc <= df.shape[0] - 1:
                  print(df.iloc[inicio_loc:fin_loc,:])
                  inicio_loc += 5
                  fin_loc += 5
                  mensaje_final = input("¿Quiere continuar?: ").lower()
                  if mensaje_final == 'no':
                  
                    break
                    
                    
muestra_data(df)
print("Gracias por visitarnos")
