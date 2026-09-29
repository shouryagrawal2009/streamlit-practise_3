import numpy as np
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="kinematics visualiser", page_icon="A", layout="wide")

st.markdown("""
<style>
h1 {color: Aqua;}
.stApp {background-color: #f8f9fa;}
[class*="st-key-"][class*="_dec"] button {
  width: 36px;
  height: 36px;
  min-height: 36px;
  border-radius: 50%;
  padding: 0;
  border: 2px solid black;
  background: white;
  font-size: 50px;
  font-weight: bold;
  line-height:10;
}
[class*="st-key-"][class*="_inc"] button {
  width: 36px;
  height: 36px;
  min-height: 36px;
  border-radius: 50%;
  padding: 0;
  border: 2px solid black;
  background: white;
  font-size: 50px;
  font-weight: bold;
  right:100px;
}

[class*="st-key-"][class*="_inc"],
[class*="st-key-"][class*="_inc"] .stButton button {
  display:flex;
  jutify-content: flex-end !important;
}

[class*="st-key-"][class*="_dec"],
[class*="st-key-"][class*="_dec"] .stButton button {
  display: flex;
  justify-content:  flex-start !important;
}
</style>
""", unsafe_allow_html=True)

def stepper(label, min_v, max_v, default, key):
  if key not in st.session_state:
    st.session_state[key]= default
  def dec():
    st.session_state[key] = max(min_v, st.session_state[key] - 1)
  def inc():
    st.session_state[key]=  min(max_v, st.session_state[key] +1)

  st.sidebar.write(label)
  c1, c2, c3= st.sidebar.columns([1,4,1])
  c1.button("-", key=key + "_dec", on_click=dec)
  c2.button("+", key=key + "_inc", on_click=inc)
  return c2.slider(label, min_v, max_v, key=key, label_visibility="collapsed")
  

st.title("Kinematics Visualizer")

u=stepper("Initial velocity (m/s)",0,50, 20,"u")
a=stepper("Acceleartion (m/s2)",0, 20, 10,"a")
T=stepper("Total time (s)", 1, 30, 10,"T")

t= np.linspace(0, T, 200)
v= u+ a*t
X= u*t + 0.5*a*t**2

fig= go.Figure(go.Scatter(x=t, y=v, mode="lines"))
fig.update_layout(title="Velocity vs Time", xaxis_title="Time(s)",yaxis_title="Velocity (m/s)", template="plotly_white")
fig.update_traces(line_color="#3B5BDB", line_width=3)

fig2= go.Figure(go.Scatter(x=t, y=X, mode="lines"))
fig2.update_layout(title="Position vs Time", xaxis_title="Time(s)",yaxis_title="Position(m)", template="plotly_white")
fig2.update_traces(line_color="#E8590C", line_width=3)

tab1, tab2 = st.tabs(["Velocity-Time", "Position-Time"])
with tab1:
  st.plotly_chart(fig, use_container_width=True)
with tab2:
  st.plotly_chart(fig2, use_container_width=True)
