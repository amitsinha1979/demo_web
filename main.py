# import streamlit library
import streamlit as st01


st01.title("welcome to streamlit website")
st01.header("Python")
st01.subheader("Java")

# dataset = pd.read_csv("Mall_Customers.csv")
# st01.dataframe(dataset)

name = st01.text_input("Enter your Name : ")
fname = st01.text_input("Enter your Father Name : ")
adr = st01.text_area("Enter your address : ")
classdata = st01.selectbox("Enter your class :",(1,2,3,4,5,6))

button = st01.button("Done")
if button :
    st01.markdown(f""""
        Name : {name}
        Father Name : {fname}
        address : {adr}
        class : {classdata}
    """)

