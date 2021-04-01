#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import chart_studio.plotly as plty
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np 
from string import *
import plotly.express as px


# In[2]:


calender = pd.read_csv("calendar.csv")
sales = pd.read_csv("sales_train_evaluation.csv")
sell_prices = pd.read_csv("sell_prices.csv")


# In[3]:


calender["week_of_year"] = calender["wm_yr_wk"].astype("str").str[-2:].astype("int")
calender.drop(columns=['snap_CA', 'snap_TX', 'snap_WI'], inplace=True)
calender


# In[4]:


calender.drop(
    columns=[
        'date', 
        'weekday', 
        'wday', 
        'd','event_name_1',
        'event_type_1',
        'event_name_2',
        'event_type_2'
    ]
).drop_duplicates()


# In[5]:


cal_sell_merged = sell_prices.merge(calender[['wm_yr_wk', 'week_of_year', 'year']].drop_duplicates(),
                 on='wm_yr_wk',
                 how="left")

cal_sell_merged


# In[6]:


salesDateCol = list(sales.columns[sales.columns.str.startswith("d_")])


# In[7]:


sales["total_items_sold"] = sales[salesDateCol].apply(lambda x:sum(x), axis=1)


# In[8]:


itemsSoldperStore = sales[['item_id', 'dept_id', 'cat_id', 'store_id', 'state_id', 'total_items_sold']]
itemsSoldperStore


# In[9]:


sales_long = pd.melt(
    sales.drop(columns=['total_items_sold']),
    id_vars=['id','item_id', 'dept_id', 'cat_id', 'store_id', 'state_id'],
    var_name= "day_index",
    value_name= "sale_quantity"
)
sales_long


# In[10]:


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

sales_master


# In[11]:


display(sales_master.isnull().sum())


# In[12]:


sales_master_final = sales_master[sales_master['sell_price'].notna()]


# In[13]:


sales_master_final.head()


# In[14]:


sales_master_final.dtypes


# In[15]:


# pd.to_datetime(sales_master.date, format='%Y-%m-%d')
sales_master_final = sales_master_final.astype(
    {
        'date':'datetime64[D]',
        'wm_yr_wk':'object',
        'week_of_year':'int32',
#         'year':'datetime64[Y]'
        'year':'int32'
    }
)
# pd.to_datetime(sales_master_final.year, format='%Y')
sales_master_final.dtypes


# In[16]:


sales_master_final['revenue'] = sales_master_final[
    'sell_price'
]*sales_master_final[
    'sale_quantity'
]

sales_master_final


# In[17]:


del sales_long, sales_master, salesDateCol


# In[18]:


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

def event_df_creater(event_list, event_type_str):
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
        DF = event_df_creater(eventList, eventType)
        if mergedDF.empty:
            mergedDF=DF.copy(deep=True)
        else:
            mergedDF= mergedDF.merge(DF, on=['d','date','year'], how='outer')
    return mergedDF


# In[19]:


event_cal = event_manager(calender)
event_cal


# In[20]:


sales_master_final = sales_master_final.merge(
    event_cal.drop(columns=['date','year']),
    left_on='day_index',
    right_on='d',
    how='left'
)
sales_master_final

del event_cal


# In[21]:


summary11 = sales_master_final.groupby(
    'state_id'
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
).reset_index()

# display(summary11)

summary11_fig = go.Figure(
    data=[
        go.Bar(
            name = 'Revenue',
            x = summary11['state_id'],
            y = summary11['revenue']
        ),
        go.Bar(
            name = 'Total Sales',
            x = summary11['state_id'],
            y = summary11['sale_quantity']
        )
    ],
)

summary11_fig.update_layout(title="Wallmart's Total Revenue and Total Sales by States")
                   
summary11_fig.show()

del summary11


# In[22]:


summary12 = sales_master_final.groupby(
    [
        'state_id',
        'store_id'
    ]
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
).reset_index()

# display(summary12)

summary12_fig = px.bar(
    summary12,
    x="store_id", 
    y=['sale_quantity', "revenue"],  
    barmode="stack"
)


summary12_fig.update_layout(
    title="Wallmart's Total Revenue for store in all States"
)
                   
summary12_fig.show()

del summary12


# In[23]:


# sales_master = sales_long.merge(
#     calender[['date', 'wm_yr_wk', 'd']],
#     left_on='day_index',
#     right_on='d', 
#     how='left'
# ).drop(
#     columns=['d']
# ).merge(
#     cal_sell_merged,
#     on = ['item_id', 'store_id', 'wm_yr_wk'],
#     how="left"
# )

# sales_master


# In[24]:


summary21 = sales_master_final.groupby(
    [
        'state_id',
        'cat_id',
        'dept_id'
    ]
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
).reset_index()

# display(summary21)

summary21_fig = px.bar(
    summary21,
    x="dept_id", 
    y=["sale_quantity", "revenue"], 
#     color="cat_id", 
    facet_col = 'state_id',
    barmode="stack"
)

