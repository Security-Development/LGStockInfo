from datetime import datetime as date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import pandas_datareader.data as pd
          
start = date(2010, 1, 4)
end = date(2021, 8, 19)
lg = pd.get_data_yahoo('078930.KS', start, end)

def num_format(int):
    text = str(int)
    text = list(text)
    count = 0
    for i in range(1, len(text)):
        if len(text) == 4 and text[0] == '-':
            break
            
        if i % 3 == 0:
            text.insert(-1 * (i + count), ',')
            count += 1
    return "".join(text)
        
    
    
def get_view():
    money = 0
    text = ''
    for i, j in lg['Adj Close'].items():
        text = f'{"▼" if money > j else "▲"} {num_format(round(-1 * (money - j)))}원'
        print(str(i).split(' ')[0]+'에 LG 주식가격: ' + str(num_format(round(j))) + '원' + text)
        money = j

plt.figure('LG Stock')
plt.title('LG Stock')
plt.plot(lg.index, lg['Adj Close'])
get_view()
plt.show()

