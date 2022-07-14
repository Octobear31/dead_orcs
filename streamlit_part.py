import streamlit as st
import requests
import pandas as pd
import json
import pickle
import numpy as np
from datetime import date # for today method
from PIL import Image


st.set_page_config(
    page_title = 'Втрати жокупанта',
    layout = 'wide'
)

@st.cache(allow_output_mutation=True)
def load_model():
    today = date.today() # gets today's date

    dates_rng = pd.date_range(start='25/02/2022', end=today) # gets range between specific dates
    # print(dates_rng.to_pydatetime())
    dates_wrong_format = dates_rng.to_pydatetime() # turns received data into specific format
    print(dates_wrong_format)

    dates = []
    for i in range(len(dates_wrong_format)):
        all = dates_wrong_format[i].strftime('%Y-%m-%d') # turns received data into DD/MM/YYYY format
        dates.append(all)
    

    stats_data = [] # stores recieved data from API
    for i in dates:
        response = requests.get('https://russianwarship.rip/api/v1/statistics/%s' % i) # we get requested data for every day of war
        stats_data.append(response.json())

    return (stats_data)

stats_data = load_model() 



# class MyClass():
#     def __init__(self, param):
#         self.param = param
 
# def load_object(filename):
#     try:
#         with open(filename, "rb") as f:
#             return pickle.load(f)
#     except Exception as ex:
#         print("Error during unpickling object (Possibly unsupported):", ex)
 
# obj = load_object("data.pickle")
# # print((stats_data[-1]['data']['day']))
# if 'param' not in st.session_state:
#     st.session_state.param = stats_data

x = st.slider('Оберіть день війни', min_value = stats_data[0]['data']['day'], max_value = stats_data[-1]['data']['day'], key="myslider", value=stats_data[-1]['data']['day'] )  # 👈 this is a widget
# d = st.date_input(
#      "When's your birthday",
#      date.today())
# data_date = []
# response = requests.get('https://russianwarship.rip/api/v1/statistics/%s' % d)
# data_date.append(response.json())
# print(data_date[0]['data'])
# personnel_units = data_date[0]['data']['stats']['personnel_units']
# st.write(personnel_units)

if stats_data[x-2]['message'] == 'Statistic record not found.':
    st.error('Вибачте, але за цей день не знайдено відповідних даних.') 
