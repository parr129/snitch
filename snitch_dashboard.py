# snitch_dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.express as px

# Streamlit page config
st.set_page_config(page_title="Customer Review Insights", layout="wide")
st.title("🧠 Customer Review Insights Dashboard")

st.markdown("""
Welcome to the smart feedback explorer! Upload your customer reviews in CSV format with the following columns:
- `Rating` (float)
- `NLP_Tag` (text)
- `Category` (text)
- `Return_Reason` (text)
""")

# File upload
uploaded_file = st.sidebar.file_uploader("📁 Upload Review Data", type=["csv"])

# Process uploaded file
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Cleanup
    df.dropna(subset=['Rating'], inplace=True)
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    df = df[df['Rating'].notnull()]

    st.success("✅ Review data loaded successfully!")

    # Sidebar filters
    st.sidebar.header("📊 Filter Options")
    category_filter = st.sidebar.multiselect("Filter by Category", options=df['Category'].dropna().unique(), default=df['Category'].dropna().unique())
    rating_range = st.sidebar.slider("Filter by Rating", min_value=0.0, max_value=5.0, value=(1.0, 5.0), step=0.1)

    # Apply filters
    filtered_df = df[
        df['Category'].isin(category_filter) &
        df['Rating'].between(rating_range[0], rating_range[1])
    ]

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Overview", "📋 Category Insights", "🔍 NLP Analysis", "🚚 Return Insights"])

    # --- Tab 1: Overview ---
    with tab1:
        st.header("📈 General Metrics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Avg. Rating", f"{filtered_df['Rating'].mean():.2f} / 5")
        with col2:
            st.metric("Total Reviews", len(filtered_df))
        with col3:
            st.metric("Unique Categories", filtered_df['Category'].nunique())
        with col4:
            top_return = filtered_df['Return_Reason'].mode().iloc[0] if 'Return_Reason' in filtered_df.columns and not filtered_df['Return_Reason'].isna().all() else "N/A"
            st.metric("Top Return Reason", top_return)

        st.subheader("🟡 Rating Distribution")
        fig = px.histogram(filtered_df, x='Rating', nbins=20, title="Ratings Histogram", color_discrete_sequence=["#0077b6"])
        st.plotly_chart(fig, use_container_width=True)

    # --- Tab 2: Category Insights ---
    with tab2:
        st.header("📋 Ratings & Returns by Category")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("⭐ Average Rating by Category")
            cat_rating = filtered_df.groupby('Category')['Rating'].mean().reset_index()
            fig1 = px.bar(cat_rating, x='Rating', y='Category', orientation='h', color='Rating', color_continuous_scale='Blues')
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            st.subheader("📦 Return Reasons by Category")
            if 'Return_Reason' in filtered_df.columns:
                heat_data = pd.crosstab(filtered_df['Category'], filtered_df['Return_Reason'])
                fig2, ax2 = plt.subplots(figsize=(10, 6))
                sns.heatmap(heat_data, annot=True, fmt='d', cmap="YlOrBr")
                st.pyplot(fig2)

    # --- Tab 3: NLP Tags ---
    with tab3:
        st.header("🔍 NLP Tag Analysis")
        st.subheader("Top NLP Tags")

        top_tags = filtered_df['NLP_Tag'].value_counts().head(15).reset_index()
        top_tags.columns = ['Tag', 'Count']
        fig3 = px.bar(top_tags, x='Count', y='Tag', orientation='h', color='Count', color_continuous_scale='teal')
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("🧠 Word Cloud of NLP Tags")
        tag_text = " ".join(filtered_df['NLP_Tag'].dropna().astype(str).tolist())
        if tag_text:
            wc = WordCloud(width=800, height=400, background_color='white').generate(tag_text)
            fig4, ax4 = plt.subplots()
            ax4.imshow(wc, interpolation='bilinear')
            ax4.axis('off')
            st.pyplot(fig4)

    # --- Tab 4: Return Reasons ---
    with tab4:
        st.header("🚚 Return Reasons")
        if 'Return_Reason' in filtered_df.columns:
            return_counts = filtered_df['Return_Reason'].value_counts().reset_index()
            return_counts.columns = ['Reason', 'Count']
            fig5 = px.pie(return_counts, names='Reason', values='Count', title="Return Reason Distribution", color_discrete_sequence=px.colors.sequential.Oranges)
            st.plotly_chart(fig5, use_container_width=True)

            st.subheader("Rating by Return Reason")
            box_data = filtered_df[['Rating', 'Return_Reason']].dropna()
            fig6 = px.box(box_data, x='Return_Reason', y='Rating', color='Return_Reason', title="Rating Spread for Each Return Reason")
            st.plotly_chart(fig6, use_container_width=True)

else:
    st.info("📤 Please upload a CSV file with the columns: `Rating`, `NLP_Tag`, `Category`, `Return_Reason`.")
