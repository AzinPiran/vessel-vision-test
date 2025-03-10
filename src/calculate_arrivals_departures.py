import pandas as pd

port_result_df = None
car_df = None
pas_df = None


# calculate departures and arrivals
def calculate_arrivals_departures(df):
    """
    Computes vessel arrivals and departures for each port.
    Also assigns the corresponding national flag emoji to each port.
    Separates data for Cargo and Passenger vessel types.

    Returns:
    --------
    Three DataFrames:
        - port_result_df (All vessel types)
        - car_df (Only Cargo vessels)
        - pas_df (Only Passenger vessels)
    """

    # only calculate once and store result
    global port_result_df, car_df, pas_df

    if port_result_df is not None and car_df is not None and pas_df is not None:
        return port_result_df, car_df, pas_df 
    
    cargo_df = df[df["Vessel Type Name"] == "Cargo"]
    passenger_df = df[df["Vessel Type Name"] == "Passenger"]

    def compute_port_stats(filtered_df):
        # national flag
        port_flags = {
            "Port of Tacoma": "\U0001F1FA\U0001F1F8", #US
            "Port of Vancouver": "\U0001F1E8\U0001F1E6", #CA
            "Port of Long Beach": "\U0001F1FA\U0001F1F8",
            "Port of Los Angeles": "\U0001F1FA\U0001F1F8",
            "Port of San Francisco": "\U0001F1FA\U0001F1F8",
            "Port of Oakland": "\U0001F1FA\U0001F1F8",
            "Port of Seattle": "\U0001F1FA\U0001F1F8",
            "Port of Ensenada": "\U0001F1F2\U0001F1FD", #MX
            "Port of San Diego": "\U0001F1FA\U0001F1F8",
        }

        # sort by MMSI and BaseDateTime
        filtered_df = filtered_df.sort_values(by=["MMSI", "BaseDateTime"])
        port_stats = {}
        prev_port = None
        prev_mmsi = None

        for _, row in filtered_df.iterrows():
            current_port = row["Nearest Port"]
            mmsi = row["MMSI"]

            if mmsi != prev_mmsi:
                prev_mmsi = mmsi
                prev_port = current_port
                continue

            if current_port != prev_port:
                # departure from old port +1
                if prev_port in port_stats:
                    port_stats[prev_port]["departures"] += 1
                else:
                    port_stats[prev_port] = {"arrivals": 0, "departures": 1}

                # arrival in new port +1
                if current_port in port_stats:
                    port_stats[current_port]["arrivals"] += 1
                else:
                    port_stats[current_port] = {"arrivals": 1, "departures": 0}

            prev_port = current_port

        if not port_stats:
            return pd.DataFrame(columns=["FLAG", "PORT NAME", "ARRIVALS", "DEPARTURES"])
        
        result_df = pd.DataFrame([
            {
                "FLAG": port_flags.get(port, "\U0001F3F3"), 
                "PORT NAME": port,
                "ARRIVALS": stats["arrivals"],
                "DEPARTURES": stats["departures"],
            }
            for port, stats in port_stats.items()
        ])

        return result_df.sort_values(by="ARRIVALS", ascending=False)

    port_result_df = compute_port_stats(df)
    car_df = compute_port_stats(cargo_df)
    pas_df = compute_port_stats(passenger_df)

    return port_result_df, car_df, pas_df