elif stats_data[x-2]['data']['date'] == '2022-02-27':
    personnel_units = stats_data[x-2]['data']['stats']['personnel_units']
    personnel_units_delta = (stats_data[x-2]['data']['stats']['personnel_units'])-(stats_data[x-4]['data']['stats']['personnel_units'])

    tanks = stats_data[x-2]['data']['stats']['tanks']
    tanks_delta = (stats_data[x-2]['data']['stats']['tanks'])-(stats_data[x-4]['data']['stats']['tanks'])

    armoured_fighting_vehicles = stats_data[x-2]['data']['stats']['armoured_fighting_vehicles']
    armoured_fighting_vehicles_delta = (stats_data[x-2]['data']['stats']['armoured_fighting_vehicles'])-(stats_data[x-4]['data']['stats']['armoured_fighting_vehicles'])

    artillery_systems = stats_data[x-2]['data']['stats']['artillery_systems']
    artillery_systems_delta = (stats_data[x-2]['data']['stats']['artillery_systems'])-(stats_data[x-4]['data']['stats']['artillery_systems'])

    mlrs = stats_data[x-2]['data']['stats']['mlrs']
    mlrs_delta = (stats_data[x-2]['data']['stats']['mlrs'])-(stats_data[x-4]['data']['stats']['mlrs'])

    aa_warfare_systems = stats_data[x-2]['data']['stats']['aa_warfare_systems']
    aa_warfare_systems_delta = (stats_data[x-2]['data']['stats']['aa_warfare_systems'])-(stats_data[x-4]['data']['stats']['aa_warfare_systems'])

    planes = stats_data[x-2]['data']['stats']['planes']
    planes_delta = (stats_data[x-2]['data']['stats']['planes'])-(stats_data[x-4]['data']['stats']['planes'])

    helicopters = stats_data[x-2]['data']['stats']['helicopters']
    helicopters_delta = (stats_data[x-2]['data']['stats']['helicopters'])-(stats_data[x-4]['data']['stats']['helicopters'])

    vehicles_fuel_tanks = stats_data[x-2]['data']['stats']['vehicles_fuel_tanks']
    vehicles_fuel_tanks_delta = (stats_data[x-2]['data']['stats']['vehicles_fuel_tanks'])-(stats_data[x-4]['data']['stats']['vehicles_fuel_tanks'])

    warships_cutters = stats_data[x-2]['data']['stats']['warships_cutters']
    warships_cutters_delta = (stats_data[x-2]['data']['stats']['warships_cutters'])-(stats_data[x-4]['data']['stats']['warships_cutters'])

    cruise_missiles = stats_data[x-2]['data']['stats']['cruise_missiles']
    cruise_missiles_delta = (stats_data[x-2]['data']['stats']['cruise_missiles'])-(stats_data[x-4]['data']['stats']['cruise_missiles'])

    uav_systems = stats_data[x-2]['data']['stats']['uav_systems']
    uav_systems_delta = (stats_data[x-2]['data']['stats']['uav_systems'])-(stats_data[x-4]['data']['stats']['uav_systems'])

    special_military_equip = stats_data[x-2]['data']['stats']['special_military_equip']
    special_military_equip_delta = (stats_data[x-2]['data']['stats']['special_military_equip'])-(stats_data[x-4]['data']['stats']['special_military_equip'])

    atgm_srbm_systems = stats_data[x-2]['data']['stats']['atgm_srbm_systems']
    atgm_srbm_systems_delta = (stats_data[x-2]['data']['stats']['atgm_srbm_systems'])-(stats_data[x-4]['data']['stats']['atgm_srbm_systems'])

    st.subheader('Загальні бойові втрати :skull: противника на %s день війни, орієнтовно склали:' % x)
    st.metric(label = 'Дата:', value = stats_data[x-2]['data']['date'])

    personnel_units_col, tanks_col, armoured_fighting_vehicles_col, artillery_systems_col, mlrs_col, aa_warfare_systems_col, planes_col = st.columns(7)
    with personnel_units_col:
        # st.image('enemy.png', width = 50)
        st.metric(label = '🧟‍♂️ Особового складу:', value = personnel_units, delta= personnel_units_delta)
    with tanks_col:
        # st.image('icon-tank.svg', width = 50)
        st.metric(label = '💩 Танків:', value = tanks, delta = tanks_delta)
    with armoured_fighting_vehicles_col:
        # st.image('icon-bbm.svg', width = 50)
        st.metric(label = '🚜 ББМ::', value = armoured_fighting_vehicles, delta = armoured_fighting_vehicles_delta)
    with artillery_systems_col:
        # st.image('icon-art.svg', width = 50)
        st.metric(label = '☄️ Арт. систем:', value = artillery_systems, delta = artillery_systems_delta)
    with mlrs_col:
        # st.image('icon-rszv.svg', width = 50)
        st.metric(label = '🚀 РСЗВ::', value = mlrs, delta = mlrs_delta)
    with aa_warfare_systems_col:
        # st.image('icon-ppo.svg', width = 50)
        st.metric(label = '🛰 Засобів ППО:', value = aa_warfare_systems, delta = aa_warfare_systems_delta)
    with planes_col:
        # st.image('icon-plane.svg', width = 50)
        st.metric(label = '✈️ Літаків:', value = planes, delta = planes_delta)

    helicopters_col, vehicles_fuel_tanks_col, warships_cutters_col, cruise_missiles_col, uav_systems_col, special_military_equip_col, atgm_srbm_systems_col = st.columns(7)
    with helicopters_col:
        # st.image('icon-helicopter.svg', width = 50)
        st.metric(label = '🚁 Гелікоптерів:', value = helicopters, delta = helicopters_delta)
    with vehicles_fuel_tanks_col:
        # st.image('icon-auto.svg', width = 50)
        st.metric(label = '⛽️ Автотехніки/автоцистерн:', value = vehicles_fuel_tanks, delta = vehicles_fuel_tanks_delta)
    with warships_cutters_col:
        # st.image('ship.png', width = 50)
        st.metric(label = '🖕🏻 Кораблів/катерів:', value = warships_cutters, delta = warships_cutters_delta)
    with cruise_missiles_col:
        # st.image('icon-rocket.svg', width = 50)
        st.metric(label = '🚀 Крилатих ракет:', value = cruise_missiles, delta = cruise_missiles_delta)
    with uav_systems_col:
        # st.image('icon-bpla.svg', width = 50)
        st.metric(label = '🛸 БПЛА:', value = uav_systems, delta = uav_systems_delta)
    with special_military_equip_col:
        # st.image('icon-auto.svg', width = 50)
        st.metric(label = '🚍 Спец. техніки:', value = special_military_equip, delta = special_military_equip_delta)
    with atgm_srbm_systems_col:
        # st.image('ship.png', width = 50)
        st.metric(label = '🚀 Установок ОТРК/ТРК:', value = atgm_srbm_systems, delta = atgm_srbm_systems_delta)

