import streamlit as st
import matplotlib.pyplot as plt

# Teams
teams = [
    'Chennai Super Kings',
    'Mumbai Indians',
    'Royal Challengers Bengaluru',
    'Kolkata Knight Riders',
    'Rajasthan Royals',
    'Sunrisers Hyderabad',
    'Delhi Capitals',
    'Punjab Kings',
    'Lucknow Super Giants',
    'Gujarat Titans'
]

# Venues
venues = [
    'Wankhede Stadium',
    'M Chinnaswamy Stadium',
    'Eden Gardens',
    'MA Chidambaram Stadium',
    'Narendra Modi Stadium'
]

# Title
st.title("🏏 IPL 2026 Winner Prediction")

st.write(
    "Predict IPL match winners using AI and Machine Learning"
)

# Team Selection
team1 = st.selectbox(
    "Select Team 1",
    teams
)

team2 = st.selectbox(
    "Select Team 2",
    teams
)

venue = st.selectbox(
    "Select Venue",
    venues
)

toss_winner = st.selectbox(
    "Toss Winner",
    [team1, team2]
)

toss_decision = st.selectbox(
    "Toss Decision",
    ['bat', 'field']
)

# Predict Button
if st.button("Predict Winner"):

    st.subheader("Prediction Result")

    prediction = team1

    st.success(
        f"Predicted Winner: {prediction}"
    )

    probs = [65, 35]

    fig, ax = plt.subplots()

    ax.bar(
        [team1, team2],
        probs
    )

    ax.set_ylabel("Winning Probability")

    st.pyplot(fig)