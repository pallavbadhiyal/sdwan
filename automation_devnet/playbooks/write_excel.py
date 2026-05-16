import xlsxwriter
import sys
import json

# Load the interface data passed from Ansible
data = json.loads(sys.argv[1])

# Create a new Excel workbook and worksheet
workbook = xlsxwriter.Workbook('/tmp/interface_descriptions.xlsx')
worksheet = workbook.add_worksheet()

# Define headers
headers = ['Device', 'Interface', 'Description']

# Write the headers to the worksheet
worksheet.write_row(0, 0, headers)

# Write the data
row = 1
for entry in data:
    worksheet.write_row(row, 0, [entry['Device'], entry['Interface'], entry['Description']])
    row += 1

# Close the workbook
workbook.close()
