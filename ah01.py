
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    # font="monospace"
    selected=option_menu(
       
        menu_title= "Main Menu",
        options=["DASHBOARD","PROJECTS","MY TASK","CALENDER",'REPORTS',"SETTINGS"],
        icons=["box","bag-plus","envelope","calendar","pie-chart","tools"],
        menu_icon="cast",
    )


    if selected=="DASHBOARD":
        st.title(f"You are selected {selected}")
    if selected=="PROJECTS":
        st.title(f"You are selected {selected}")
    if selected=="MY TASK":
        st.title(f"You are selected {selected}")
    if selected=="CALENDER":
        st.title(f"You are selected {selected}")
    if selected=="REPORTS":
        st.title(f"You are selected {selected}")
    if selected=="SETTINGS":
        st.title(f"You are selected {selected}")
    


st.title("Option menu")


