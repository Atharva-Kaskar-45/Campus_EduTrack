import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
#from tkinter import ttk, filedialog, messagebox #specific submodules
from PIL import Image, ImageTk #python made image importation ((Python Imaging Library) )
import xlwings as xw #import xlwings 
import re #regular expressions sathi (string manipulation like that)
import customtkinter as cstk

global start_row_entry, end_row_entry, file_path_label, option_var, output_text

root = tk.Tk() #main window Tkinter(in short root window )

def fill_page1_and_page2(workbook, row_start, row_end):
    try:
        # Convert row start and row end to integers
        row_start = int(row_start)
        row_end = int(row_end)
        
        # Check if workbook is provided
        if not workbook:
            
            #error message if workbook is not provided
            messagebox.showerror("Error", "Please select the database file.")
            return
# changed to configure
        output_text.configure(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)  # Clear previous messages
        output_text.insert(tk.END, "PROCESSING FILES FOR PAGE 1 AND PAGE 2....\n\n")
        output_text.configure(state=tk.DISABLED)
        root.update()
        
        #excel launch karto
        app = xw.App(visible=False)
        
        #open current  book
        current_workbook = xw.Book(workbook)
        #acess detoy info cha 
        student_datasheet1 = current_workbook.sheets["Personal Info"]
        
        #open template 
        sheet_template_wb = xw.Book("template.xlsx")
        
        #page 1 nad 2 cha access
        template_page1 = sheet_template_wb.sheets["Page 1"]
        template_page2 = sheet_template_wb.sheets["Page 2"]

        for row in range(row_start, row_end + 1):
            new_template = xw.Book() #new workbook create karto
            
            
            #copy kaych chalu ahe page 1 and 2 made 
            template_page1.copy(after=new_template.sheets[0])
            template_page2.copy(after=new_template.sheets[1])
            new_template.sheets[0].delete()

            page1 = new_template.sheets["Page 1"]
            page2 = new_template.sheets["Page 2"]

            #data from the current row in the datasheet
            dstuple1 = tuple((
                student_datasheet1[f"F{row}"].value, student_datasheet1[f"B{row}"].value, student_datasheet1[f"C{row}"].value,
                student_datasheet1[f"D{row}"].value, student_datasheet1[f"E{row}"].value, student_datasheet1[f"A{row}"].value,
                student_datasheet1[f"G{row}"].value, student_datasheet1[f"H{row}"].value, student_datasheet1[f"I{row}"].value,
                student_datasheet1[f"J{row}"].value, student_datasheet1[f"K{row}"].value, student_datasheet1[f"L{row}"].value,
                student_datasheet1[f"M{row}"].value, student_datasheet1[f"N{row}"].value, student_datasheet1[f"O{row}"].value,
                student_datasheet1[f"P{row}"].value, student_datasheet1[f"Q{row}"].value, student_datasheet1[f"R{row}"].value,
                student_datasheet1[f"S{row}"].value, student_datasheet1[f"T{row}"].value, student_datasheet1[f"U{row}"].value,
                student_datasheet1[f"V{row}"].value, student_datasheet1[f"W{row}"].value, student_datasheet1[f"X{row}"].value,
                student_datasheet1[f"Y{row}"].value, student_datasheet1[f"Z{row}"].value, student_datasheet1[f"AA{row}"].value,
                student_datasheet1[f"AB{row}"].value, student_datasheet1[f"AC{row}"].value, student_datasheet1[f"AD{row}"].value,
                student_datasheet1[f"AE{row}"].value, student_datasheet1[f"AF{row}"].value, student_datasheet1[f"AG{row}"].value,
                student_datasheet1[f"AH{row}"].value))
            # Assign values to specific cells 
            (page1["H7"].value, page1["H5"].value, page1["H9"].value, page1["D9"].value, page1["C7"].value, page1["C5"].value,
             page1["B13"].value, page1["D14"].value, page1["D17"].value, page1["D20"].value, page1["F14"].value, page1["F17"].value,
             page1["F20"].value, page1["B23"].value, page1["D22"].value, page1["F22"].value, page1["H27"].value, page1["E28"].value,
             page1["D32"].value, page1["D33"].value, page1["E32"].value, page1["E33"].value, page1["C32"].value, page1["C33"].value,
             page1["H33"].value, page1["H32"].value, page1["D36"].value, page1["H36"].value, page2["A2"].value, page2["A5"].value,
             page2["F5"].value, page2["C17"].value, page2["C26"].value, page2["A34"].value) = dstuple1
             
             #prn name ne save kartoy 
            prn_file_name = dstuple1[0]
            prn_file_name = re.sub("[^a-zA-Z0-9 \n\\.]", ".", prn_file_name)
            
            #save kartoy  workbook
            new_template.save(f"output\\{str(prn_file_name)}.xlsx")
            new_template.close()
# changed config to configure
            output_text.configure(state=tk.NORMAL)
            output_text.insert(tk.END, f"CREATED PERSONAL INFORMATION PAGE 1 AND PAGE 2 OF {prn_file_name}\n","red")
            output_text.configure(state=tk.DISABLED)
            root.update()
# changed here            
            output_text.configure(fg_color="white", text_color="red")
        
        #excel band kartoy    
        app.quit()
        
        #sucess mesg 
        messagebox.showinfo("Success", "Processing completed successfully.")

    except Exception as e:
        # konta sepecific error dakvaych asel tar 
        messagebox.showerror("Error", f"An error occurred while filling Page 1 and Page 2: {str(e)}")
        
