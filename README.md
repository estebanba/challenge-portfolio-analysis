# Portfolio Analysis

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://challenge-portfolio-analysis.streamlit.app/)

## Overview

This repository contains a comprehensive portfolio analysis project developed during the Data Analytics Bootcamp. The project demonstrates various financial analysis techniques using Python, focusing on portfolio management, return calculations, and risk assessment.

## Features

The analysis includes several key components:

1. **Data Loading and Price Charting**
   - Loading and cleaning financial asset price data
   - Time series visualization of asset prices
   - Trend analysis with normalized price series

2. **Daily Returns Analysis**
   - Calculation of daily percentage returns
   - Correlation matrix analysis
   - Asset return comparisons through scatter plots

3. **Portfolio Analysis**
   - Portfolio weight visualization
   - Historical cumulative returns tracking
   - Annualized return calculations
   - Portfolio volatility analysis
   - Asset category-based weight distribution

## Project Structure

```
challenge-portfolio-analysis/
│
├── components/
│   ├── __pycache__/
│   └── footer.py
│
├── data/
│   ├── clean/
│   │   ├── asset_price_data.csv
│   │   └── data.csv
│   └── raw/
│       ├── asset_information_data.csv
│       ├── asset_price_data.csv
│       └── portfolio_weights.csv
│
├── notebooks/
│   └── analysis_portfolio.ipynb
│
├── streamlit/
│   ├── config.toml
│   └── streamlit_app.py
│
├── .gitattributes
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

## Technologies Used

- Python 3.x
- Pandas for data manipulation
- NumPy for numerical computations
- Plotly Express for interactive visualizations
- Streamlit for web application deployment

## Installation

1. Clone the repository:
```bash
git clone https://github.com/estebanba/challenge-portfolio-analysis.git
cd challenge-portfolio-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Jupyter Notebook
To explore the analysis:
1. Navigate to the notebooks directory
2. Open `analysis_portfolio.ipynb`
3. Run the cells sequentially to see the analysis process

### Streamlit App
To run the web application locally:
```bash
streamlit run streamlit/streamlit_app.py
```

Or visit the live application at: [https://challenge-portfolio-analysis.streamlit.app/](https://challenge-portfolio-analysis.streamlit.app/)

## Data Files

The project uses three main data files:

- `asset_price_data.csv`: Contains historical price data for different assets
- `portfolio_weights.csv`: Includes daily portfolio weights for each asset
- `asset_information_data.csv`: Contains asset categorization information

## Live Demo

Access the live Streamlit application [here](https://challenge-portfolio-analysis.streamlit.app/).

## License

This project is part of a Data Analytics Bootcamp exercise and is available for educational purposes.

## Contributing

While this is primarily an educational exercise, suggestions and improvements are welcome:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request