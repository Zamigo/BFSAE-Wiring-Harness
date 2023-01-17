import pandas as pd

raw_data = pd.read_csv('Manufacturing Documents - 1_17_22.csv')
print(raw_data)


def define_num(table):
    # this function makes sure that each row of the "#"
    # category has an associated wire # to it, instead
    # of displaying "nan"

    nan_table = table["#"].isna() # true-false table, shows true where nan is displayed

    for num in table.index: # runs through the table and sets nan spots to the correct number
        if nan_table.at[num] == False:
            set_num = table.at[num, "#"]
        elif nan_table.at[num] == True:
            table.at[num, "#"] = set_num
    print(table)