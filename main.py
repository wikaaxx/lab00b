import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json


# panda ex
def ex1():
    df = pd.read_csv('sales_data.csv')

    profit = df['total_profit'].values
    months = df['month_number'].values

    plt.figure()
    plt.plot(months, profit, label=' Month - wise Profit data of last year')
    plt.xlabel('Month number')
    plt.ylabel('Profit [$]')
    plt.xticks(months)
    plt.title('Company profit per month')
    plt.yticks([100e3, 200e3, 300e3, 400e3, 500e3])
    plt.show()


def ex2():
    df = pd.read_csv('sales_data.csv')

    profit2 = df['total_profit'].values
    months = df['month_number'].values

    plt.figure()
    plt.plot(months,profit2, label='Profit data of last year', color='r', marker='o',markerfacecolor='k',linestyle='-',linewidth=3)
    plt.xlabel('Month number')
    plt.ylabel('Profit')
    plt.legend(loc='lower left')
    plt.title('Comp sales of last year')
    plt.xticks(months)
    plt.yticks([100e3,200e3,300e3,400e3,500e3])
    plt.show()

def ex3():
    df =pd.read_csv('sales_data.csv')
    months = df['month_number'].values
    facecreams = df['facecream'].values
    facewashes = df['facewash'].values
    toothpastes = df['toothpaste'].values
    bathingsoaps = df['bathingsoap'].values
    shampoos = df['shampoo'].values
    moisturizers = df['moisturizer'].values

    plt.figure()
    plt.plot(months,facewashes,label='facewash')
    plt.plot(months,facecreams,label='facecream')
    plt.plot(months,toothpastes,label ='toothpaste')
    plt.plot(months,bathingsoaps,label = 'bathing soap')
    plt.plot(months,shampoos,label='shampoo')
    plt.plot(months,moisturizers,label='moisturizer')
    plt.xticks(months)
    plt.yticks([1e3,2e3,3e3,4e3,5e3,6e3,7e3,8e3,9e3])
    plt.legend(loc='upper left')
    plt.xlabel('months')
    plt.ylabel('sales of each product in each month')
    plt.title('sales')
    plt.show()

def ex4():
    df = pd.read_csv('sales_data.csv')
    toothpastes=df['toothpaste'].values
    months = df['month_number'].values

    plt.figure()
    plt.scatter(months,toothpastes,label='toothpaste_sales')
    plt.xlabel('months')
    plt.ylabel('sales in dollars')
    plt.xticks(months)
    plt.grid(True, linewidth=0.3)
    plt.title('toothpaste sales')
    plt.legend(loc='upper left')
    plt.show()

def ex5():
    df = pd.read_csv('sales_data.csv')
    bathsoaps=df['bathingsoap'].values
    months =df['month_number'].values
    plt.figure()
    plt.bar(months,bathsoaps,label='bathsoap sales')
    plt.xticks(months)
    plt.xlabel('months')
    plt.title('bathsoap sales chart')
    plt.legend(loc='upper left')
    plt.savefig('bathsoap_sales_data.png', dpi=150)
    plt.show()

def ex6():
    df = pd.read_csv('sales_data.csv')
    profit=df['total_profit'].values
    plt.figure()
    p_range=[150e3,175e3,200e3,225e3,250e3,300e3,350e3]
    plt.hist(profit,p_range,label='profit')
    plt.xlabel('profit range')
    plt.ylabel('profit in dollars')
    plt.xticks(p_range)
    plt.title('profit')
    plt.legend(loc='upper left')
    plt.show()

def ex7():
    df =pd.read_csv('sales_data.csv')
    months= df['month_number'].values
    bathingsoaps=df['bathingsoap'].values
    facewashes=df['facewash'].values
    f, axs = plt.subplots(2,1,sharex=True)
    axs[0].plot(months, bathingsoaps, label='bathing soap sales')
    axs[0].set_title('sales of bathing soap')
    axs[0].grid()
    axs[0].legend()
    axs[1].plot(months, facewashes,label='facewash sales')
    axs[1].grid()
    axs[1].legend()
    axs[1].set_title('sales of facewash')
    plt.xticks(months)
    plt.xlabel('month no')
    plt.ylabel('sales units')
    plt.show()

#JSON EXERCISES

def ex8():
    json_obj='{ "Month":"January","Day":"Monday","No_of_days":"31"}'
    in_python=json.loads(json_obj)
    print(in_python)
    print(in_python['Month'])
    print(in_python['Day'])

def ex9():
    in_python ={'month':'january','day':'monday'}
    print(in_python)
    print(type(in_python))
    j_obj=json.dumps(in_python)
    print(j_obj)

def ex10():
    python_int =3
    python_t =True
    python_n=None
    j_obj1=json.dumps(python_int)
    print(j_obj1)
    j_obj2=json.dumps(python_n)
    print(j_obj2)
    j_obj3=json.dumps(python_t)
    print(j_obj3)

def ex11():
    with open('states.json') as f:
        json_data=json.load(f)
    print('json keys: ',[state.keys() for state in json_data['states']][0])
    with open('new_states.json','w') as f:
        json.dump(json_data,f,indent=2)
    with open('new_states.json') as f:
        state_d=json.load(f)
    print('new json keys: ', [state.keys() for state in state_d['states']][0])

ex11()




