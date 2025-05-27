import streamlit as st
from datetime import time

# Slider Test

class Slider:
    def __init__(self, title:str, start:int, end:int, init:int):
        self.number = st.slider(title, start, end, init)

    def selected(self):
        return self.number

title = "Test Slider"
start = 0
end = 100
init = (start + end) // 2
slider = Slider(title, start, end, init)

# Range Slider Test

class RangeSlider:
    def __init__(self, title:str, start:int, end:int, init_start:int, init_end:int):
        self.appointment = st.slider(title, start, end, (init_start, init_end))

    def selected_start(self):
        return self.appointment[0]

    def selected_end(self):
        return self.appointment[1]

init_start = 5
init_end = 95

range_slider = RangeSlider(title, start, end, init_start, init_end)
st.write("You're scheduled for:", range_slider.selected_start(), " to ", range_slider.selected_end())

class TimeRangeSlider:
    def __init__(self, title:str, init_start:time, init_end:time):
        self.appointment = st.slider(title, value=(init_start, init_end))

    def selected_start(self):
        return self.appointment[0]

    def selected_end(self):
        return self.appointment[1]


init_start = time(11, 30)
init_end = time(12, 45)

time_range_slider = TimeRangeSlider(title, init_start, init_end)
st.write("You're scheduled for:", time_range_slider.selected_start(), " to ", time_range_slider.selected_end())