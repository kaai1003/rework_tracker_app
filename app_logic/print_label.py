#!/usr/bin/python
"""print label Module"""
import win32print
import win32ui

def generate_label(id, label, printer, data):
    """generate label"""
    template_path = 'data/label/{}_template.txt'.format(label)
    try:
        # Read the template
        with open(template_path, 'r') as template_file:
            label_content = template_file.read()

        # Replace variables in the template
        if data:
            label_content = label_content.format(**data)
            output_label = 'data/label/{}_{}.txt'.format(label, id)
            # Save the modified label to a new file
            with open(output_label, 'w') as output_file:
                output_file.write(label_content)
            
            print(f"Label generated and saved to {output_label}")
            try:
                # Get the printer handle
                printer_handle = win32print.OpenPrinter(printer)
                
                # Open a print job
                job = win32print.StartDocPrinter(printer_handle, 1, ("Print Job", None, "RAW"))
                win32print.StartPagePrinter(printer_handle)

                
                # Send the content to the printer
                win32print.WritePrinter(printer_handle, label_content.encode('utf-8'))
                win32print.EndPagePrinter(printer_handle)
                win32print.EndDocPrinter(printer_handle)
                win32print.ClosePrinter(printer_handle)
                
                print("File sent to the printer successfully.")
            except Exception as e:
                print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
