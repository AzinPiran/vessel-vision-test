import os
import pandas as pd
import numpy as np

def load_data(date_filter=None):
    # Define the root directory and the split-file folder path
    root_dir = os.path.dirname(os.path.abspath(__file__))  # This gets the absolute path of the current file (app.py is in src)
    split_file_dir = os.path.join(root_dir, '..', 'data', 'split-data')  # Navigate to data/split-file folder

    # List all CSV files in the split-file folder
    csv_files = [f for f in os.listdir(split_file_dir) if f.endswith('.csv')]

    # Read all CSV files and combine them into one DataFrame
    combined_df = pd.concat(
        [pd.read_csv(os.path.join(split_file_dir, csv_file)) for csv_file in csv_files],
        ignore_index=True
    )

    # ----------- preprocessing for maximum time anchored computation ----------------
    # Ensure the 'BaseDateTime' column is in datetime format after combining all files
    combined_df['BaseDateTime'] = pd.to_datetime(combined_df['BaseDateTime'], errors='coerce')  # Coerce invalid parsing to NaT

    # Filter data by specific date if the date_filter is provided
    if date_filter:
        combined_df = combined_df[combined_df['BaseDateTime'].dt.date == pd.to_datetime(date_filter).date()]

    # Sort the dataframe by MMSI and BaseDateTime
    combined_df = combined_df.sort_values(by=['MMSI', 'BaseDateTime']).reset_index(drop=True)

    # Calculate the 'Duration Anchored' for each vessel (SOG == 0 means anchored)
    combined_df['Duration Anchored'] = np.nan  # Initialize an empty column for duration

    # Loop through each unique vessel
    for mmsi in combined_df['MMSI'].unique():
        vessel_data = combined_df[combined_df['MMSI'] == mmsi]

        # Find rows where the vessel is anchored (SOG == 0)
        anchored_data = vessel_data[vessel_data['SOG'] == 0]

        # Calculate the time difference between consecutive anchored rows
        anchored_data['Duration Anchored'] = anchored_data['BaseDateTime'].diff().shift(-1)

        # Store this back into the original dataframe
        combined_df.loc[anchored_data.index, 'Duration Anchored'] = anchored_data['Duration Anchored']

    # Return combined dataframe
    return combined_df


load_data()