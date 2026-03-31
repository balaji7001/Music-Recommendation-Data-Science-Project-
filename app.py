import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/music_dataset_500.csv')

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Music Recommender", layout="wide")

st.title("🎧 Music Recommendation & Analytics Dashboard")

# ---------------------
# SIDEBAR MENU
# ---------------------
menu = st.sidebar.selectbox(
    "Choose Option",
    ["Recommend Songs", "Search Song", "Trending Songs", "Analytics Dashboard"]
)

# -------------------
# 1. RECOMMENDATION
# -------------------
if menu == "Recommend Songs":
    st.header("🎶 Recommend Songs")

    col1, col2 = st.columns(2)

    with col1:
        genre = st.selectbox("Select Genre", df['genre'].unique())

    with col2:
        language = st.selectbox("Select Language", df['language'].unique())

    if st.button("Recommend"):
        result = df[(df['genre'] == genre) & (df['language'] == language)]

        if result.empty:
            st.warning("No songs found!")
        else:
            st.dataframe(result.head(10))

# ----------------------------
# 2. SEARCH
# ----------------------------
elif menu == "Search Song":
    st.header("🔍 Search Song")

    song = st.text_input("Enter song name")

    if st.button("Search"):
        result = df[df['song'].str.lower().str.contains(song.lower())]

        if result.empty:
            st.error("Song not found!")
        else:
            st.dataframe(result.head(10))

# ----------------------------
# 3. TRENDING
# ----------------------------
elif menu == "Trending Songs":
    st.header("🔥 Trending Songs")

    if st.button("Show Trending"):
        st.dataframe(df.sample(10))

# ----------------------------
# 4. ANALYTICS DASHBOARD
# ----------------------------
elif menu == "Analytics Dashboard":
    st.header("📊 Analytics Dashboard")

    col1, col2 = st.columns(2)

    # Genre Chart
    with col1:
        st.subheader("🎼 Genre Distribution")
        fig1, ax1 = plt.subplots()
        df['genre'].value_counts().head(10).plot(kind='bar', ax=ax1)
        st.pyplot(fig1)

    # Language Pie
    with col2:
        st.subheader("🌍 Language Distribution")
        fig2, ax2 = plt.subplots()
        df['language'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax2)
        ax2.set_ylabel("")
        st.pyplot(fig2)

    # Top Artists
    st.subheader("🎤 Top Artists")
    fig3, ax3 = plt.subplots()
    df['artist'].value_counts().head(10).plot(kind='bar', ax=ax3)
    st.pyplot(fig3)

    # Histogram
    st.subheader("📉 Histogram")
    fig4, ax4 = plt.subplots()
    ax4.hist(df['genre'].value_counts())
    st.pyplot(fig4)

    # Line Graph
    st.subheader("📈 Trend Line")
    df['index'] = range(len(df))
    fig5, ax5 = plt.subplots()
    ax5.plot(df['index'], df['id'])
    st.pyplot(fig5)