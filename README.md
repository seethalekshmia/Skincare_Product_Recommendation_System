# Skincare Product Recommendation System

A personalized skincare product recommendation system that suggests products based on skin type, concerns, and budget.

## Features

- Personalized product recommendations based on:
  - Skin type (oily, dry, combination, sensitive, normal)
  - Skin concerns (acne, aging, dryness, etc.)
  - Budget range
- Ingredient analysis and benefits explanation
- Direct purchase links
- User-friendly interface built with Streamlit

## Installation

1. Create a virtual environment:
```bash
python3 -m venv skincare_env
```

2. Activate the virtual environment:
```bash
source skincare_env/bin/activate  # On Linux/Mac
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Activate the virtual environment (if not already activated)
2. Run the Streamlit app:
```bash

streamlit run app.py
```

3. Open your web browser and go to the URL shown in the terminal (typically http://localhost:8501)

## How It Works

The system uses natural language processing and machine learning techniques to match your preferences with product ingredients and characteristics:

1. **Data Processing**: Products are analyzed based on their ingredients using TF-IDF vectorization
2. **Similarity Matching**: Cosine similarity is used to match your preferences with product characteristics
3. **Ingredient Analysis**: Key ingredients are identified and their benefits are explained
4. **Price Filtering**: Products are filtered based on your budget range

## Dataset

The system uses a curated dataset of skincare products with the following information:
- Product name and type
- Ingredients list
- Price
- Purchase URL
