# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def data_clean():
    
    data = pd.read_excel('ClimateChange.xlsx', sheetname='Data')
    data_gdp = data[data['Series code'] == 'NY.GDP.MKTP.CD'].set_index('Country code')
    data_co2 = data[data['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')

    data_gdp.replace({'..':pd.np.NaN}, inplace=True)
    data_co2.replace({'..':pd.np.NaN}, inplace=True)
    data_gdp = data_gdp.iloc[:, 5:].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    data_co2 = data_co2.iloc[:, 5:].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    data_gdp['gdp-sum'] = data_gdp.sum(axis=1)
    data_co2['co2-sum'] = data_co2.sum(axis=1)
    data_merge = pd.concat([data_gdp['gdp-sum'], data_co2['co2-sum']], axis=1)
    data_merge_fill = data_merge.fillna(value=0)

    return data_merge_fill

def co2_gdp_plot():

    df_clean = data_clean()
    df_max_min = (df_clean - df_clean.min())/(df_clean.max() - df_clean.min())
    china = []
    for i in df_max_min[df_max_min.index == 'CHN'].values:
        china.extend(np.round(i, 3).tolist())
    country_label = ['USA', 'CHN', 'FRA', 'RUS', 'GBR']
    sticks_label = []
    label_position = []
    for i in range(len(df_max_min)):
        if df_max_min.index[i] in country_label:
            sticks_label.append(df_max_min.index[i])
            label_position.append(i)
    fig = plt.subplot()
    df_max_min.plot(
        kind='line',
        title='GDP-CO2',
        ax=fig
        )
    plt.xlabel('Countries')
    plt.ylabel('Values')
    plt.xticks(label_position, sticks_lanel, rotation='vertical')
    plt.show()

    return fig, china
