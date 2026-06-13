import streamlit as st
import requests

st.set_page_config(page_title="News Dashboard", layout="wide")
st.title("📰 Advanced News Dashboard")

# API details
url = "https://newsapi.org/v2/top-headlines"
api_key = "a3f417b116fa4104b3c547e8ee9d32e1"

# Sidebar filters
st.sidebar.header("Filters")
country = st.sidebar.selectbox("Location", ["in", "us", "gb", "ca", "au"])
category = st.sidebar.selectbox("Topic", ["general", "business", "technology", "sports", "health", "science", "entertainment"])
num_articles = st.sidebar.slider("Number of articles", 1, 20, 5)
keyword = st.sidebar.text_input("Search keyword", "")

# Fetch news
params = {
    "country": country,
    "category": category,
    "pageSize": num_articles,
    "apiKey": api_key
}

if keyword:
    url = "https://newsapi.org/v2/everything"
    params["q"] = keyword
    params.pop("country")
    params.pop("category")

response = requests.get(url, params=params)
data = response.json()

if data["status"] == "ok":
    st.write(f"Showing {len(data['articles'])} articles")
    for article in data["articles"]:
        st.subheader(article["title"])
        if article["description"]:
            st.write(article["description"])
        if article["urlToImage"]:
            st.image(article["urlToImage"], width=400)
        st.write(f"[Read full article]({article['url']})")
        st.write(f"Source: {article['source']['name']}")
        st.divider()
else:
    st.error("Failed to fetch news. Check API key or try again.")
