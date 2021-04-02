# import data_preprocess as pp
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


class CHART_MAKER:
    
    def __init__(self, data_dict):
        self.data = data_dict
        self.stateDict = {
            'CA': 'California',
            'TX': 'Texas',
            'WI': 'Wisconsin'
        }
        self.top_3_dept_by_revenue=None   
        
    def plot_summary11(self):
        summary11 = self.data['summary11']

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
                        
        return summary11_fig

    def plot_summary12(self):
        summary12 = self.data['summary12']

        summary12_fig = px.bar(
            summary12,
            x="store_id", 
            y=['sale_quantity', "revenue"],  
            barmode="stack"
        )

        summary12_fig.update_layout(
            title="Wallmart's Total Revenue for store in all States"
        )
                            
        # summary12_fig.show()

        # del summary12

        return summary12_fig


    def plot_summary21(self):
        summary21 = self.data['summary21']

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
                        
        # summary21_fig.show()

        # del summary21

        return summary21_fig


    def plot_summary22(self):
        summary22 = self.data['summary22']

        summary22_fig = px.sunburst(summary22, path=['state_id', 'cat_id', 'item_id'], values='revenue')
        summary22_fig.update_layout(
            title="Wallmart's Top Three selling products in each state and category"
        )
        # summary22_fig.show()

        # del summary22

        return summary22_fig

    def display_ssd00(self, st):
        ssd00 = self.data['ssd00']

        best_store = self.data['ssd00_01']

        worst_store = self.data['ssd00_02']

        best_of_state = best_store[best_store['state_id']==st]
        worst_of_state = worst_store[worst_store['state_id']==st]

        return best_of_state, worst_of_state


    def plot_ssd11(self, st='CA'):
        ssd11 = self.data['ssd11']

        ssd11_01 = self.data['ssd11_01']

        ssd11_02 = self.data['ssd11_02']

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
            title_text=self.stateDict[st] 
            + 
            "'s top 3 selling departments in revenue and volumn"
        )
        # ssd11_fig.show()

        self.top_3_dept_by_revenue = list(ssd11_01[ssd11_01.state_id==st]['dept_id'])
        

        # del ssd11, ssd11_01, ssd11_02

        return ssd11_fig


    def plot_ssd12(self, st='CA'):
        ssd12 = self.data['ssd12']

        ssd12_cond = (ssd12.state_id==st) & (ssd12.dept_id.isin(self.top_3_dept_by_revenue))

        ssd12_fig = px.bar(
            ssd12[ssd12_cond],
            x='store_id', 
            y="revenue",
            facet_col='dept_id'

        )

        ssd12_fig.update_layout(
            title="Revenue of "
            +
            self.stateDict[st]
            +
            "'s top 3 selling department's best performing stores"
        )
                        
        # ssd12_fig.show()

        # del ssd12

        return ssd12_fig

    def plot_ssd21(self, st='CA'):
        ssd21 = self.data['ssd21']

        worst_performing_store = self.data[
            'state_worst_stores'
        ][
            self.data['state_worst_stores'].state_id==st
        ][
            'store_id'
        ]

        ssd21_fig = px.bar(
            ssd21,
            x='dept_id', 
            y="revenue",
        )

        ssd21_fig.update_layout(
            title="Revenue of top 3 selling department of "
            +
            self.stateDict[st]
            +
            "'s worst \nperforming store '"
            +
            worst_performing_store[0]+ "'"
        )
                        
        # ssd21_fig.show()

        # del ssd21

        return ssd21_fig
 

    def plot_ssd22(self, st='CA'):
        ssd22 = self.data['ssd22']

        ssd22_fig = px.bar(
            ssd22[ssd22.state_id==st],
            x='event', 
            y="revenue",
            facet_col='store_id'
        )

        ssd22_fig.update_layout(
            title=self.stateDict[st]
            +
            "'s top 5 revenue generating events by store"
        )

        # ssd22_fig.show()    

        return ssd22_fig

    def plot_esd(self, event_type, st='CA'):

        df1 = self.data['df1'+event_type]   
        df2 = self.data['df2'+event_type] 
        
        esd_fig = go.Figure(
            data=[
                go.Bar(
                    name = 'Best Store '+ df1[df1.state_id==st]['store_id'].unique()[0],
                    x = df1[df1.state_id==st][event_type],
                    y = df1[df1.state_id==st]['revenue'],
                ),
                go.Bar(
                    name = 'Worst Store '+ df2[df2.state_id==st]['store_id'].unique()[0],
                    x = df2[df2.state_id==st][event_type],
                    y = df2[df2.state_id==st]['revenue']
                )
            ],
        )
            


        esd_fig.update_layout(
            title=self.stateDict[st]
            +
            "'s top 3 stores that have high sales during "
            +
            event_type
        )
        
        # esd_fig.show()  

        return esd_fig 
    
    # # def psd(self):
    # # def plot_psd11(self):
    # # def plot_psd12(self):
    # # def plot_psd21(self):
    # # def plot_psd22(self):