def sem1(workbook, row_start, row_end):
    try:
        ROW_START = int(row_start)
        ROW_END = int(row_end)
        
        #apn code run kadun drop down chnages kelayvar text box change karayla 
        output_text.configure(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)  # Clear previous messages
        output_text.insert(tk.END, "PROCESSING FILES FOR SEM 1....\n")
        output_text.configure(state=tk.DISABLED)
        root.update()
        
        #exel la launch kela (karn sem 1 run kelayvar sucessfull cha mesg dakvayla )
        app = xw.App(visible=False)

        #open
        CURRENT_WORKBOOK = xw.Book(workbook)
        #sem data cha acess 
        STUDENT_DATASHEET2 = CURRENT_WORKBOOK.sheets["Sem 1"]
        #template open 
        SHEET_TEMPLATE_wb = xw.Book(r"template.xlsx")
        #page 3 cha access deto 
        TemplatePage3 = SHEET_TEMPLATE_wb.sheets["Page 3"]

        #sub define kelet 
        sem1Subjects = (
            STUDENT_DATASHEET2["C1"].value,
            STUDENT_DATASHEET2["F1"].value,
            STUDENT_DATASHEET2["I1"].value,
            STUDENT_DATASHEET2["L1"].value,
            STUDENT_DATASHEET2["O1"].value,
        )

        for row in range(ROW_START, ROW_END + 1):
            
            #prn getoy data base madun 
            PRN_FILE_NAME = STUDENT_DATASHEET2[f"A{row}"].value
            #open template 
            NEW_TEMPLATE = xw.Book(f"output\\{str(PRN_FILE_NAME)}.xlsx")
            #copy kartoy new template made 
            TemplatePage3.copy(after=NEW_TEMPLATE.sheets[1])
            
            #acess detoy page 3 template cha output folder madun 
            Page3 = NEW_TEMPLATE.sheets["Page 3"]

            #data from the current row
            dstupleSem1 = (
                STUDENT_DATASHEET2[f"C{row}"].value,
                STUDENT_DATASHEET2[f"D{row}"].value,
                STUDENT_DATASHEET2[f"E{row}"].value,
                STUDENT_DATASHEET2[f"F{row}"].value,
                STUDENT_DATASHEET2[f"G{row}"].value,
                STUDENT_DATASHEET2[f"H{row}"].value,
                STUDENT_DATASHEET2[f"I{row}"].value,
                STUDENT_DATASHEET2[f"J{row}"].value,
                STUDENT_DATASHEET2[f"K{row}"].value,
                STUDENT_DATASHEET2[f"L{row}"].value,
                STUDENT_DATASHEET2[f"M{row}"].value,
                STUDENT_DATASHEET2[f"N{row}"].value,
                STUDENT_DATASHEET2[f"O{row}"].value,
                STUDENT_DATASHEET2[f"P{row}"].value,
                STUDENT_DATASHEET2[f"Q{row}"].value,
            )
           # Assign values pretket cell la 
            (Page3["C8"].value, Page3["D8"].value, Page3["F8"].value, Page3["C9"].value, Page3["D9"].value, Page3["F9"].value, 
            Page3["C10"].value, Page3["D10"].value, Page3["F10"].value, Page3["C11"].value, Page3["D11"].value, Page3["F11"].value, 
            Page3["C12"].value, Page3["D12"].value, Page3["F12"].value ) = dstupleSem1
            
            (Page3["B8"].value, Page3["B9"].value, Page3["B10"].value, Page3["B11"].value, Page3["B12"].value) = sem1Subjects

            NEW_TEMPLATE.save()
            NEW_TEMPLATE.close()
            
            #same logic above 
            output_text.configure(state=tk.NORMAL)
            output_text.insert(tk.END, f"FILLED SEM 1 MARKS OF {PRN_FILE_NAME}\n","red")
            output_text.configure(state=tk.DISABLED)
            root.update()
            output_text.configure(fg_color="white", text_color="red")
         
         #sucess full after complition    
        app.quit()
        messagebox.showinfo("Success", "Processing completed successfully.")

    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occurred while processing Semester 1: {str(e)}"
        )
 
#browsing function         
def browse_file():
    #open kartoy dialog box specific (file extension sobat)
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx;.xls")])
    
    # means jar apn file path select kela tar iffffff
    if file_path:
        
        #file_path_var (ya variable made store kartoy mi )
        file_path_var.set(file_path)