elif stats_data[x-2]['data']['date'] == '2022-02-25':
    personnel_units = stats_data[x-2]['data']['stats']['personnel_units']
    tanks = stats_data[x-2]['data']['stats']['tanks']
    armoured_fighting_vehicles = stats_data[x-2]['data']['stats']['armoured_fighting_vehicles']
    artillery_systems = stats_data[x-2]['data']['stats']['artillery_systems']
    mlrs = stats_data[x-2]['data']['stats']['mlrs']
    aa_warfare_systems = stats_data[x-2]['data']['stats']['aa_warfare_systems']
    planes = stats_data[x-2]['data']['stats']['planes']
    helicopters = stats_data[x-2]['data']['stats']['helicopters']
    vehicles_fuel_tanks = stats_data[x-2]['data']['stats']['vehicles_fuel_tanks']
    warships_cutters = stats_data[x-2]['data']['stats']['warships_cutters']
    cruise_missiles = stats_data[x-2]['data']['stats']['cruise_missiles']
    uav_systems = stats_data[x-2]['data']['stats']['uav_systems']
    special_military_equip = stats_data[x-2]['data']['stats']['special_military_equip']
    atgm_srbm_systems = stats_data[x-2]['data']['stats']['atgm_srbm_systems']

    st.subheader('Загальні бойові втрати :skull: противника на %s день війни, орієнтовно склали:' % x)
    st.metric(label = 'Дата:', value = stats_data[x-2]['data']['date'])

    personnel_units_col, tanks_col, armoured_fighting_vehicles_col, artillery_systems_col, mlrs_col, aa_warfare_systems_col, planes_col = st.columns(7)
    with personnel_units_col:
        # st.image('enemy.png', width = 50)
        st.metric(label = '🧟‍♂️ Особового складу:', value = personnel_units)
    with tanks_col:
        # st.image('icon-tank.svg', width = 50)
        st.metric(label = '💩 Танків:', value = tanks)
    with armoured_fighting_vehicles_col:
        # st.image('icon-bbm.svg', width = 50)
        st.metric(label = '🚜 ББМ::', value = armoured_fighting_vehicles)
    with artillery_systems_col:
        # st.image('icon-art.svg', width = 50)
        st.metric(label = '☄️ Арт. систем:', value = artillery_systems)
    with mlrs_col:
        # st.image('icon-rszv.svg', width = 50)
        st.metric(label = '🚀 РСЗВ::', value = mlrs)
    with aa_warfare_systems_col:
        # st.image('icon-ppo.svg', width = 50)
        st.metric(label = '🛰 Засобів ППО:', value = aa_warfare_systems)
    with planes_col:
        # st.image('icon-plane.svg', width = 50)
        st.metric(label = '✈️ Літаків:', value = planes)

    helicopters_col, vehicles_fuel_tanks_col, warships_cutters_col, cruise_missiles_col, uav_systems_col, special_military_equip_col, atgm_srbm_systems_col = st.columns(7)
    with helicopters_col:
        # st.image('icon-helicopter.svg', width = 50)
        st.metric(label = '🚁 Гелікоптерів:', value = helicopters)
    with vehicles_fuel_tanks_col:
        # st.image('icon-auto.svg', width = 50)
        st.metric(label = '⛽️ Автотехніки/автоцистерн:', value = vehicles_fuel_tanks)
    with warships_cutters_col:
        # st.image('ship.png', width = 50)
        st.metric(label = '🖕🏻 Кораблів/катерів:', value = warships_cutters)
    with cruise_missiles_col:
        # st.image('icon-rocket.svg', width = 50)
        st.metric(label = '🚀 Крилатих ракет:', value = cruise_missiles)
    with uav_systems_col:
        # st.image('icon-bpla.svg', width = 50)
        st.metric(label = '🛸 БПЛА:', value = uav_systems)
    with special_military_equip_col:
        # st.image('icon-auto.svg', width = 50)
        st.metric(label = '🚍 Спец. техніки:', value = special_military_equip)
    with atgm_srbm_systems_col:
        # st.image('ship.png', width = 50)
        st.metric(label = '🚀 Установок ОТРК/ТРК:', value = atgm_srbm_systems)

