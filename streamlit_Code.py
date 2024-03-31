import streamlit as st
import pickle
import pandas as pd

teams=['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

City=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

task=pickle.load(open('match.pkl','rb'))
st.title('IPL Win Predictor')

column1,column2=st.columns(2)

with column1:
    batting_team=st.selectbox("Select the batting team",sorted(teams))
with column2:
    bowling_team=st.selectbox("Select the bowling team",sorted(teams))


host_city=st.selectbox("Select the city hosting the match",sorted(City))

target=st.number_input("Target")

column3,column4,column5=st.columns(3)

with column3:
    runs=st.number_input("Current Score")
with column4:
    wickets=st.number_input("Wickets fallen")
with column5:
    overs=st.number_input("Overs Completed")


if st.button("Predict Probablity"):
    runs_left=target-runs
    balls_left=120-(overs*6)
    wickets_left=10-wickets
    crr=runs/overs
    rrr=(runs_left*6)/balls_left

    stats=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[host_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    st.table(stats)
    result=task.predict_proba(stats)
    loss=result[0][0]
    win=result[0][1]
    st.header(batting_team + "-" + str(round(win*100))+ "%")
    st.header(bowling_team + "-" + str(round(loss*100))+ "%")
    