#bakicha functions         
def sem2(workbook, row_start, row_end):
    try:
        ROW_START = int(row_start)
        ROW_END = int(row_end)
        
        #apn code run kadun drop down chnages kelayvar text box change karayla 
        output_text.configure(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)  # Clear previous messages
        output_text.insert(tk.END, "PROCESSING FILES FOR SEM 2....\n")
        output_text.configure(state=tk.DISABLED)
        root.update()
        
        #exel la launch kela (karn sem 1 run kelayvar sucessfull cha mesg dakvayla )
        app = xw.App(visible=False)

        #open
        CURRENT_WORKBOOK = xw.Book(workbook)
        #sem data cha acess 
        STUDENT_DATASHEET3 = CURRENT_WORKBOOK.sheets["Sem 2"]

        #sub define kelet 
        sem2Subjects = tuple((STUDENT_DATASHEET3[f"C1"].value, STUDENT_DATASHEET3[f"F1"].value, STUDENT_DATASHEET3[f"I1"].value,
                             STUDENT_DATASHEET3[f"L1"].value, STUDENT_DATASHEET3[f"O1"].value))

        for row in range(ROW_START, ROW_END + 1):
            
            #prn getoy data base madun 
            PRN_FILE_NAME = STUDENT_DATASHEET3[f"A{row}"].value
            #open template 
            NEW_TEMPLATE = xw.Book(f"output\\{str(PRN_FILE_NAME)}.xlsx", ignore_read_only_recommended=True)
            
            #acess detoy page 3 template cha output folder madun 
            Page3 = NEW_TEMPLATE.sheets["Page 3"]

            #data from the current row
            dstupleSem2 = tuple((STUDENT_DATASHEET3[f"C{row}"].value, STUDENT_DATASHEET3[f"D{row}"].value, STUDENT_DATASHEET3[f"E{row}"].value, 
                             STUDENT_DATASHEET3[f"F{row}"].value, STUDENT_DATASHEET3[f"G{row}"].value, STUDENT_DATASHEET3[f"H{row}"].value, 
                             STUDENT_DATASHEET3[f"I{row}"].value, STUDENT_DATASHEET3[f"J{row}"].value, STUDENT_DATASHEET3[f"K{row}"].value, 
                             STUDENT_DATASHEET3[f"L{row}"].value, STUDENT_DATASHEET3[f"M{row}"].value, STUDENT_DATASHEET3[f"N{row}"].value, 
                             STUDENT_DATASHEET3[f"O{row}"].value, STUDENT_DATASHEET3[f"P{row}"].value, STUDENT_DATASHEET3[f"Q{row}"].value))
           # Assign values pretket cell la 
            (Page3["N8"].value, Page3["O8"].value, Page3["Q8"].value, Page3["N9"].value, Page3["O9"].value, Page3["Q9"].value, 
         Page3["N10"].value, Page3["O10"].value, Page3["Q10"].value, Page3["N11"].value, Page3["O11"].value, Page3["Q11"].value, 
         Page3["N12"].value, Page3["O12"].value, Page3["Q12"].value) = dstupleSem2
            
            (Page3["M8"].value, Page3["M9"].value, Page3["M10"].value, Page3["M11"].value, Page3["M12"].value) = sem2Subjects

            NEW_TEMPLATE.save()
            NEW_TEMPLATE.close()
            
            #same logic above 
            output_text.configure(state=tk.NORMAL)
            output_text.insert(tk.END, f"FILLED SEM 2 MARKS OF {PRN_FILE_NAME}\n","red")
            output_text.configure(state=tk.DISABLED)
            root.update()
            output_text.configure(fg_color="white", text_color="red")
         
         #sucess full after complition    
        app.quit()
        messagebox.showinfo("Success", "Processing completed successfully.")

    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occurred while processing Semester 2: {str(e)}"
        )

def sem3(workbook, row_start, row_end):
    try:
        ROW_START = int(row_start)
        ROW_END = int(row_end)
        
        #apn code run kadun drop down chnages kelayvar text box change karayla 
        output_text.configure(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)  # Clear previous messages
        output_text.insert(tk.END, "PROCESSING FILES FOR SEM 3....\n")
        output_text.configure(state=tk.DISABLED)
        root.update()
        
        #exel la launch kela (karn sem 1 run kelayvar sucessfull cha mesg dakvayla )
        app = xw.App(visible=False)

        #open
        CURRENT_WORKBOOK = xw.Book(workbook)
        #sem data cha acess 
        STUDENT_DATASHEET4 = CURRENT_WORKBOOK.sheets["Sem 3"]
        #template open 
        SHEET_TEMPLATE_wb = xw.Book(r"template.xlsx")
        #page 3 cha access deto 
        TemplatePage4 = SHEET_TEMPLATE_wb.sheets["Page 4"]

        #sub define kelet 
        sem3Subjects = tuple((STUDENT_DATASHEET4[f"C1"].value, STUDENT_DATASHEET4[f"F1"].value, STUDENT_DATASHEET4[f"I1"].value,
                             STUDENT_DATASHEET4[f"L1"].value, STUDENT_DATASHEET4[f"O1"].value))

        for row in range(ROW_START, ROW_END + 1):
            
            #prn getoy data base madun 
            PRN_FILE_NAME = STUDENT_DATASHEET4[f"A{row}"].value
            #open template 
            NEW_TEMPLATE = xw.Book(f"output\\{str(PRN_FILE_NAME)}.xlsx", ignore_read_only_recommended=True)
            #copy kartoy new template made 
            TemplatePage4.copy(after=NEW_TEMPLATE.sheets[2])
            
            #acess detoy page 3 template cha output folder madun 
            Page4 = NEW_TEMPLATE.sheets["Page 4"]

            #data from the current row
            dstupleSem3 = tuple((STUDENT_DATASHEET4[f"C{row}"].value, STUDENT_DATASHEET4[f"D{row}"].value, STUDENT_DATASHEET4[f"E{row}"].value, 
                             STUDENT_DATASHEET4[f"F{row}"].value, STUDENT_DATASHEET4[f"G{row}"].value, STUDENT_DATASHEET4[f"H{row}"].value, 
                             STUDENT_DATASHEET4[f"I{row}"].value, STUDENT_DATASHEET4[f"J{row}"].value, STUDENT_DATASHEET4[f"K{row}"].value, 
                             STUDENT_DATASHEET4[f"L{row}"].value, STUDENT_DATASHEET4[f"M{row}"].value, STUDENT_DATASHEET4[f"N{row}"].value, 
                             STUDENT_DATASHEET4[f"O{row}"].value, STUDENT_DATASHEET4[f"P{row}"].value, STUDENT_DATASHEET4[f"Q{row}"].value))
           # Assign values pretket cell la 
            (Page4["C8"].value, Page4["D8"].value, Page4["F8"].value, Page4["C9"].value, Page4["D9"].value, Page4["F9"].value, 
         Page4["C10"].value, Page4["D10"].value, Page4["F10"].value, Page4["C11"].value, Page4["D11"].value, Page4["F11"].value, 
         Page4["C12"].value, Page4["D12"].value, Page4["F12"].value) = dstupleSem3
            
            (Page4["B8"].value, Page4["B9"].value, Page4["B10"].value, Page4["B11"].value, Page4["B12"].value) = sem3Subjects

            NEW_TEMPLATE.save()
            NEW_TEMPLATE.close()
            
            #same logic above 
            output_text.configure(state=tk.NORMAL)
            output_text.insert(tk.END, f"FILLED SEM 3 MARKS OF {PRN_FILE_NAME}\n","red")
            output_text.configure(state=tk.DISABLED)
            root.update()
            output_text.configure(fg_color="white", text_color="red")
         
         #sucess full after complition    
        app.quit()
        messagebox.showinfo("Success", "Processing completed successfully.")

    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occurred while processing Semester 3: {str(e)}"
        )

