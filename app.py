import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
import catboost

def more(self):
    pass



# Initialize 
if 'page' not in st.session_state:
    st.session_state.page = 'Home'


st.sidebar.title("Navigation -->")

# sidebar
home_button = st.sidebar.button("Home")
prediction_button = st.sidebar.button("Prediction")
more_button = st.sidebar.button("More")


# button click
if home_button:
    st.session_state.page = 'Home'

elif prediction_button:
    st.session_state.page = 'Prediction'

elif more_button:
    st.session_state.page = 'More'

# Load Model
model = catboost.CatBoostRegressor()
model.load_model('pubg_model.cbm')

# Display page
if st.session_state.page == 'Home':
    st.title('Chicken Dinner Prediction 🍗')
    st.image('https://media.giphy.com/media/QCC0h2pdbvGN5JTBmk/giphy.gif', use_column_width=True)
    st.markdown('''
    ### <font color="Tan">Data Description</font><a class="anchor" id="desc"></a>
    - <b style="color: purple;">DBNOs -</b> Number of enemy players knocked.
    - <b style="color: purple;">assists -</b> Number of enemy players this player damaged that were killed by teammates.
    - <b style="color: purple;">boosts -</b> Number of boost items used.
    - <b style="color: purple;">damageDealt -</b> Total damage dealt. Note: Self-inflicted damage is subtracted.
    - <b style="color: purple;">headshotKills -</b> Number of enemy players killed with headshots.
    - <b style="color: purple;">heals -</b> Number of healing items used.
    - <b style="color: purple;">killPlace -</b> Ranking in match of number of enemy players killed.
    - <b style="color: purple;">killPoints -</b> Kills-based external ranking of player. (Think of this as an Elo ranking where only kills matter.) If there is a value other than -1 in rankPoints, then any 0 in killPoints should be treated as a “None”.
    - <b style="color: purple;">killStreaks -</b> Max number of enemy players killed in a short amount of time.
    - <b style="color: purple;">kills -</b> Number of enemy players killed.
    - <b style="color: purple;">longestKill -</b> Longest distance between player and player killed at time of death. This may be misleading, as downing a player and driving away may lead to a large longestKill stat.
    - <b style="color: purple;">matchDuration -</b> Duration of match in seconds.
    - <b style="color: purple;">rankPoints -</b> Elo-like ranking of player. This ranking is inconsistent and is being deprecated in the API’s next version, so use with caution. Value of -1 takes place of “None”.
    - <b style="color: purple;">revives -</b> Number of times this player revived teammates.
    - <b style="color: purple;">PlayerInMatch -</b> Number of Players in the match calculated, by grouping people with same MatchID and taking their count.   
    - <b style="color: purple;">roadKills -</b> Number of kills while in a vehicle.
    - <b style="color: purple;">teamKills -</b> Number of times this player killed a teammate.
    - <b style="color: purple;">vehicleDestroys -</b> Number of vehicles destroyed.
    - <b style="color: purple;">Totaldistance -</b> Total distance traveled on foot, vehicles, and by swimming measured in meters.
    - <b style="color: purple;">weaponsAcquired -</b> Number of weapons picked up.
    - <b style="color: purple;">winPoints -</b> Win-based external ranking of player. (Think of this as an Elo ranking where only winning matters.) If there is a value other than -1 in rankPoints, then any 0 in winPoints should be treated as a “None”.
    - <b style="color: purple;">numGroups -</b> Number of groups we have data for in the match.
    - <b style="color: purple;">maxPlace -</b> Worst placement we have data for in the match. This may not match with numGroups, as sometimes the data skips over placements.
    ''', unsafe_allow_html=True)

