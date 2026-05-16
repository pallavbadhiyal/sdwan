from ansible.errors import AnsibleFilterError
import openpyxl
import os

class FilterModule(object):
    def filters(self):
        return {
            'convert_interfaces_to_excel': self.convert_interfaces_to_excel,
        }

    @staticmethod
    def convert_interfaces_to_excel(parsed_interfaces, output_file='./interfaces.xlsx', sheet_name='Interfaces'):
        # if not isinstance(parsed_interfaces, dict) or 'interface' not in parsed_interfaces:
        #     raise AnsibleFilterError("Input must be a dictionary with an 'interface' key.")

        # interfaces = parsed_interfaces['interface']
        headers = ['Device','Interface', 'Is OK', 'IP Address', 'Method', 'Protocol', 'Status']
        data = [headers]
        for device, output in parsed_interfaces.items():

            for iface, details in output["interface"].items():
                row = [
                    device,
                    iface,
                    details.get('interface_is_ok', 'N/A'),
                    details.get('ip_address', 'N/A'),
                    details.get('method', 'N/A'),
                    details.get('protocol', 'N/A'),
                    details.get('status', 'N/A')
                ]
                data.append(row)

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = sheet_name

        for row in data:
            ws.append(row)

        try:
            wb.save(output_file)
            return f"Excel file saved at {output_file}"
        except PermissionError:
            raise AnsibleFilterError(f"Permission denied when saving the file: {output_file}")