def sem4(workbook, row_start, row_end):
    try:
        ROW_START = int(row_start)
        ROW_END = int(row_end)
        
        #apn code run kadun drop down chnages kelayvar text box change karayla 
        output_text.configure(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)  # Clear previous messages
        output_text.insert(tk.END, "PROCESSING FILES FOR SEM 4....\n")
        output_text.configure(state=tk.DISABLED)
        root.update()
        
        #exel la launch kela (karn sem 1 run kelayvar sucessfull cha mesg dakvayla )
        app = xw.App(visible=False)

        #open
        CURRENT_WORKBOOK = xw.Book(workbook)
        #sem data cha acess 
        STUDENT_DATASHEET5 = CURRENT_WORKBOOK.sheets["Sem 4"]

        #sub define kelet 
        sem4Subjects = tuple((STUDENT_DATASHEET5[f"C1"].value, STUDENT_DATASHEET5[f"F1"].value, STUDENT_DATASHEET5[f"I1"].value,
                             STUDENT_DATASHEET5[f"L1"].value, STUDENT_DATASHEET5[f"O1"].value))

        for row in range(ROW_START, ROW_END + 1):
            
            #prn getoy data base madun 
            PRN_FILE_NAME = STUDENT_DATASHEET5[f"A{row}"].value
            #open template 
            NEW_TEMPLATE = xw.Book(f"output\\{str(PRN_FILE_NAME)}.xlsx", ignore_read_only_recommended=True)
            
            #acess detoy page 3 template cha output folder madun 
            Page4 = NEW_TEMPLATE.sheets["Page 4"]

            #data from the current row
            dstupleSem4 = tuple((STUDENT_DATASHEET5[f"C{row}"].value, STUDENT_DATASHEET5[f"D{row}"].value, STUDENT_DATASHEET5[f"E{row}"].value, 
                             STUDENT_DATASHEET5[f"F{row}"].value, STUDENT_DATASHEET5[f"G{row}"].value, STUDENT_DATASHEET5[f"H{row}"].value, 
                             STUDENT_DATASHEET5[f"I{row}"].value, STUDENT_DATASHEET5[f"J{row}"].value, STUDENT_DATASHEET5[f"K{row}"].value, 
                             STUDENT_DATASHEET5[f"L{row}"].value, STUDENT_DATASHEET5[f"M{row}"].value, STUDENT_DATASHEET5[f"N{row}"].value, 
                             STUDENT_DATASHEET5[f"O{row}"].value, STUDENT_DATASHEET5[f"P{row}"].value, STUDENT_DATASHEET5[f"Q{row}"].value))
       
            (Page4["N8"].value, Page4["O8"].value, Page4["Q8"].value, Page4["N9"].value, Page4["O9"].value, Page4["Q9"].value, 
            Page4["N10"].value, Page4["O10"].value, Page4["Q10"].value, Page4["N11"].value, Page4["O11"].value, Page4["Q11"].value, 
            Page4["N12"].value, Page4["O12"].value, Page4["Q12"].value) = dstupleSem4
        
            (Page4["M8"].value, Page4["M9"].value, Page4["M10"].value, Page4["M11"].value, Page4["M12"].value) = sem4Subjects

            NEW_TEMPLATE.save()
            NEW_TEMPLATE.close()
            
            #same logic above 
            output_text.configure(state=tk.NORMAL)
            output_text.insert(tk.END, f"FILLED SEM 4 MARKS OF {PRN_FILE_NAME}\n","red")
            output_text.configure(state=tk.DISABLED)
            root.update()
            output_text.configure(fg_color="white", text_color="red")
         
         #sucess full after complition    
        app.quit()
        messagebox.showinfo("Success", "Processing completed successfully.")

    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occurred while processing Semester 4: {str(e)}"
        )

