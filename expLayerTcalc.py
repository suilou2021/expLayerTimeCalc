########################################################################
# expLayerTcalc.py
#
# Created: Aug. 23, 2022
# Author: S. Huang
# This is the main program for calculating expected layer time for OEE
# based on GEN2.0 specifications
########################################################################

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyodbc
import pandas as pd

import params


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def readData():
    # to be completed by Nirnay or Patrick
    # read data from database to data frome
    server = 'server_name'
    database = 'database_name'
    username = 'user_name'
    password = 'database_password'
    con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = con.cursor()
    #
    query = "SELECT * FROM <table>;"
    df = pd.read_sql(query, con)
    # expected field names: lotid, boolDoubleLase, layernumber, scanDir, xMin, xMax, yMin, yMax, cntAct, cntExp
    return df

def layerTcalc(df):
    # compute expected layer time
    # for dev
    if(1==0):
        data = {'lotid': ['VF-00441-0004', 'VF-00441-0004'],
                'boolDoubleLase': [0, 0],
                'layernumber': [1, 2],
                'scanDir': ['X', 'Y'],
                'xMin': [0.0, 0.0],
                'xMax': [600.0, 600.0],
                'yMin': [0.0, 0.0],
                'yMax': [600.0, 600.0],
                'cntAct': [50, 60],
                'cntExp': [144, 144]
        }
        df = pd.DataFrame(data)

    #
    df['boolXscan'] = 1
    df.loc[df['scanDir']=='Y', 'boolXscan'] = 0
    df['boolYscan'] = 0
    df.loc[df['scanDir']=='Y', 'boolYscan'] = 1
    # scan time for one trajectory
    scanT1 = 2*params.tRampComp + \
             (df.boolXscan*(df.xMax-df.xMin) + df.boolYscan*(df.yMax-df.yMin))/params.v + \
             params.tIndexOffset
    # scan time for n trajectories
    scanTn = scanT1 * df.cntExp
    # layer time for n trajectories
    layerT = scanTn + sum([params.tRecoatImg, params.tGasHeadCleaning])

    df['expLayerTime_s'] = layerT

    return df


# Press the green button in the gutter to run the script.
# if __name__ == '__expLayerTcalcn__':
print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
