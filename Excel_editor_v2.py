import os
import pandas as pd
import streamlit as st
import datetime

# reload all
def rerun():
    raise st.ScriptRunner.RerunException(st.ScriptRequestQueue.RerunData(None))

# selecting file
start_dir = os.getcwd()
prepper_file = f'{start_dir}//data//Prepper_list.xlsx'
backup_file = f'{start_dir}//data//Prepper_{datetime.date.today()}.xlsx'

# load data
df = pd.read_excel(prepper_file)
df = df.fillna('_')
df = df.astype(str)
st.dataframe(df, width=1000, height=450)


# make input sidebar
#  delete items from df
delete_row = st.text_input("Delete Row:",value='')
if st.button('delete') == True:
    df.drop(labels=int(delete_row), axis=0, inplace=True)
    df.to_excel(prepper_file, index=False) 
    rerun()

if st.button('Save_backup') == True:
    df.to_excel(backup_file, index=False) 

#make add items
row_add = {}
for nr, item in enumerate(df.columns): 
    row_add[item] = st.sidebar.text_input(item, value='')
if st.sidebar.button('add') == True:
    connect_df = pd.DataFrame()
    connect_df = connect_df.append(row_add, ignore_index=True)
    df = df.append(connect_df)
    df.sort_values(by=['Voedsel'], inplace=True)
    df.to_excel(prepper_file, index=False)
    rerun()

st.write(row_add)

