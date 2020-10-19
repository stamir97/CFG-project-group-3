import csv
import pandas as pd


def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


def run():
    data = read_data()
    sales = []

    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    total = sum(sales)
    print(f'Total sales: {total:,d}')


    #using pandas to read file
    df = pd.read_csv('sales.csv')

    # FINDING MAX AND MIN
    max_sales = df['sales'].max()
    min_sales = df['sales'].min()
    mean_sales = int(df['sales'].mean())
    print(f'Max sales: {max_sales:,d}')
    print(f'Min sales: {min_sales:,d}')
    print(f'Mean sales: {mean_sales:,d}')



run()
