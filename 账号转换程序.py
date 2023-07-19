import re
import xlwt
import tkinter as tk
from tkinter import filedialog

def extract_fields(file_path):
    pattern = r'出的账号(\d+).*买家手机号(\d+)'
    extracted_data = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                account = match.group(1)
                phone_number = match.group(2)
                extracted_data.append({'账号': account, '手机号': phone_number})
    
    return extracted_data

def save_to_excel(data, excel_file_path):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('数据')
    
    row = 0
    sheet.write(row, 0, '账号')
    sheet.write(row, 1, '手机号')
    
    for item in data:
        row += 1
        sheet.write(row, 0, item['账号'])
        sheet.write(row, 1, item['手机号'])
    
    workbook.save(excel_file_path)

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        output_file_path = filedialog.asksaveasfilename(defaultextension='.xls')
        if output_file_path:
            extracted_data = extract_fields(file_path)
            save_to_excel(extracted_data, output_file_path)
            result_label.config(text=f'处理完成！输出文件: {output_file_path}')
        else:
            result_label.config(text='请选择输出文件的位置！')
    else:
        result_label.config(text='请选择一个txt文件！')

# 创建窗口
window = tk.Tk()
window.title('依旧网游账号处理工具')
window.geometry('400x400')  # 设置窗口大小为200*400

# 创建按钮和标签
browse_button = tk.Button(window, text='选择文件', command=browse_file)
browse_button.pack(pady=20)

result_label = tk.Label(window, text='')
result_label.pack()

# 启动窗口循环
window.mainloop()
