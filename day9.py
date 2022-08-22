import streamlit as zd
import pandas as pd
import numpy as np

zd.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 4),
     columns=['a', 'b', 'c','d'])

zd.line_chart(chart_data)