def sem5(workbook, row_start, row_end):
    try:
        ROW_START = int(row_start)
        ROW_END = int(row_end)
        
        #apn code run kadun drop down chnages kelayvar text box change karayla 
        output_text.configure(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)  # Clear previous messages
        output_text.insert(tk.END, "PROCESSING FILES FOR SEM 5....\n")
        output_text.configure(state=tk.DISABLED)
        root.update()
        
        #exel la launch kela (karn sem 1 run kelayvar sucessfull cha mesg dakvayla )
        app = xw.App(visible=False)

        #open
        CURRENT_WORKBOOK = xw.Book(workbook)
        #sem data cha acess 
        STUDENT_DATASHEET6 = CURRENT_WORKBOOK.sheets["Sem 5"]
        #template open 
        SHEET_TEMPLATE_wb = xw.Book(r"template.xlsx")
        #page 3 cha access deto 
        TemplatePage5 = SHEET_TEMPLATE_wb.sheets["Page 5"]

        #sub define kelet 
        sem5Subjects = tuple((STUDENT_DATASHEET6[f"C1"].value, STUDENT_DATASHEET6[f"F1"].value, STUDENT_DATASHEET6[f"I1"].value,
                             STUDENT_DATASHEET6[f"L1"].value, STUDENT_DATASHEET6[f"O1"].value))

        for row in range(ROW_START, ROW_END + 1):
            
            #prn getoy data base madun 
            PRN_FILE_NAME = STUDENT_DATASHEET6[f"A{row}"].value
            #open template 
            NEW_TEMPLATE = xw.Book(f"output\\{str(PRN_FILE_NAME)}.xlsx", ignore_read_only_recommended=True)
            #copy kartoy new template made 
            TemplatePage5.copy(after=NEW_TEMPLATE.sheets[3])
            Page5 = NEW_TEMPLATE.sheets["Page 5"]


            #data from the current row
            dstupleSem5 = tuple((STUDENT_DATASHEET6[f"C{row}"].value, STUDENT_DATASHEET6[f"D{row}"].value, STUDENT_DATASHEET6[f"E{row}"].value, 
                             STUDENT_DATASHEET6[f"F{row}"].value, STUDENT_DATASHEET6[f"G{row}"].value, STUDENT_DATASHEET6[f"H{row}"].value, 
                             STUDENT_DATASHEET6[f"I{row}"].value, STUDENT_DATASHEET6[f"J{row}"].value, STUDENT_DATASHEET6[f"K{row}"].value, 
                             STUDENT_DATASHEET6[f"L{row}"].value, STUDENT_DATASHEET6[f"M{row}"].value, STUDENT_DATASHEET6[f"N{row}"].value, 
                             STUDENT_DATASHEET6[f"O{row}"].value, STUDENT_DATASHEET6[f"P{row}"].value, STUDENT_DATASHEET6[f"Q{row}"].value))
       
            (Page5["C8"].value, Page5["D8"].value, Page5["F8"].value, Page5["C9"].value, Page5["D9"].value, Page5["F9"].value, 
            Page5["C10"].value, Page5["D10"].value, Page5["F10"].value, Page5["C11"].value, Page5["D11"].value, Page5["F11"].value, 
            Page5["C12"].value, Page5["D12"].value, Page5["F12"].value) = dstupleSem5
        
            (Page5["B8"].value, Page5["B9"].value, Page5["B10"].value, Page5["B11"].value, Page5["B12"].value) = sem5Subjects

            NEW_TEMPLATE.save()
            NEW_TEMPLATE.close()
            
            #same logic above 
            output_text.configure(state=tk.NORMAL)
            output_text.insert(tk.END, f"FILLED SEM 5 MARKS OF {PRN_FILE_NAME}\n","red")
            output_text.configure(state=tk.DISABLED)
            root.update()
            output_text.configure(fg_color="white", text_color="red")
         
         #sucess full after complition    
        app.quit()
        messagebox.showinfo("Success", "Processing completed successfully.")

    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occurred while processing Semester 5: {str(e)}"
        )

def sem6(workbook, row_start, row_end):
    try:
        ROW_START = int(row_start)
        ROW_END = int(row_end)
        
        #apn code run kadun drop down chnages kelayvar text box change karayla 
        output_text.configure(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)  # Clear previous messages
        output_text.insert(tk.END, "PROCESSING FILES FOR SEM 6....\n")
        output_text.configure(state=tk.DISABLED)
        root.update()
        
        #exel la launch kela (karn sem 1 run kelayvar sucessfull cha mesg dakvayla )
        app = xw.App(visible=False)

        #open
        CURRENT_WORKBOOK = xw.Book(workbook)
        #sem data cha acess 
        STUDENT_DATASHEET7 = CURRENT_WORKBOOK.sheets["Sem 6"]

        #sub define kelet 
        sem6Subjects = tuple((STUDENT_DATASHEET7[f"C1"].value, STUDENT_DATASHEET7[f"F1"].value, STUDENT_DATASHEET7[f"I1"].value,
                             STUDENT_DATASHEET7[f"L1"].value, STUDENT_DATASHEET7[f"O1"].value))

        for row in range(ROW_START, ROW_END + 1):
            
            #prn getoy data base madun 
            PRN_FILE_NAME = STUDENT_DATASHEET7[f"A{row}"].value
            #open template 
            NEW_TEMPLATE = xw.Book(f"output\\{str(PRN_FILE_NAME)}.xlsx", ignore_read_only_recommended=True)
            
            #acess detoy page 3 template cha output folder madun 
            Page5 = NEW_TEMPLATE.sheets["Page 5"]

            dstupleSem6 = tuple((STUDENT_DATASHEET7[f"C{row}"].value, STUDENT_DATASHEET7[f"D{row}"].value, STUDENT_DATASHEET7[f"E{row}"].value, 
                                STUDENT_DATASHEET7[f"F{row}"].value, STUDENT_DATASHEET7[f"G{row}"].value, STUDENT_DATASHEET7[f"H{row}"].value, 
                                STUDENT_DATASHEET7[f"I{row}"].value, STUDENT_DATASHEET7[f"J{row}"].value, STUDENT_DATASHEET7[f"K{row}"].value, 
                                STUDENT_DATASHEET7[f"L{row}"].value, STUDENT_DATASHEET7[f"M{row}"].value, STUDENT_DATASHEET7[f"N{row}"].value, 
                                STUDENT_DATASHEET7[f"O{row}"].value, STUDENT_DATASHEET7[f"P{row}"].value, STUDENT_DATASHEET7[f"Q{row}"].value))

            (Page5["N8"].value, Page5["O8"].value, Page5["Q8"].value, Page5["N9"].value, Page5["O9"].value, Page5["Q9"].value, 
            Page5["N10"].value, Page5["O10"].value, Page5["Q10"].value, Page5["N11"].value, Page5["O11"].value, Page5["Q11"].value, 
            Page5["N12"].value, Page5["O12"].value, Page5["Q12"].value) = dstupleSem6
            
            (Page5["M8"].value, Page5["M9"].value, Page5["M10"].value, Page5["M11"].value, Page5["M12"].value) = sem6Subjects

            NEW_TEMPLATE.save()
            NEW_TEMPLATE.close()
            
            #same logic above 
            output_text.configure(state=tk.NORMAL)
            output_text.insert(tk.END, f"FILLED SEM 6 MARKS OF {PRN_FILE_NAME}\n","red")
            output_text.configure(state=tk.DISABLED)
            root.update()
            output_text.configure(fg_color="white", text_color="red")
         
         #sucess full after complition    
        app.quit()
        messagebox.showinfo("Success", "Processing completed successfully.")

    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occurred while processing Semester 6: {str(e)}"
        )

