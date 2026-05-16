import pandas as pd

def read_excel_file_to_list(file_path):
    try:
        # Read Excel file into a pandas DataFrame
        data = pd.read_excel(file_path)
        # Convert DataFrame to a list of lists
        data_list = data.values.tolist()
        return data_list
    except Exception as e:
        print("An error occurred:", e)
        return None
    
print("Please Provide Device")
device_data = input(": ")
if __name__ == "__main__":
    # Provide the path to your Excel file
    excel_file_path = "Device_ip.xlsx"  
    excel_data_list = read_excel_file_to_list(excel_file_path)
    if excel_data_list is not None:
        for device in excel_data_list:
            if device_data in device:
                print(device[1])
                print(device[2])
            else:
                pass