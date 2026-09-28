import yfinance as yf  

# Get data  
def get_data(s):  
    d = yf.download(s, period="1mo")  
    return d['Close']  

# Buy/Sell logic  
def bot(s):  
    p = get_data(s)  
    s_avg = p.rolling(3).mean()  # Short average  
    l_avg = p.rolling(7).mean()  # Long average  

    for i in range(len(p)):  
        if s_avg[i] > l_avg[i]:  
            print(p.index[i].date(), "- BUY")  
        elif s_avg[i] < l_avg[i]:  
            print(p.index[i].date(), "- SELL")  
        else:  
            print(p.index[i].date(), "- HOLD")  

# Check for stock  
bot("AAPL")  