def sem7(workbook, row_start, row_end):
    try:
        ROW_START = int(row_start)
        ROW_END = int(row_end)
        
        #apn code run kadun drop down chnages kelayvar text box change karayla 
        output_text.configure(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)  # Clear previous messages
        output_text.insert(tk.END, "PROCESSING FILES FOR SEM 7....\n")
        output_text.configure(state=tk.DISABLED)
        root.update()
        
        #exel la launch kela (karn sem 1 run kelayvar sucessfull cha mesg dakvayla )
        app = xw.App(visible=False)

        #open
        CURRENT_WORKBOOK = xw.Book(workbook)
        #sem data cha acess 
        STUDENT_DATASHEET8 = CURRENT_WORKBOOK.sheets["Sem 7"]
        #template open 
        SHEET_TEMPLATE_wb = xw.Book(r"template.xlsx")
        #page 3 cha access deto 
        TemplatePage6 = SHEET_TEMPLATE_wb.sheets["Page 6"]

        #sub define kelet 
        sem7Subjects = tuple((STUDENT_DATASHEET8[f"C1"].value, STUDENT_DATASHEET8[f"F1"].value, STUDENT_DATASHEET8[f"I1"].value,
                             STUDENT_DATASHEET8[f"L1"].value, STUDENT_DATASHEET8[f"O1"].value))

        for row in range(ROW_START, ROW_END + 1):
            
            #prn getoy data base madun 
            PRN_FILE_NAME = STUDENT_DATASHEET8[f"A{row}"].value
            #open template 
            NEW_TEMPLATE = xw.Book(f"output\\{str(PRN_FILE_NAME)}.xlsx", ignore_read_only_recommended=True)
            #copy kartoy new template made 
            TemplatePage6.copy(after=NEW_TEMPLATE.sheets[4])
            Page6 = NEW_TEMPLATE.sheets["Page 6"]

            dstupleSem7 = tuple((STUDENT_DATASHEET8[f"C{row}"].value, STUDENT_DATASHEET8[f"D{row}"].value, STUDENT_DATASHEET8[f"E{row}"].value, 
                                STUDENT_DATASHEET8[f"F{row}"].value, STUDENT_DATASHEET8[f"G{row}"].value, STUDENT_DATASHEET8[f"H{row}"].value, 
                                STUDENT_DATASHEET8[f"I{row}"].value, STUDENT_DATASHEET8[f"J{row}"].value, STUDENT_DATASHEET8[f"K{row}"].value, 
                                STUDENT_DATASHEET8[f"L{row}"].value, STUDENT_DATASHEET8[f"M{row}"].value, STUDENT_DATASHEET8[f"N{row}"].value, 
                                STUDENT_DATASHEET8[f"O{row}"].value, STUDENT_DATASHEET8[f"P{row}"].value, STUDENT_DATASHEET8[f"Q{row}"].value))

            (Page6["C8"].value, Page6["D8"].value, Page6["F8"].value, Page6["C9"].value, Page6["D9"].value, Page6["F9"].value, 
            Page6["C10"].value, Page6["D10"].value, Page6["F10"].value, Page6["C11"].value, Page6["D11"].value, Page6["F11"].value, 
            Page6["C12"].value, Page6["D12"].value, Page6["F12"].value) = dstupleSem7
            
            (Page6["B8"].value, Page6["B9"].value, Page6["B10"].value, Page6["B11"].value, Page6["B12"].value) = sem7Subjects

            NEW_TEMPLATE.save()
            NEW_TEMPLATE.close()
            
            #same logic above 
            output_text.configure(state=tk.NORMAL)
            output_text.insert(tk.END, f"FILLED SEM 7 MARKS OF {PRN_FILE_NAME}\n","red")
            output_text.configure(state=tk.DISABLED)
            root.update()
            output_text.configure(fg_color="white", text_color="red")
         
         #sucess full after complition    
        app.quit()
        messagebox.showinfo("Success", "Processing completed successfully.")

    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occurred while processing Semester 7: {str(e)}"
        )

def sem8(workbook, row_start, row_end):
    try:
        ROW_START = int(row_start)
        ROW_END = int(row_end)
        
        #apn code run kadun drop down chnages kelayvar text box change karayla 
        output_text.configure(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)  # Clear previous messages
        output_text.insert(tk.END, "PROCESSING FILES FOR SEM 8....\n")
        output_text.configure(state=tk.DISABLED)
        root.update()
        
        #exel la launch kela (karn sem 1 run kelayvar sucessfull cha mesg dakvayla )
        app = xw.App(visible=False)

        #open
        CURRENT_WORKBOOK = xw.Book(workbook)
        #sem data cha acess 
        STUDENT_DATASHEET9 = CURRENT_WORKBOOK.sheets["Sem 8"]

        #sub define kelet 
        sem8Subjects = tuple((STUDENT_DATASHEET9[f"C1"].value, STUDENT_DATASHEET9[f"F1"].value, STUDENT_DATASHEET9[f"I1"].value,
                             STUDENT_DATASHEET9[f"L1"].value, STUDENT_DATASHEET9[f"O1"].value))

        for row in range(ROW_START, ROW_END + 1):
            
            #prn getoy data base madun 
            PRN_FILE_NAME = STUDENT_DATASHEET9[f"A{row}"].value
            #open template 
            NEW_TEMPLATE = xw.Book(f"output\\{str(PRN_FILE_NAME)}.xlsx", ignore_read_only_recommended=True)
            
            #acess detoy page 3 template cha output folder madun 
            Page6 = NEW_TEMPLATE.sheets["Page 6"]

            dstupleSem8 = tuple((STUDENT_DATASHEET9[f"C{row}"].value, STUDENT_DATASHEET9[f"D{row}"].value, STUDENT_DATASHEET9[f"E{row}"].value, 
                                STUDENT_DATASHEET9[f"F{row}"].value, STUDENT_DATASHEET9[f"G{row}"].value, STUDENT_DATASHEET9[f"H{row}"].value, 
                                STUDENT_DATASHEET9[f"I{row}"].value, STUDENT_DATASHEET9[f"J{row}"].value, STUDENT_DATASHEET9[f"K{row}"].value, 
                                STUDENT_DATASHEET9[f"L{row}"].value, STUDENT_DATASHEET9[f"M{row}"].value, STUDENT_DATASHEET9[f"N{row}"].value, 
                                STUDENT_DATASHEET9[f"O{row}"].value, STUDENT_DATASHEET9[f"P{row}"].value, STUDENT_DATASHEET9[f"Q{row}"].value))

            (Page6["N8"].value, Page6["O8"].value, Page6["Q8"].value, Page6["N9"].value, Page6["O9"].value, Page6["Q9"].value, 
            Page6["N10"].value, Page6["O10"].value, Page6["Q10"].value, Page6["N11"].value, Page6["O11"].value, Page6["Q11"].value, 
            Page6["N12"].value, Page6["O12"].value, Page6["Q12"].value) = dstupleSem8
            
            (Page6["M8"].value, Page6["M9"].value, Page6["M10"].value, Page6["M11"].value, Page6["M12"].value) = sem8Subjects

            NEW_TEMPLATE.save()
            NEW_TEMPLATE.close()
            
            #same logic above 
            output_text.configure(state=tk.NORMAL)
            output_text.insert(tk.END, f"FILLED SEM 8 MARKS OF {PRN_FILE_NAME}\n","red")
            output_text.configure(state=tk.DISABLED)
            root.update()
            output_text.configure(fg_color="white", text_color="red")
         
         #sucess full after complition    
        app.quit()
        messagebox.showinfo("Success", "Processing completed successfully.")

    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occurred while processing Semester 8: {str(e)}"
        )
