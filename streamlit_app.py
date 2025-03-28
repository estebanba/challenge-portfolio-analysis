import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go

from components.footer import footer

@st.cache_data

def load_data(path):
    df = pd.read_csv(path)
    return df


st.set_page_config(page_title="Tech-Challenge: Portfolio Analysis")

st.markdown(
    """
    <style>
        .stTabs [data-baseweb="tab-list"] {
            justify-content: left;
        }
        .stMarkdown, .stPlotlyChart, .stDataFrame {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

df_asset_price = load_data("./data/clean/asset_price_data.csv")

assets_list = list(df_asset_price.drop(columns=["date"]))

df_portfolio_weights = load_data("./data/raw/portfolio_weights.csv")

# -----------------------------------------------

st.title("Portfolio Analysis")

sections = ["Data Loading and Price Charting", "Daily Percentage Returns", "Portfolio Analysis", "Readme"]

tab1, tab2, tab3, tab4 = st.tabs(sections)

with tab1:
    st.header(f"Exercise 1: {sections[0]}")
    st.dataframe(df_asset_price, use_container_width=True)
   
    df_unpivot = pd.melt(
    df_asset_price, 
    id_vars=['date'], 
    value_vars = assets_list,
    var_name = 'Asset',
    value_name = 'Price'
    )

    fig = px.line(
    df_unpivot, 
    x='date', 
    y='Price', 
    color='Asset',
    title='Price Evolution of assets Over Time',
    labels={
        'date': 'Date',
        'Price': 'Price',
        'Asset': 'Asset'
        }
    )

    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Price',
        legend_title='Assets'
    )

    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header(f"Exercise 2: {sections[1]}")

    returns_df = pd.DataFrame({'date': df_asset_price['date'][1:]})

    for asset in assets_list:
        returns_df[f'{asset}_return'] = df_asset_price[asset].pct_change() * 100

    st.dataframe(returns_df, use_container_width=True)
    
    
    returns_df_unpivot = pd.melt(
    returns_df, 
    id_vars=['date'],
    value_vars=[f'{asset}_return' for asset in assets_list],
    var_name='Asset',
    value_name='Return (%)'
    )

    returns_df_unpivot['Asset'] = returns_df_unpivot['Asset'].str.replace('_return', '')

    fig = px.line(
        returns_df_unpivot,
        x='date',
        y='Return (%)',
        color='Asset',
        title='Daily Percentage Returns by Asset'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Summary Statistics for Daily Returns")

    summary_stats = returns_df[[f'{asset}_return' for asset in assets_list]].describe()
   
    st.dataframe(summary_stats, use_container_width=True)
   
    st.subheader("Correlation Matrix of Daily Returns")
    corr_matrix = returns_df[[f'{asset}_return' for asset in assets_list]].corr()

    fig = px.imshow(
    corr_matrix.apply(lambda x: round(x, 2)),
    text_auto=True,
    color_continuous_scale='RdBu_r',
    zmin=-1,
    zmax=1,
    title='Correlation Matrix of Daily Returns'
    )

    fig.update_layout(
        width=600,
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Correlation Matrix Calculation")

    corr_matrix = df_asset_price.drop('date', axis=1).corr()

    fig = px.imshow(
        corr_matrix.apply(lambda x: round(x, 2)),
        text_auto=True, 
        color_continuous_scale='RdBu_r',  
        zmin=-1,  
        zmax=1, 
        title='Asset Price Correlation Matrix'
    )

    fig.update_layout(
        width=600,
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Scatter Plot between the Returns of Two Assets")

    asset_x = st.selectbox(
    "Select the first Asset",
    assets_list,
    index=0,
    placeholder="Click here to see the assets...",
    )

    asset_y = st.selectbox(
    "Select the second Asset",
    assets_list,
    index=1,
    placeholder="Click here to see the assets...",
    )

    fig = px.scatter(
        returns_df,
        x=f'{asset_x}_return',
        y=f'{asset_y}_return',
        title=f'Scatter Plot of Daily Returns: {asset_x} vs {asset_y}',
        labels={
            f'{asset_x}_return': f'{asset_x} Daily Return (%)',
            f'{asset_y}_return': f'{asset_y} Daily Return (%)'
        },

    )

    fig.update_layout(
        width=700,
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header(f"Exercise 3: {sections[2]}")

    st.subheader("Portfolio Weights")
    st.dataframe(df_portfolio_weights, use_container_width=True)

    fig = px.area(
    df_portfolio_weights, 
    x='date',
    y=assets_list,
    title='Asset Weights Over Time',
    labels={'value': 'Allocation', 'variable': 'Asset'},
    )

    fig.update_layout(
        yaxis_tickformat='.0%',
        height=500,
        width=800
    )

    st.plotly_chart(fig, use_container_width=True)

    # ----------

    returns = df_asset_price.select_dtypes(include=[float]).pct_change()

    cumulative_returns = (1 + returns).cumprod() - 1

    fig = px.line(
        cumulative_returns,
        x=df_asset_price['date'],
        y=cumulative_returns.columns,
        title='Cumulative Returns by Asset',
        labels={'value': 'Cumulative Return', 'variable': 'Asset'}
    )

    fig.update_layout(
        yaxis_tickformat='.1%',
        height=500,
        width=800,
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)

    # -------

    # Calculate weighted portfolio returns
    weights = df_portfolio_weights.set_index('date').iloc[0]  # Use first row as weights
    portfolio_returns = (returns * weights).sum(axis=1)

    # Calculate cumulative returns
    cumulative_returns = (1 + portfolio_returns).cumprod() - 1
    plot_df = pd.DataFrame({
    'date': cumulative_returns.index,
    'Cumulative Return': cumulative_returns
    })

    fig = px.line(
        plot_df, 
        x='date', 
        y='Cumulative Return',
        title='Portfolio Cumulative Returns'
    )

    fig.update_layout(
        yaxis_tickformat='.1%',
        height=500,
        width=800
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------

    # Calculate weights by family
    weights_by_family = df_portfolio_weights.set_index('date').copy()
    weights_by_family['Fixed Income'] = weights_by_family['Asset1'] + weights_by_family['Asset2']
    weights_by_family['Equity'] = weights_by_family['Asset3'] + weights_by_family['Asset4']
    weights_by_family['Alternative'] = weights_by_family['Asset5']

    # Keep only family columns
    family_weights = weights_by_family[['Fixed Income', 'Equity', 'Alternative']]

    # Create the plot
    fig = px.area(
        family_weights,
        title='Portfolio Weights by Asset Family',
    )

    # Update layout
    fig.update_layout(
        height=500,
        width=800,
        yaxis_title='Weight',
        yaxis_tickformat='.0%',
        showlegend=True,
    )

    st.plotly_chart(fig, use_container_width=True)

# Call the footer function at the end
try:
    footer()
except Exception as e:
    st.write("Note: Custom footer could not be loaded.")
    st.error(f"Footer error: {e}")
    # Fallback footer
    st.markdown(
        """
        <div style="position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px; background-color: #f8f9fa;">
            Portfolio Analysis Dashboard | Created using Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )
with tab4:
   # Custom CSS to ensure left alignment
    st.markdown("""
    <style>
    .stMarkdown {
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

    # Read and display markdown file from the root folder
    with open("README.md", "r") as file:
        content = file.read()
        st.markdown(content)