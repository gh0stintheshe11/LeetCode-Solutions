import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # Separate start and end activities
    start_activities = activity[activity['activity_type'] == 'start']
    end_activities = activity[activity['activity_type'] == 'end']
    
    # Merge start and end activities on machine_id and process_id
    merged_activities = pd.merge(start_activities, end_activities, on=['machine_id', 'process_id'], suffixes=('_start', '_end'))
    
    # Calculate the processing time for each process
    merged_activities['processing_time'] = merged_activities['timestamp_end'] - merged_activities['timestamp_start']
    
    # Group by machine_id and calculate the average processing time
    result = merged_activities.groupby('machine_id')['processing_time'].mean().reset_index()
    
    # Round the average processing time to 3 decimal places
    result['processing_time'] = result['processing_time'].round(3)
    
    return result