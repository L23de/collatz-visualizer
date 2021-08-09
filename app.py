import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def collatz_algo(start_int: int):
    """
    Collatz's Conjecture
    If even: Divide by 2
    If odd: Multiple by 3 and add 1
    """
    if start_int == 0:  # Special case
        yield 0
    else:
        while start_int != 1:
            if start_int % 2 == 0:  # If even
                start_int = start_int / 2
            else:  # If odd
                start_int = start_int * 3 + 1
            yield start_int


st.write(
    """
# Visualizing Collatz Conjecture

Introduced by Lothar Collatz in 1937, the conjecture states that:

- If the number is even, divide it by 2
- If the number is odd, multiply it by 3 and add one

"Almost all" numbers converge to 1 according to these rules. This is the reason why it is a conjecture and not a mathematical proof. No one has been able to prove such is true for EVERY number 
"""
)
start_int = st.number_input("Starting integer:", value=5, min_value=0)
results = collatz_algo(start_int * 2)

st.line_chart(results)
