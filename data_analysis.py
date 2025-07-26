import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_data(file_path):
    """Performs data analysis and generates insights from the preprocessed dataset."""
    try:
        df = pd.read_csv(file_path)
        print(f"Analyzing dataset with {len(df)} rows and {len(df.columns)} columns.")

        print("\n" + "="*50)
        print("SUMMARY STATISTICS")
        print("="*50)
        print(df.describe())

        print("\n" + "="*50)
        print("TOP TYRE BRANDS")
        print("="*50)
        tyre_brand_counts = df["Tyre Brand"].value_counts().head(10)
        print(tyre_brand_counts)

        print("\n" + "="*50)
        print("PRICE ANALYSIS")
        print("="*50)
        print(f"Average Selling Price: {df['Selling Price'].mean():.2f}")
        print(f"Average Original Price: {df['Original Price'].mean():.2f}")
        print(f"Average Discount (Original - Selling): {(df['Original Price'] - df['Selling Price']).mean():.2f}")

        print("\n" + "="*50)
        print("RATING ANALYSIS")
        print("="*50)
        rating_counts = df["Rating"].value_counts(dropna=False).sort_index()
        print(rating_counts)
        print(f"Average Rating: {df['Rating'].mean():.2f}")

        print("\n" + "="*50)
        print("VISUALIZATIONS")
        print("="*50)

        # Set up plot style
        sns.set_style("whitegrid")
        plt.figure(figsize=(18, 12))

        # 1. Distribution of Selling Price
        plt.subplot(2, 3, 1)
        sns.histplot(df["Selling Price"], bins=30, kde=True, color='skyblue')
        plt.title("Distribution of Selling Price")
        plt.xlabel("Selling Price")
        plt.ylabel("Frequency")

        # 2. Top 10 Tyre Brands
        plt.subplot(2, 3, 2)
        sns.barplot(x=tyre_brand_counts.values, y=tyre_brand_counts.index, palette='viridis')
        plt.title("Top 10 Tyre Brands")
        plt.xlabel("Number of Tyres")
        plt.ylabel("Tyre Brand")

        # 3. Distribution of Ratings
        plt.subplot(2, 3, 3)
        sns.histplot(df["Rating"].dropna(), bins=10, kde=True, color='lightcoral')
        plt.title("Distribution of Ratings")
        plt.xlabel("Rating")
        plt.ylabel("Frequency")

        # 4. Selling Price vs. Rating (Scatter Plot)
        plt.subplot(2, 3, 4)
        sns.scatterplot(x="Selling Price", y="Rating", data=df, alpha=0.6, color='purple')
        plt.title("Selling Price vs. Rating")
        plt.xlabel("Selling Price")
        plt.ylabel("Rating")

        # 5. Tyre Type Distribution
        plt.subplot(2, 3, 5)
        type_counts = df["Type"].value_counts()
        plt.pie(type_counts, labels=type_counts.index, autopct="%1.1f%%", startangle=90, colors=sns.color_palette('pastel'))
        plt.title("Tyre Type Distribution")
        plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.tight_layout()
        plt.savefig("Car_Tyres_Analysis_Visualizations.png")
        print("Visualizations saved as Car_Tyres_Analysis_Visualizations.png")

        return True

    except Exception as e:
        print(f"An error occurred during analysis: {e}")
        return False

if __name__ == "__main__":
    input_csv = "Car_Tyres_Dataset_Preprocessed.csv"
    if analyze_data(input_csv):
        print("\nData analysis successful.")
    else:
        print("Data analysis failed.")


