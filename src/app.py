import streamlit as st
from data_processor import DataProcessor
import os

# Initialize the DataProcessor
data_processor = DataProcessor('skincare_products_clean.csv')

def main():
    st.title('🧴 Skincare Product Recommendation System')
    st.write('Find the perfect skincare products for your needs!')

    # User Input Section
    st.sidebar.header('Tell us about your skin')
    
    # Skin Type Selection
    skin_type = st.sidebar.selectbox(
        'What is your skin type?',
        ['Oily', 'Dry', 'Combination', 'Sensitive', 'Normal']
    )

    # Skin Concerns (Multiple Selection)
    concerns = st.sidebar.multiselect(
        'What are your skin concerns?',
        ['Acne', 'Aging', 'Dryness', 'Redness', 'Pigmentation', 'Large Pores', 'Dullness']
    )

    # Budget Range
    st.sidebar.header('Budget Range (in £)')
    col1, col2 = st.sidebar.columns(2)
    with col1:
        min_price = st.number_input('Min Price (£)', value=5)
        st.write(f'₹{min_price * 104:.0f}')
    with col2:
        max_price = st.number_input('Max Price (£)', value=50)
        st.write(f'₹{max_price * 104:.0f}')

    if st.sidebar.button('Get Recommendations'):
        if not concerns:
            st.warning('Please select at least one skin concern.')
            return

        # Get recommendations
        recommendations = data_processor.get_recommendations(
            skin_type.lower(),
            [concern.lower() for concern in concerns],
            (min_price, max_price)
        )

        if not recommendations:
            st.info('No products found within your criteria. Try adjusting your filters.')
            return

        # Display recommendations
        st.subheader('Recommended Products for You')
        
        for product in recommendations:
            with st.expander(f"🏷️ {product['product_name']} - £{product['price']:.2f} (₹{product['price_inr']:.2f})"):
                st.write(f"**Product Type:** {product['product_type']}")
                
                # Get and display key ingredients benefits
                benefits = data_processor.get_ingredient_benefits(product['clean_ingreds'])
                if benefits:
                    st.write("**Key Ingredients & Benefits:**")
                    for ingredient, benefit in benefits:
                        st.write(f"- {ingredient}: {benefit}")
                
                st.write(f"**Price:** £{product['price']:.2f} (₹{product['price_inr']:.2f})")
                st.write(f"**Purchase Link:** [Buy Now]({product['product_url']})")

if __name__ == '__main__':
    main()
