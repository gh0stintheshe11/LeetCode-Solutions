import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    # Create the Sales DataFrame
    sales_df = sales

    # Step 1: Find the first year for each product
    sales_df['first_year'] = sales_df.groupby('product_id')['year'].transform('min')

    # Step 2: Filter the rows where the year matches the first year
    first_year_sales_df = sales_df[sales_df['year'] == sales_df['first_year']]

    # Step 3: Select and rename the columns as required
    result_df = first_year_sales_df[['product_id', 'first_year', 'quantity', 'price']]

    # Display the result
    return result_df