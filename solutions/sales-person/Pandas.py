import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Get the company ID for the company named "RED"
    red_company = company[company['name'] == 'RED']['com_id']
    
    # Step 2: Find the sales_ids of salespersons who have made orders for the company "RED"
    sales_to_red = orders[orders['com_id'].isin(red_company)]['sales_id'].unique()
    
    # Step 3: Find salespersons who did not sell to the company "RED"
    no_red_sales = sales_person[~sales_person['sales_id'].isin(sales_to_red)]
    
    # Step 4: Return only the names of these salespersons
    return no_red_sales[['name']]