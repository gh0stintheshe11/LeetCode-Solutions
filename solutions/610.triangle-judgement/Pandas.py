import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    # Define a function to check if three sides can form a triangle
    def can_form_triangle(row):
        x, y, z = row['x'], row['y'], row['z']
        if x + y > z and x + z > y and y + z > x:
            return 'Yes'
        else:
            return 'No'
    
    # Apply the function to each row in the DataFrame
    triangle['triangle'] = triangle.apply(can_form_triangle, axis=1)
    
    return triangle
