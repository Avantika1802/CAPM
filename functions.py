import plotly.express as px

#function to plot interactive ploty chart

def interactive_plot(df):
    fig=px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x= df['Date'],y=df[i],name=i)
    fig.update_layout(width=450,margin=dict(l=20,r=20,t=50,b=20),legend=dict(orientation='h',yanchor='bottom',
    y=1.02,xanchor='right',x=1,))
    return fig

# function to normalize the prices based on the initial price
# tells how many times the price has increased from starting

def normalize(df_2):
    df= df_2.copy()#so that there is no change in original data frame
    for i in df.columns[1:]:
        df[i]=df[i]/df[i][0]
    return df

#function to calculate daily returns ==current value-previous closed price/prev closed pice
def daily_return(df):
    df_daily_return= df.copy()
    for i in df.columns[1:]:
        for j in range(1,len(df)):
            df_daily_return[i][j]=((df[i][j]-df[i][j-1])/df[i][j-1])*100
        df_daily_return[i][0]=0 #returns 0 in first row
        return df_daily_return

#function to calculate beta
def calculate_beta(stocks_daily_return,stock):
    #expected return of market
    rm=stocks_daily_return['sp500'].mean()*252
    #calculate beta and alpha
    b,a=np.polyfit(stocks_daily_return['sp500'],stocks_daily_return[stock],1)
    return b,a


