#!/usr/bin/env python3
# A simple script to generate a word cloud from the 'NAME' column of a CSV.

import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# NLTK Stopwords import (make sure you've downloaded them via nltk.download('stopwords'))
from nltk.corpus import stopwords

# ------------------------------------------------------------------------------
# Define file paths (adjust as needed)
# ------------------------------------------------------------------------------
data_file_path = 'product-stats.csv'     # Path to your CSV with a 'NAME' column
output_image_path = 'WORD-CLOUD.jpg'     # Path/filename for the output image

# ------------------------------------------------------------------------------
# Function: generate_word_cloud_text
# ------------------------------------------------------------------------------
def generate_word_cloud_text(df):
    """
    Convert the 'NAME' column of the provided dataframe into a cleaned,
    lowercase string of words (minus stopwords and special characters).
    """
    try:
        # Check if the 'NAME' column exists
        if 'NAME' not in df.columns:
            print("The 'NAME' column is missing from the product data.")
            return ''

        # Extract product names as strings
        product_titles = df['NAME'].astype(str)

        # Combine all product names into one string
        text = ' '.join(product_titles)

        # Convert to lowercase
        text = text.lower()

        # Remove non-alphabetic characters (anything except a-z and whitespace)
        text = re.sub(r'[^a-z\s]', '', text)

        # Prepare a set of English stopwords
        stop_words = set(stopwords.words('english'))

        # Add custom words that you want excluded from the word cloud
        custom_stopwords = {
            'worksheet', 'worksheets', 'lesson', 'lessons',
            'activities', 'activity', 'grade', 'grades'
        }
        stop_words.update(custom_stopwords)

        # Split the text into tokens
        text_tokens = text.split()

        # Filter out any tokens that are in the stopwords set
        text_tokens_filtered = [word for word in text_tokens if word not in stop_words]

        # Rejoin the filtered tokens back into a single string
        filtered_text = ' '.join(text_tokens_filtered)
        return filtered_text

    except Exception as e:
        print(f"Error generating text for word cloud: {e}")
        return ''

# ------------------------------------------------------------------------------
# Function: save_product_name_word_cloud
# ------------------------------------------------------------------------------
def save_product_name_word_cloud(df):
    """
    Generate a word cloud from the 'NAME' column of the dataframe,
    and save it as a JPG file.
    """
    try:
        # Generate the cleaned text from the dataframe
        text = generate_word_cloud_text(df)

        # If there's no text, skip creating the word cloud
        if not text:
            print("No text available for word cloud; skipping word cloud generation.")
            return None

        # Create the WordCloud object
        wordcloud = WordCloud(
            width=800,
            height=600,
            background_color='black',
            colormap='Greens',
            stopwords=None,  # We manually handled stopwords in the generate_word_cloud_text() function
            max_words=200,
            max_font_size=100,
            random_state=42
        ).generate(text)

        # Set up the figure for plotting
        plt.figure(figsize=(11, 8.5), facecolor='k')
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')         # Hide the axis
        plt.tight_layout(pad=0) # Remove extra padding around the image

        # Optional: Add descriptive text under the word cloud
        plt.figtext(
            0.5, 0.02,
            'This word cloud highlights the top keywords from product names.',
            ha='center', va='center', fontsize=12, color='white'
        )

        # Save the figure as a JPG image
        plt.savefig(
            output_image_path,
            format='jpg',
            dpi=300,
            bbox_inches='tight',
            facecolor='k'  # Keep a black background
        )
        plt.close()

        print(f"Word Cloud saved as: {output_image_path}")
        return output_image_path

    except Exception as e:
        print(f"Error generating Word Cloud: {e}")
        return None

# ------------------------------------------------------------------------------
# Main: Execution starts here
# ------------------------------------------------------------------------------
def main():
    """
    1. Read the CSV file containing product data.
    2. Generate and save the word cloud image as a JPG file.
    """
    try:
        # Read data from CSV into a pandas DataFrame
        df = pd.read_csv(data_file_path)

        # Call our function to generate and save the word cloud
        image_path = save_product_name_word_cloud(df)

        # If needed, you can do other things after generating the image
        if image_path:
            print("Word Cloud generation complete.")
        else:
            print("Word Cloud was not generated.")
    except FileNotFoundError:
        print(f"The data file '{data_file_path}' was not found. Please check the path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# ------------------------------------------------------------------------------
# Name check for script execution
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
