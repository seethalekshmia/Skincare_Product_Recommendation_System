import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

class DataProcessor:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df['clean_ingreds'] = self.df['clean_ingreds'].apply(ast.literal_eval)
        self.df['price'] = self.df['price'].str.replace('£', '').astype(float)
        self.df['price_inr'] = self.df['price'] * 104  # Converting to INR
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.ingredients_matrix = None
        self._process_ingredients()

    def _process_ingredients(self):
        # Convert ingredients lists to strings for TF-IDF
        ingredients_text = [' '.join(ingredients) for ingredients in self.df['clean_ingreds']]
        self.ingredients_matrix = self.vectorizer.fit_transform(ingredients_text)

    def get_recommendations(self, skin_type, concerns, budget_range):
        # Filter by budget
        min_price, max_price = budget_range
        filtered_df = self.df[(self.df['price'] >= min_price) & (self.df['price'] <= max_price)]

        if filtered_df.empty:
            return []

        # Create query based on skin type and concerns
        query_terms = [skin_type] + concerns
        query_vector = self.vectorizer.transform([' '.join(query_terms)])

        # Calculate similarity scores
        similarity_scores = cosine_similarity(query_vector, self.ingredients_matrix[filtered_df.index])
        
        # Get top recommendations
        top_indices = similarity_scores[0].argsort()[::-1][:5]
        recommendations = filtered_df.iloc[top_indices]

        return recommendations.to_dict('records')

    def get_ingredient_benefits(self, ingredients):
        benefits = {
            'hyaluronic acid': 'Hydration and moisture retention',
            'niacinamide': 'Reduces redness and regulates oil production',
            'salicylic acid': 'Treats acne and unclogs pores',
            'retinol': 'Anti-aging and cell turnover',
            'vitamin c': 'Brightening and antioxidant protection',
            'ceramides': 'Strengthens skin barrier',
            'glycerin': 'Hydration and moisture retention',
            'peptides': 'Anti-aging and skin firming',
            'aloe': 'Soothing and calming',
            'tea tree': 'Anti-bacterial and acne treatment'
        }
        
        found_benefits = []
        for ingredient in ingredients:
            for key, benefit in benefits.items():
                if key in ingredient.lower():
                    found_benefits.append((ingredient, benefit))
        return found_benefits
