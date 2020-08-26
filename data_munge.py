from jinja2 import Environment, FileSystemLoader
import json
import pandas as pd 
from pandas import ExcelWriter 
import os
from weasyprint import HTML


class GenerateOutputFiles:

    def parse_json(self):
        with open('bandit_report.json', 'r') as report:
            report_dict = json.load(report)
        # only return the metrics as of now...
        return report_dict['metrics']
    
    # Attain data from the text files generated from the security scan. 
    def get_data(self): 
        
        warnings = open('warnings.txt', 'r') 
        suggestions = open('suggestions.txt', 'r') 
        packages = open('packages.txt', 'r') 
        shells = open('shells.txt', 'r') 
    
        warn_data = warnings.readlines() 
        sugg_data = suggestions.readlines() 
        pack_data = packages.read() 
        shell_data = shells.readlines() 
    
        return warn_data, sugg_data, pack_data, shell_data 
    
    #  Munge data 
    def clean_data(self): 
    
        warn, sugg, pack, shell = self.get_data() 
    
        warn_clean = [] 
        for line in warn: 
            warn_clean.append(line.split('|')) 
    
        for i in range(len(warn_clean)): 
            warn_clean[i] = warn_clean[i][:2] 
    
        sugg_clean = []     
        for line in sugg: 
            sugg_clean.append(line.split('|')) 
    
        for i in range(len(sugg_clean)): 
            sugg_clean[i] = sugg_clean[i][:2] 
    
        pack_clean = [] 
        pack = pack.split('|') 
        pack_clean = pack 
        del pack_clean[0] 
    
        shell_clean = [] 
    
        for i in range(len(shell)): 
            shell_clean.append(shell[i].rstrip('\n'))   
    
        return warn_clean, sugg_clean, pack_clean, shell_clean 

    def generate_output_directory(self):
        cwd = os.getcwd()
        path = os.path.join(cwd,"outputs")
        if not os.path.exists(path):
            os.mkdir(path)
        os.chdir('outputs') 
    
    def generate_worksheet(self, out_type):
        error = []
        text = []
        for i in range(len(out_type)):
            error.append(out_type[i][0]) 
        for i in range(len(out_type)): 
            text.append(out_type[i][1]) 
        return error, text
    
    def output_to_excel(self): 
    
        warnings, suggestions, packages, shells = self.clean_data() 
        # Generate the output directory for the security reports
        self.generate_output_directory()
    
        # Generate worksheet for the warnings section
        warn_packages, warn_text = self.generate_worksheet(warnings)
        warn = pd.DataFrame() 
        warn['Packages'], warn['warnings'] = warn_packages, warn_text 

        writer = ExcelWriter('warnings.xlsx')     
        warn.to_excel(writer, 'report1', index = False) 
        workbook = writer.book 
        worksheet = writer.sheets['report1'] 
        worksheet.set_column('A:A', 15) 
        worksheet.set_column('B:B', 45) 
        writer.save() 
    
        # Generate worksheet for the suggestions section
        sugg_packages, sugg_text = self.generate_worksheet(suggestions)
        sugg = pd.DataFrame() 
        sugg['Packages'], sugg['suggestions'] = sugg_packages, sugg_text

        writer1 = ExcelWriter('suggestions.xlsx') 
        sugg.to_excel(writer1, 'report2', index = False) 
        workbook = writer1.book 
        worksheet = writer1.sheets['report2'] 
        worksheet.set_column('A:A', 25) 
        worksheet.set_column('B:B', 120) 
        writer1.save() 
    
        # Generate worksheet for the packages section
        pack_data = pd.DataFrame() 
        pack_data['Packages'] = packages 
        writer1 = ExcelWriter('packages.xlsx')  
        pack_data.to_excel(writer1, 'report3', index = False) 
        workbook = writer1.book 
        worksheet = writer1.sheets['report3'] 
        worksheet.set_column('A:A', 75) 
        writer1.save() 
        # Resituate the user in the repositories root directory
        os.chdir('..') 
  
  
if __name__ == '__main__': 
    
    # env = Environment(loader=FileSystemLoader('.'))
    # template = env.get_template("report_template.html")
    # template_vars = {"title" : "Static File Analysis - Report",
    #              "bandit_report": bandit_report.to_html()}
    # html_out = template.render(template_vars)
  
    outputs = GenerateOutputFiles()

    warnings, suggestions, packages, shells = outputs.clean_data()
    outputs.output_to_excel() 
    # parse_json()