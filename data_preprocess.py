import pandas as pd
import numpy as np 
from string import *


def event_organiser(df, event_list, event_type_str):
    
    cond1 = df.event_name_2.notnull() 
    cond2 = -(df.event_name_1.isin(event_list))

    df.event_name_1 = np.where(
        (
            (cond1) 
            & 
            (cond2)
        ),
        df.event_name_2,
        df.event_name_1
    )
    df.drop(columns='event_name_2', inplace=True)
    df.rename(columns={'event_name_1':event_type_str+"_event"}, inplace=True)
    return df

def event_df_creater(calender, event_list, event_type_str):
    df = calender.loc[
        :,
        ['d','date','year','event_name_1','event_name_2']
    ][
        (calender.event_name_1.isin(event_list)) 
        | 
        (calender.event_name_2.isin(event_list))
    ]
    
    df = event_organiser(df,event_list, event_type_str)
    
    return df

def event_dict_creater(df):
    event_types = list(df.event_type_1.unique())
    event_types.pop(0)
    event_types
    event_dict = {}
    for i in event_types:
        event_list_1 = df["event_name_1"][df.event_type_1==str(i)].unique()
        event_list_2 = df["event_name_2"][df.event_type_2==str(i)].unique()
#         print(event_list_1)
        event_dict[i] = np.unique(np.hstack((event_list_1, event_list_2)))
    
    return event_dict

def event_manager(df):
    event_dict = event_dict_creater(df)
    mergedDF = pd.DataFrame()
    for eventType, eventList in event_dict.items():
        DF = event_df_creater(df, eventList, eventType)
        if mergedDF.empty:
            mergedDF=DF.copy(deep=True)
        else:
            mergedDF= mergedDF.merge(DF, on=['d','date','year'], how='outer')
    return mergedDF


def preprocess():

    # import the data
    calender = pd.read_csv("calendar.csv")
    sales = pd.read_csv("sales_train_evaluation.csv")
    sell_prices = pd.read_csv("sell_prices.csv")

    # create a new column in calender
    calender["week_of_year"] = calender["wm_yr_wk"].astype("str").str[-2:].astype("int")
    calender.drop(columns=['snap_CA', 'snap_TX', 'snap_WI'], inplace=True)

    # merge calender and sell_prices dataframes
    cal_sell_merged = sell_prices.merge(
        calender[
            [
                'wm_yr_wk', 
                'week_of_year', 
                'year'
            ]
        ].drop_duplicates(),
        on='wm_yr_wk',
        how="left"
        )

    # get day columns in sales df in list
    salesDateCol = list(
        sales.columns[
            sales.columns.str.startswith("d_")
        ]
    )

    # create a columns to records total sales for every record
    sales["total_items_sold"] = sales[
        salesDateCol
    ].apply(
        lambda x:
        sum(x),
         axis=1
    )

    # get items sold per store
    itemsSoldperStore = sales[
        [
            'item_id', 
            'dept_id',
            'cat_id',
            'store_id',
            'state_id', 
            'total_items_sold'
        ]
    ]

    # melt sales dataframe
    sales_long = pd.melt(
        sales.drop(columns=['total_items_sold']),
        id_vars=[
            'id',
            'item_id', 
            'dept_id', 
            'cat_id', 
            'store_id', 
            'state_id'
        ],
        var_name= "day_index",
        value_name= "sale_quantity"
    )
    
    # create master sales dataframe which contains 
    # required information from calender and sales
    sales_master = sales_long.merge(
        calender[['d', 'date', 'wm_yr_wk']],
        left_on='day_index',
        right_on='d',
        how='left'
    ).drop(
        columns=['d']
    ).merge(
        cal_sell_merged,
        on=['store_id', 'item_id', 'wm_yr_wk'],
        how='left'
    )

    # handle missing values 
    sales_master_final = sales_master[
        sales_master['sell_price'].notna()
    ]

    # fix dtypes
    sales_master_final = sales_master_final.astype(
        {
            'date':'datetime64[D]',
            'wm_yr_wk':'object',
            'week_of_year':'int32',
            'year':'int32'
        }
    )

    # Calculate revenue
    sales_master_final['revenue'] = sales_master_final[
        'sell_price'
    ]*sales_master_final[
        'sale_quantity'
    ]

    # delete unwanted dataframes to free up some memory
    del sales_long, sales_master, salesDateCol

    # get event data from calender 
    event_cal = event_manager(calender)

    # merged event data with final master sales
    sales_master_final = sales_master_final.merge(
        event_cal.drop(columns=['date','year']),
        left_on='day_index',
        right_on='d',
        how='left'
    )

    # delete event_cal
    del event_cal 

    return sales_master_final





    