else:
    personnel_units = stats_data[x-2]['data']['stats']['personnel_units']
    personnel_units_delta = (stats_data[x-2]['data']['stats']['personnel_units'])-(stats_data[x-3]['data']['stats']['personnel_units'])

    tanks = stats_data[x-2]['data']['stats']['tanks']
    tanks_delta = (stats_data[x-2]['data']['stats']['tanks'])-(stats_data[x-3]['data']['stats']['tanks'])

    armoured_fighting_vehicles = stats_data[x-2]['data']['stats']['armoured_fighting_vehicles']
    armoured_fighting_vehicles_delta = (stats_data[x-2]['data']['stats']['armoured_fighting_vehicles'])-(stats_data[x-3]['data']['stats']['armoured_fighting_vehicles'])

    artillery_systems = stats_data[x-2]['data']['stats']['artillery_systems']
    artillery_systems_delta = (stats_data[x-2]['data']['stats']['artillery_systems'])-(stats_data[x-3]['data']['stats']['artillery_systems'])

    mlrs = stats_data[x-2]['data']['stats']['mlrs']
    mlrs_delta = (stats_data[x-2]['data']['stats']['mlrs'])-(stats_data[x-3]['data']['stats']['mlrs'])

    aa_warfare_systems = stats_data[x-2]['data']['stats']['aa_warfare_systems']
    aa_warfare_systems_delta = (stats_data[x-2]['data']['stats']['aa_warfare_systems'])-(stats_data[x-3]['data']['stats']['aa_warfare_systems'])

    planes = stats_data[x-2]['data']['stats']['planes']
    planes_delta = (stats_data[x-2]['data']['stats']['planes'])-(stats_data[x-3]['data']['stats']['planes'])

    helicopters = stats_data[x-2]['data']['stats']['helicopters']
    helicopters_delta = (stats_data[x-2]['data']['stats']['helicopters'])-(stats_data[x-3]['data']['stats']['helicopters'])

    vehicles_fuel_tanks = stats_data[x-2]['data']['stats']['vehicles_fuel_tanks']
    vehicles_fuel_tanks_delta = (stats_data[x-2]['data']['stats']['vehicles_fuel_tanks'])-(stats_data[x-3]['data']['stats']['vehicles_fuel_tanks'])

    warships_cutters = stats_data[x-2]['data']['stats']['warships_cutters']
    warships_cutters_delta = (stats_data[x-2]['data']['stats']['warships_cutters'])-(stats_data[x-3]['data']['stats']['warships_cutters'])

    cruise_missiles = stats_data[x-2]['data']['stats']['cruise_missiles']
    cruise_missiles_delta = (stats_data[x-2]['data']['stats']['cruise_missiles'])-(stats_data[x-3]['data']['stats']['cruise_missiles'])

    uav_systems = stats_data[x-2]['data']['stats']['uav_systems']
    uav_systems_delta = (stats_data[x-2]['data']['stats']['uav_systems'])-(stats_data[x-3]['data']['stats']['uav_systems'])

    special_military_equip = stats_data[x-2]['data']['stats']['special_military_equip']
    special_military_equip_delta = (stats_data[x-2]['data']['stats']['special_military_equip'])-(stats_data[x-3]['data']['stats']['special_military_equip'])

    atgm_srbm_systems = stats_data[x-2]['data']['stats']['atgm_srbm_systems']
    atgm_srbm_systems_delta = (stats_data[x-2]['data']['stats']['atgm_srbm_systems'])-(stats_data[x-3]['data']['stats']['atgm_srbm_systems'])

    st.subheader('Загальні бойові втрати :skull: противника на %s день війни, орієнтовно склали:' % x)
    st.metric(label = 'Дата:', value = stats_data[x-2]['data']['date'])

    personnel_units_col, tanks_col, armoured_fighting_vehicles_col, artillery_systems_col, mlrs_col, aa_warfare_systems_col, planes_col = st.columns(7)
    with personnel_units_col:
        # st.image('enemy.png', width = 50)
        st.metric(label = '🧟‍♂️ Особового складу:', value = personnel_units, delta= personnel_units_delta)
    with tanks_col:
        # st.image('icon-tank.svg', width = 50)
        st.metric(label = '💩 Танків:', value = tanks, delta = tanks_delta)
    with armoured_fighting_vehicles_col:
        # st.image('icon-bbm.svg', width = 50)
        st.metric(label = '🚜 ББМ::', value = armoured_fighting_vehicles, delta = armoured_fighting_vehicles_delta)
    with artillery_systems_col:
        # st.image('icon-art.svg', width = 50)
        st.metric(label = '☄️ Арт. систем:', value = artillery_systems, delta = artillery_systems_delta)
    with mlrs_col:
        # st.image('icon-rszv.svg', width = 50)
        st.metric(label = '🚀 РСЗВ::', value = mlrs, delta = mlrs_delta)
    with aa_warfare_systems_col:
        # st.image('icon-ppo.svg', width = 50)
        st.metric(label = '🛰 Засобів ППО:', value = aa_warfare_systems, delta = aa_warfare_systems_delta)
    with planes_col:
        # st.image('icon-plane.svg', width = 50)
        st.metric(label = '✈️ Літаків:', value = planes, delta = planes_delta)

    helicopters_col, vehicles_fuel_tanks_col, warships_cutters_col, cruise_missiles_col, uav_systems_col, special_military_equip_col, atgm_srbm_systems_col = st.columns(7)
    with helicopters_col:
        # st.image('icon-helicopter.svg', width = 50)
        st.metric(label = '🚁 Гелікоптерів:', value = helicopters, delta = helicopters_delta)
    with vehicles_fuel_tanks_col:
        # st.image('icon-auto.svg', width = 50)
        st.metric(label = '⛽️ Автотехніки/автоцистерн:', value = vehicles_fuel_tanks, delta = vehicles_fuel_tanks_delta)
    with warships_cutters_col:
        # st.image('ship.png', width = 50)
        st.metric(label = '🖕🏻 Кораблів/катерів:', value = warships_cutters, delta = warships_cutters_delta)
    with cruise_missiles_col:
        # st.image('icon-rocket.svg', width = 50)
        st.metric(label = '🚀 Крилатих ракет:', value = cruise_missiles, delta = cruise_missiles_delta)
    with uav_systems_col:
        # st.image('icon-bpla.svg', width = 50)
        st.metric(label = '🛸 БПЛА:', value = uav_systems, delta = uav_systems_delta)
    with special_military_equip_col:
        # st.image('icon-auto.svg', width = 50)
        st.metric(label = '🚍 Спец. техніки:', value = special_military_equip, delta = special_military_equip_delta)
    with atgm_srbm_systems_col:
        # st.image('ship.png', width = 50)
        st.metric(label = '🚀 Установок ОТРК/ТРК:', value = atgm_srbm_systems, delta = atgm_srbm_systems_delta)
