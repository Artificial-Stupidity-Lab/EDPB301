def add_data():
    # Dictionary that we want to add as a new row
    clock = time.time()
    data = {'Flight Time': drone.get_flight_time(),
            'Real time': f"{clock}",
            'Picture File Path': f"C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/{clock}.jpg"
            }
    
    df = pd.DataFrame(data)
    # append data frame to CSV file
    df.to_csv('"C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/droneData.csv"', mode='a', index=False, header=False)
    
    # print message
    print("Data appended successfully.")