def extracurricular(workbook, row_start, row_end):        
    try:
        ROW_START = int(row_start)
        ROW_END = int(row_end)
        
        #apn code run kadun drop down chnages kelayvar text box change karayla 
        output_text.configure(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)  # Clear previous messages
        output_text.insert(tk.END, "PROCESSING FILES FOR EXTRACURRICULAR ACTIVITIES....\n")
        output_text.configure(state=tk.DISABLED)
        root.update()
        
        #exel la launch kela (karn sem 1 run kelayvar sucessfull cha mesg dakvayla )
        app = xw.App(visible=False)

        #open
        CURRENT_WORKBOOK = xw.Book(workbook)
        #sem data cha acess 
        STUDENT_DATASHEET10 = CURRENT_WORKBOOK.sheets["Extra Curricular"]
        #template open 
        SHEET_TEMPLATE_wb = xw.Book(r"template.xlsx")
        TemplatePage7 = SHEET_TEMPLATE_wb.sheets["Page 7"]
        TemplatePage8 = SHEET_TEMPLATE_wb.sheets["Page 8"]

        for row in range(ROW_START, ROW_END + 1):
            
            #prn getoy data base madun 
            PRN_FILE_NAME = STUDENT_DATASHEET10[f"A{row}"].value
            #open template 
            NEW_TEMPLATE = xw.Book(f"output\\{str(PRN_FILE_NAME)}.xlsx", ignore_read_only_recommended=True)
            TemplatePage7.copy(after=NEW_TEMPLATE.sheets[5])
            TemplatePage8.copy(after=NEW_TEMPLATE.sheets[6])
            Page7 = NEW_TEMPLATE.sheets["Page 7"]

            extraCurricular = tuple((STUDENT_DATASHEET10[f"C{row}"].value, STUDENT_DATASHEET10[f"D{row}"].value, 
                    STUDENT_DATASHEET10[f"E{row}"].value, STUDENT_DATASHEET10[f"F{row}"].value, STUDENT_DATASHEET10[f"G{row}"].value, 
                    STUDENT_DATASHEET10[f"H{row}"].value, STUDENT_DATASHEET10[f"I{row}"].value, STUDENT_DATASHEET10[f"J{row}"].value))
        
            (Page7["A3"].value, Page7["F3"].value, Page7["A14"].value, Page7["F14"].value, 
            Page7["A25"].value, Page7["F25"].value, Page7["A36"].value, Page7["F36"].value) = extraCurricular

            NEW_TEMPLATE.save()
            NEW_TEMPLATE.close()
            
            #same logic above 
            output_text.configure(state=tk.NORMAL)
            output_text.insert(tk.END, f"FILLED EXTRACURRICULAR ACTIVITIES OF {PRN_FILE_NAME}\n","red")
            output_text.configure(state=tk.DISABLED)
            root.update()
            output_text.configure(fg_color="white", text_color="red")
         
         #sucess full after complition    
        app.quit()
        messagebox.showinfo("Success", "Processing completed successfully.")

    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occurred while processing EXTRACURRICULAR ACTIVITIES: {str(e)}"
        )


def process_selected_option(file_path_var):
    #jo pan file path alela ahe variblae madun to ata workbook made gelay
    workbook = file_path_var.get()  
    #selection option ahe tkinter varcha 
    selected_option = option_var.get()
    
    if selected_option == "Fill Page 1 and Page 2":
        fill_page1_and_page2(workbook, start_row_entry.get(), end_row_entry.get())
    elif selected_option == "Process Semester 1":
        sem1(workbook, start_row_entry.get(), end_row_entry.get())
    elif selected_option == "Process Semester 2":
        sem2(workbook, start_row_entry.get(), end_row_entry.get())
    elif selected_option == "Process Semester 3":
        sem3(workbook, start_row_entry.get(), end_row_entry.get())
    elif selected_option == "Process Semester 4":
        sem4(workbook, start_row_entry.get(), end_row_entry.get())
    elif selected_option == "Process Semester 5":
        sem5(workbook, start_row_entry.get(), end_row_entry.get()) 
    elif selected_option == "Process Semester 6":
        sem6(workbook, start_row_entry.get(), end_row_entry.get())
    elif selected_option == "Process Semester 7":
        sem7(workbook, start_row_entry.get(), end_row_entry.get())
    elif selected_option == "Process Semester 8":
        sem8(workbook, start_row_entry.get(), end_row_entry.get())
    elif selected_option == "Process Extra curricular Activities":
        extracurricular(workbook, start_row_entry.get(), end_row_entry.get())
  