if st.session_state.page == 'Prediction':
    data = {}
    col1, col2 = st.columns(2)
    # Number input for continuous features
    with col1:
        data['DBNOs'] = st.number_input("DBNOs", min_value=0, max_value=100, value=0)
        data['headshotKills'] = st.number_input("Headshot Kills", min_value=0, max_value=100, value=0)
        data['killPlace'] = st.number_input("killPlace", min_value=0, max_value=100, value=37)
        data['killPoints'] = st.number_input("Kill Points", min_value=0, max_value=1000, value=0)
        data['killStreaks'] = st.number_input("Kill Streak", min_value=0, max_value=100, value=0)
        data['longestKill'] = st.number_input("Longest Kill", min_value=0.0, max_value=9000.0, value=0.0)
        data['matchDuration'] = st.number_input("matchDuration", min_value=0, max_value=5000, value=1774)
        data['maxPlace'] = st.number_input("maxPlace", min_value=0, max_value=100, value=29)
        data['numGroups'] = st.number_input("numGroups", min_value=1, max_value=100, value=28)
        data['rankPoints'] = st.number_input("rankPoints", min_value=0, max_value=2000, value=1766)
        data['roadKills'] = st.number_input("Road Kills", min_value=0, max_value=50, value=0)
        data['teamKills'] = st.number_input("Team Kills", min_value=0, max_value=50, value=0)
   
    with col2:
        data['vehicleDestroys'] = st.number_input("vehicleDestroys", min_value=0, max_value=50, value=0) 
        data['weaponsAcquired'] = st.number_input("Weapons Acquired", min_value=0, max_value=100, value=6)
        data['winPoints'] = st.number_input("winPoints", min_value=0, max_value=1000, value=0)
        data['Totaldistance'] = st.number_input("Total Distance", min_value=0.0, max_value=100000.0, value=9423.0)
        playesinmatch = st.number_input("Players Strted With ", min_value=1, max_value=100, value=90)
        data['PlayersInMatch'] = playesinmatch
        normalizing_factor = (100 - data['PlayersInMatch']/100)+1
        data['headshot_rate'] = st.number_input("headshot_rate", min_value=0.0, max_value=100.0, value=0.0)
        kills = st.number_input("kills", min_value=0.0, max_value=60.0, value=0.0)
        data['killsNorm'] = kills * normalizing_factor
        damageDealt = st.number_input("damageDealtNorm", min_value=0.0, max_value=1000.0, value=0.0)
        data['damageDealtNorm'] = damageDealt * normalizing_factor
        maxPlace = st.number_input("Rank died at", min_value=0, max_value=100, value=2)
        data['maxPlaceNorm'] = maxPlace * normalizing_factor
        matchDuration = st.number_input("matchDuration", min_value=0, max_value= 7200, value = 2800)
        data['matchDurationNorm'] = matchDuration * normalizing_factor
        data['healsnboosts'] = st.number_input("healsnboosts", min_value=0, max_value=25, value=0)
        data['assist'] = st.number_input("assist", min_value=0, max_value=8, value=0)

    match_type = st.selectbox("Select Match Type", 
                          options=[
                              'crashfpp', 'crashtpp', 'duo', 'duo-fpp', 
                              'flarefpp', 'flaretpp', 'normal-duo', 
                              'normal-duo-fpp', 'normal-solo', 
                              'normal-solo-fpp', 'normal-squad', 
                              'normal-squad-fpp', 'solo', 
                              'solo-fpp', 'squad', 'squad-fpp'])

    # Initialize all match types as False
    all_match_types = [
        'crashfpp', 'crashtpp', 'duo', 'duo-fpp', 
        'flarefpp', 'flaretpp', 'normal-duo', 
        'normal-duo-fpp', 'normal-solo', 
        'normal-solo-fpp', 'normal-squad', 
        'normal-squad-fpp', 'solo', 
        'solo-fpp', 'squad', 'squad-fpp'
    ]

    # Mark the selected match type as True and others as False
    for mt in all_match_types:
        if mt == match_type:
            data[f"matchType_{mt}"] = True
        else:
            data[f"matchType_{mt}"] = False



    df_input = pd.DataFrame([data])

    # Display the input DataFrame
    st.write("User Input Data:")
    st.write(df_input)

    if st.button('Predict'):
        # Prepare input data
        df = pd.DataFrame([data])
        df_x = StandardScaler().fit_transform(df)
        x = pd.DataFrame(df_x, columns=df.columns, index=df.index)

        # Generate prediction
        predictions = model.predict(x)
        
        st.success(predictions)
if st.session_state.page == 'More':
    st.markdown("""
### Connect with Me
                
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/yash-gupta09) </br>
[![X](https://img.shields.io/badge/X-black.svg?logo=X&logoColor=white)](https://x.com/YashGup4748011) </br>
[![Email](https://img.shields.io/badge/Email-yellow.svg?logo=gmail&logoColor=white)](mailto:yash733622@gmail.com) </br>
[![Instagram](https://img.shields.io/badge/Instagram-red.svg?logo=Instagram&logoColor=darkpink)](https://www.instagram.com/yash_gupta202) </br>""", unsafe_allow_html=True)


