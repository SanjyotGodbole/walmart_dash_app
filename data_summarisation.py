import pandas as pd
import data_preprocess as pp

sales_master_final = pp.preprocess()

summary11 = sales_master_final.groupby(
    'state_id'
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
).reset_index()

summary11.to_csv('summary11.csv',index=False)

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

summary12.to_csv('summary12.csv',index=False)

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

summary21.to_csv('summary21.csv',index=False)

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

summary22.to_csv('summary22.csv',index=False)

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

# display(ssd00)

ssd00_01 = ssd00['revenue'].groupby(
    ['state_id'],
    group_keys=False
).nlargest(1).reset_index()
# display(ssd00_01)

ssd00_02 = ssd00['revenue'].groupby(
    ['state_id'],
    group_keys=False
).nsmallest(1).reset_index()

ssd00.to_csv('ssd00.csv',index=False)
ssd00_01.to_csv('ssd00_01.csv',index=False)
ssd00_02.to_csv('ssd00_02.csv',index=False)

ssd11 = sales_master_final.groupby(
    ['state_id','cat_id','dept_id',]
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
).reset_index()

ssd11_01 = ssd11[ssd11["state_id"]==st].groupby(
    ["state_id", 'dept_id'],
).agg({'revenue': 'sum'})['revenue'].nlargest(3).reset_index()

ssd11_02 = ssd11[ssd11["state_id"]==st].groupby(
    ["state_id", 'dept_id'],
).agg({'sale_quantity': 'sum'})['sale_quantity'].nlargest(3).reset_index()

top_3_dept_by_revenue = list(ssd11_01['dept_id'])

ssd11.to_csv('ssd11.csv',index=False)
ssd11_01.to_csv('ssd11_01.csv',index=False)
ssd11_02.to_csv('ssd11_02.csv',index=False)

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

ssd12.to_csv('ssd12.csv',index=False)

state_worst_stores = sales_master_final.groupby(
    ['state_id','store_id']
).agg(
    {'revenue':sum}
)['revenue'].groupby(
    ['state_id'],
    group_keys=False
).nsmallest(1).reset_index()


state_worst_stores.to_csv('state_worst_stores.csv',index=False)

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

ssd21.to_csv('ssd21.csv',index=False)

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

all_events = ssd22()

all_events[all_events.state_id == st].groupby(
    ['state_id', 'store_id','event'],
#     group_keys=False
).agg({'revenue':sum}).nlargest(5, columns='revenue').reset_index()

all_events.to_csv('all_events.csv',index=False)

ssd22 = all_events[all_events.state_id == st].groupby(
    ['state_id','store_id','event'],
#     group_keys=False
).agg({'revenue':sum}).nlargest(5, columns='revenue').reset_index()

ssd22.to_csv('ssd22.csv',index=False)

psd11 = sales_master_final.groupby(
    ['state_id','store_id','Religious_event',]
).agg(
    {
        'revenue':sum,
        'sale_quantity':sum
    }
)

psd11_01 = psd11['revenue'].groupby(
    "state_id", 
    group_keys=False
).nlargest(3).reset_index()

psd11_02 = psd11['sale_quantity'].groupby(
    "state_id", 
    group_keys=False
).nlargest(3).reset_index()

psd11.to_csv('psd11.csv',index=False)
psd11_01.to_csv('psd11_01.csv',index=False)
psd11_02.to_csv('psd11_02.csv',index=False)