summary21_fig.update_layout(
    title="Wallmart's Total Revenue and Sales for store in all States"
)
                   
summary21_fig.show()

del summary21


# In[25]:


summary22 = sales_master_final.groupby(
    [
        'state_id',
        'cat_id',
        'item_id'
    ]
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
)

summary22 = summary22['revenue'].groupby(
    ['state_id','cat_id'], 
    group_keys=False
).nlargest(3).reset_index()

# display(summary22)

summary22_fig = px.sunburst(summary22, path=['state_id', 'cat_id', 'item_id'], values='revenue')
summary22_fig.update_layout(
    title="Wallmart's Top Three selling products in each state and category"
)
summary22_fig.show()

del summary22


# In[26]:


st = "CA" 

ssd00 = sales_master_final.groupby(
    [
        'state_id',
        'store_id',
        'dept_id',
        'item_id'
    ]
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
)

display(ssd00)

ssd00_01 = ssd00['revenue'].groupby(
    ['state_id'],
    group_keys=False
).nlargest(1).reset_index()
display(ssd00_01)

ssd00_02 = ssd00['revenue'].groupby(
    ['state_id'],
    group_keys=False
).nsmallest(1).reset_index()
display(ssd00_02)


# In[27]:


# Extracting one value
ssd00_02[ssd00_02['state_id']=="CA"]


# In[28]:


stateDict = {
    'CA': 'California',
    'TX': 'Texas',
    'WI': 'Wisconsin'
}


# In[29]:


ssd11 = sales_master_final.groupby(
    ['state_id','cat_id','dept_id',]
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
)

ssd11_01 = ssd11['revenue'].groupby(
    "state_id", 
    group_keys=False
).nlargest(3).reset_index()

ssd11_02 = ssd11['sale_quantity'].groupby(
    "state_id", 
    group_keys=False
).nlargest(3).reset_index()

# display(ssd11)



ssd11_fig = make_subplots(
    rows=1, 
    cols=2, 
    shared_yaxes=True
)

ssd11_fig.add_trace(
    go.Bar(
        name = 'Revenue',
        x = ssd11_01[ssd11_01.state_id==st]['dept_id'],
        y = ssd11_01[ssd11_01.state_id==st]['revenue'],
    ),
    1, 1
)
ssd11_fig.add_trace(
    go.Bar(
        name = 'Sale',
        x = ssd11_02[ssd11_02.state_id==st]['dept_id'],
        y = ssd11_02[ssd11_02.state_id==st]['sale_quantity'],
    ),
    1, 2
)

ssd11_fig.update_layout(
    title_text=stateDict[st] 
    + 
    "'s top 3 selling departments in revenue and volumn"
)
ssd11_fig.show()

top_3_dept_by_revenue = list(ssd11_01[ssd11_01.state_id==st]['dept_id'])
top_3_dept_by_revenue

del ssd11, ssd11_01, ssd11_02


# In[30]:


ssd12 = sales_master_final.groupby(
    ['state_id', 'store_id', 'dept_id']
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
)['revenue'].groupby(
    ['state_id', 'dept_id'],
    group_keys=False
).nlargest(1).reset_index()
# ssd12

ssd12_cond = (ssd12.state_id==st) & (ssd12.dept_id.isin(top_3_dept_by_revenue))

ssd12_fig = px.bar(
    ssd12[ssd12_cond],
    x='store_id', 
    y="revenue",
    facet_col='dept_id'

)

ssd12_fig.update_layout(
    title="Revenue of "
    +
    stateDict[st]
    +
    "'s top 3 selling department's best performing stores"
)
                   
ssd12_fig.show()

del ssd12


# In[31]:


state_worst_stores = sales_master_final.groupby(
    ['state_id','store_id']
).agg(
    {'revenue':sum}
)['revenue'].groupby(
    ['state_id'],
    group_keys=False
).nsmallest(1).reset_index()

state_worst_stores


# In[32]:



ssd21 = sales_master_final.groupby(
    ['state_id', 'store_id', 'dept_id']
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
)['revenue'].groupby(
    ['state_id', 'store_id'],
    group_keys=False
).nlargest(3).reset_index()


worst_performing_store = state_worst_stores[
    state_worst_stores.state_id==st
][
    'store_id'
]

ssd21 = ssd21[ssd21.store_id==worst_performing_store[0]]

# ssd12_cond = (ssd12.state_id==st) & (ssd12.dept_id.isin(top_3_dept_by_revenue))

ssd21_fig = px.bar(
    ssd21,
    x='dept_id', 
    y="revenue",
#     facet_col='dept_id'

)

ssd21_fig.update_layout(
    title="Revenue of top 3 selling department of "
    +
    stateDict[st]
    +
    "'s worst \nperforming store '"
    +
    worst_performing_store[0]+ "'"
)
                   
ssd21_fig.show()

del ssd21


# In[33]:



# ssd22_sporting = sales_master_final.groupby(
#     ['state_id', 'store_id', 'Sporting_event']
# ).agg(
#     {
#         'revenue':sum,
#         'sale_quantity':sum
#     }
# )['revenue'].groupby(
#     ['state_id', 'Sporting_event'],
#     group_keys=False
# ).nlargest(3).reset_index()

# ssd22_sporting

# ssd22_cultural = sales_master_final.groupby(
#     ['state_id', 'store_id', 'Cultural_event']
# ).agg(
#     {
#         'revenue':sum,
#         'sale_quantity':sum
#     }
# )['revenue'].groupby(
#     ['state_id', 'Cultural_event'],
#     group_keys=False
# ).nlargest(3).reset_index()

# ssd22_cultural

# ssd22_national = sales_master_final.groupby(
#     ['state_id', 'store_id', 'National_event']
# ).agg(
#     {
#         'revenue':sum,
#         'sale_quantity':sum
#     }
# )['revenue'].groupby(
#     ['state_id', 'National_event'],
#     group_keys=False
# ).nlargest(3).reset_index()

# ssd22_national

# ssd22_religious = sales_master_final.groupby(
#     ['state_id', 'store_id', 'Religious_event']
# ).agg(
#     {
#         'revenue':sum,
#         'sale_quantity':sum
#     }
# )['revenue'].groupby(
#     ['state_id', 'Religious_event'],
#     group_keys=False
# ).nlargest(3).reset_index()

# ssd22_religious


# In[ ]:





# In[34]:


psd11 = sales_master_final.groupby(
    ['state_id','store_id','Religious_event',]
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
)
display(psd11)

psd11_01 = psd11['revenue'].groupby(
    "state_id", 
    group_keys=False
).nlargest(3).reset_index()

display(psd11_01)

psd11_02 = psd11['sale_quantity'].groupby(
    "state_id", 
    group_keys=False
).nlargest(3).reset_index()

display(psd11_02)



psd11_fig = make_subplots(
    rows=1, 
    cols=2, 
    shared_yaxes=True
)

psd11_fig.add_trace(
    go.Bar(
        name = 'Revenue',
        x = psd11_01[psd11_01.state_id==st]['Religious_event'],
        y = psd11_01[psd11_01.state_id==st]['revenue'],
    ),
    1, 1
)
psd11_fig.add_trace(
    go.Bar(
        name = 'Sale',
        x = psd11_02[psd11_02.state_id==st]['Religious_event'],
        y = psd11_02[psd11_02.state_id==st]['sale_quantity'],
    ),
    1, 2
)

psd11_fig.update_layout(
    title_text=stateDict[st] 
    + 
    "'s top 3 selling "+"religious events"+" in revenue and volumn"
)
psd11_fig.show()

top_3_items_by_revenue = list(psd11_01[psd11_01.state_id==st]['Religious_event'])
top_3_items_by_revenue

del psd11, psd11_01, psd11_02


# In[35]:


def ssd22():
    event_list = list(calender.event_type_1.unique())
    event_list.pop(0)
    eventDF = pd.DataFrame(columns=['state_id', 'store_id', 'event', 'revenue'])
    for event in event_list:
        event = event + "_event"
        print(event)
        df = sales_master_final.groupby(
            ['state_id','store_id', event]
        ).agg(
            {
                'revenue':sum,
                'sale_quantity':sum
            }
        ).reset_index().rename(
            columns={event: "event"}
        )
        eventDF = eventDF.append(df)
        print(eventDF.tail(5))
        
    return eventDF


# In[36]:


all_events = ssd22()

all_events[all_events.state_id == st].groupby(
    ['state_id', 'store_id','event'],
#     group_keys=False
).agg({'revenue':sum}).nlargest(5, columns='revenue').reset_index()


# In[37]:


ssd22 = all_events[all_events.state_id == st].groupby(
    ['state_id','store_id','event'],
#     group_keys=False
).agg({'revenue':sum}).nlargest(5, columns='revenue').reset_index()


ssd22_fig = px.bar(
    ssd22[ssd22.state_id==st],
    x='event', 
    y="revenue",
    facet_col='store_id'
)

ssd22_fig.update_layout(
    title=stateDict[st]
    +
    "'s top 3 stores that have high sales during events"
)

ssd22_fig.show()    


# In[38]:


def plot_psd(event_type):
    
    df = sales_master_final.groupby(
        ['state_id', 'store_id', event_type]
    ).agg(
        {
            'revenue':sum,
            'sale_quantity':sum
        }
    )['revenue'].groupby(
        ['state_id', event_type],
        group_keys=False
    ).nlargest(3).reset_index()    
    
        
    psd_fig = px.bar(
        df[df.state_id==st],
        x=event_type, 
        y="revenue",
        facet_col='store_id'
    )

    psd_fig.update_layout(
        title=stateDict[st]
        +
        "'s top 3 stores that have high sales during "
        +
        event_type
    )

    psd_fig.show()    


# In[39]:


plot_psd("Religious_event")


# In[40]:


plot_psd("Cultural_event")


# In[41]:


plot_psd("National_event")


# In[42]:


plot_psd("Sporting_event")