# logo chya bajucha text ahe (title of the GUI window)
root.title("SIES GST - Campus Edu Track")
root.iconbitmap('logo.ico')



# Custom Fonts
title_font = ("Lucida Bright", 24, "bold")  #label chi styling specially title chi 
button_font = ("Cambria", 12) # button chi styling 
label_font = ("Cambria", 15,"bold") #font lable cha 

# Custom Colors
root.configure(bg="black")
# bg_color = "#2F9E82"
bg_color = "#000000"
fg_color = "#FFFFFF"  # White text color
button_bg_color = "#8B0000"  # Dark red color
button_fg_color = "#000000"  # Black text color
dropdown_bg_color = "#212121"  # Dark grey color
dropdown_fg_color = "#FFFFFF"  # White text color
box_bg_color = "#000000"  # Dark black color for box

# Center the window
window_width = 800
window_height = 600
#dont touch it its for all centre 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width - window_width) / 2)
y_cordinate = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")


# Styling
style = ttk.Style()
style.configure("Title.TLabel", font=title_font, foreground=fg_color, background=bg_color)
style.configure("TButton", font=button_font, foreground=button_fg_color, background=button_bg_color)
style.configure("TLabel", font=label_font, foreground=fg_color, background=bg_color)
style.configure("TEntry", fieldbackground='white')  
style.map("TCombobox", fieldbackground=[("readonly", dropdown_bg_color)], foreground=[("readonly", dropdown_fg_color)], background=[("readonly", dropdown_bg_color)], selectbackground=[("readonly", bg_color)], selectforeground=[("readonly", fg_color)])  

# Create top interface
title_label = ttk.Label(root, text="SIES GST - Campus Edu Track", style="Title.TLabel")
title_label.pack(pady=(20, 0))

# Load and display logo
logo_image = Image.open("logo.jpeg") 
logo_image = logo_image.resize((100, 100))  # Resize the image
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = ttk.Label(root, image=logo_photo)
logo_label.image = logo_photo  
logo_label.pack(pady=(0, 20))

# Create main frame with black background
main_frame = ttk.Frame(root, padding=20, style="Black.TFrame")
main_frame.pack(expand=False)

# Style for black frame
style.configure("Black.TFrame", background=box_bg_color)

# Row 1: Browse Button
browse_button = cstk.CTkButton(main_frame, text="Browse Database", command=browse_file, corner_radius=400, bg_color="Black",text_color="black",font=("Arial", 22, "bold"),hover_color="violet")
browse_button.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# Row 2: File Path Entry
file_path_var = tk.StringVar()
file_path_entry = cstk.CTkEntry(main_frame, textvariable=file_path_var, width=400, corner_radius=40, bg_color="Black", border_color="Black",text_color="Black",font=("Lucida Bright", 20, "bold"))
file_path_entry.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Row 3: Start Row Entry
start_row_label = ttk.Label(main_frame, text="Enter Start Row Number:",)
start_row_label.grid(row=2, column=0, padx=5, pady=5)

start_row_var = tk.StringVar()
start_row_entry = cstk.CTkEntry(main_frame, textvariable=start_row_var, width=150, corner_radius=40, bg_color="black", border_color="black",text_color="black",font=("MathJax Fonts", 20, "bold"))
start_row_entry.grid(row=2, column=1, padx=5, pady=5)


# Row 4: End Row Entry
end_row_label = ttk.Label(main_frame, text="Enter End Row Number:")
end_row_label.grid(row=3, column=0, padx=5, pady=5)

end_row_var = tk.StringVar()
end_row_entry = cstk.CTkEntry(main_frame, textvariable=end_row_var, width=150, corner_radius=40, bg_color="black", border_color="black",text_color="black",font=("MathJax Fonts", 20, "bold"))
end_row_entry.grid(row=3, column=1, padx=5, pady=5)


# Row 5: Option Label
option_label = ttk.Label(main_frame, text="Select Operation:")
option_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Row 6: Option Combobox
options = [
    
    "Fill Page 1 and Page 2",
    "Process Semester 1",
    "Process Semester 2",
    "Process Semester 3",
    "Process Semester 4",
    "Process Semester 5",
    "Process Semester 6",
    "Process Semester 7",
    "Process Semester 8",
    "Process Extra curricular Activities"
]

option_var = tk.StringVar(root)
option_var.set(options[0])

# option_menu = cstk.CTkComboBox(main_frame, textvariable=option_var, values=options, state="readonly", width=30)
option_menu = cstk.CTkComboBox(main_frame, variable=option_var, values=options, state="readonly", width=300,
                                corner_radius=40, bg_color="black", dropdown_fg_color="White",
                                button_color="White",border_color="black",text_color="black",font=("Lucida Bright", 15, "bold")
                                )
option_menu.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
# Row 7: Process Button
process_button = cstk.CTkButton(main_frame, text="Process Selected Operation",
                                
                                 command=lambda: process_selected_option(file_path_var),
                                  corner_radius=400, bg_color="Black",text_color="black",font=("Lucida Bright", 18, "bold"),hover_color="violet")


process_button.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky="ew")



# Text Widget
output_text = cstk.CTkTextbox(root, height=1100, width=600, corner_radius=20, bg_color="black", border_color="black",font=("Lucida Bright", 20, "bold"))
output_text.pack()
root.update()
#changed here
output_text.configure(fg_color="white", text_color="red",font=("Lucida Bright", 15, "bold"))

root.mainloop()