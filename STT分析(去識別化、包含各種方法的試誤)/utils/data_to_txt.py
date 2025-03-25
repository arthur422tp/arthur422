"""
This is for data processing, change data to .txt
"""
import os
import pandas as pd

class Convert:
    """_summary
    """
    def __init__(self, excel_path, txt_path):
        self.excel_path = excel_path
        self.txt_path = txt_path

    def xlsx_to_txt(self, excel_path, txt_path, sheet_name=0, delimiter='\t'):
        """_summary_

        Args:
            excel_path (_type_): _description_
            txt_path (_type_): _description_
            sheet_name (int, optional): _description_. Defaults to 0.
            delimiter (str, optional): _description_. Defaults to '\t'.
        """
        output_dir = os.path.dirname(self.txt_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        df.to_csv(txt_path, sep=delimiter, index=False, header=True, encoding='UTF-8')

        print("done")

    def csv_to_txt(self, excel_path, txt_path, delimiter='\t'):
        """_summary_

        Args:
            excel_path (_type_): _description_
            txt_path (_type_): _description_
            sheet_name (int, optional): _description_. Defaults to 0.
            delimiter (str, optional): _description_. Defaults to '\t'.
        """
        output_dir = os.path.dirname(self.txt_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        df = pd.read_csv(excel_path)
        df.to_csv(txt_path, sep=delimiter, index=False, header=True, encoding='UTF-8')

        print("done")