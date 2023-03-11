import streamlit as st

# Set page title
st.title("Basic Calculator")

# Define function for addition


def add(x, y):
    return x + y

# Define function for subtraction


def subtract(x, y):
    return x - y

# Define function for multiplication


def multiply(x, y):
    return x * y

# Define function for division


def divide(x, y):
    return x / y


# Create page content
st.write("""
# Welcome to the Basic Calculator
""")

# Get user input
operation = st.selectbox("Select an operation", [
                         "Addition", "Subtraction", "Multiplication", "Division"])
num1 = st.number_input("Enter the first number", format="%d", value=0)
num2 = st.number_input("Enter the second number", format="%d", value=0)

# Perform calculation based on user input
if operation == "Addition":
    result = add(num1, num2)
elif operation == "Subtraction":
    result = subtract(num1, num2)
elif operation == "Multiplication":
    result = multiply(num1, num2)
else:
    result = divide(num1, num2)

# Display result
st.markdown(f"<h1>Result: {result}</h1>", unsafe_allow_html=True)
