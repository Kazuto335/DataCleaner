# from customtkinter import *
# import pandas as pd
#
# df = pd.read_excel('test.xlsx')
# column_list = [a for a in df.head()]
# print(column_list)
#
#
# screen = CTk()
# screen.title('Split')
#
# # Vars
# text = StringVar()
# column = StringVar()
#
#
#
# #GUI's
# dropdown = CTkOptionMenu(screen, variable=column, values=column_list)
# dropdown.pack()
#
# entry = CTkEntry(screen, variable=text)
# entry.pa
# screen.mainloop()




# def split_sheet():
#     print(selected_col.get())
#     text_list = textstr.get().split(',')
#     print("Text list:", text_list)
#     print(text_list)
#
# # Check if the input text is empty or contains only whitespace characters
# if not textstr.get().strip():
#     print("Input text is empty. No files will be saved.")
#     return
#
# split_df_1 = df[df[selected_col.get()].isin(text_list)]
# split_df_2 = df[~df[selected_col.get()].isin(text_list)]
#
# split_df_1.to_excel('C:/Users/Himanshu/Desktop/file1.xlsx', index=False)
# split_df_2.to_excel('C:/Users/Himanshu/Desktop/file2.xlsx', index=False)
# print("Files saved")


import pandas as pd
# Read the Excel file
df = pd.read_excel("Scheme and Category.xlsx")

# Define the lists of tests for Group 1 and Group 2
group_1_tests = ["HBsAg", "Hepatitis C (HCV)", "HIV Test", "VDRL Test", "Widal Test",
                 "Dengue Serology", "Malaria", "Chikungunya", "Stool Routine",
                 "Pleural Fluid AFB", "Pleural Fluid Culture", "Pleural Fluid Protein",
                 "Pleural Fluid Routine", "Stool M/E", "Stool for Occult Blood",
                 "Blood Culture and Sensitivity", "Bleeding Time (BT)",
                 "Clotting Time (CT) - Activated", "Pap Smear", "Pus Culture and Sensitivity",
                 "AFB Sputum", "Stool Culture and Sensitivity", "Pleural Fluid Sensitivity",
                 "Blood - Serological Test", "HVS Culture and Sensitivity", "AFB Culture",
                 "Ascitic Fluid AFB", "Ascitic Fluid Protein", "Ascitic Fluid Routine",
                 "Ascitic Fluid Culture", "Cerebrospinal Fluid (CSF) - Culture",
                 "Cerebrospinal Fluid (CSF) - Sensitivity", "Cerebrospinal Fluid (CSF) - AFB",
                 "H1N1 (Swine Flu) Test", "CA 19.9", "Hepatitis A"]

# Filter data for Group 1
group_1_data = df[df["Service Name"].isin(group_1_tests)]

# Filter data for Group 2
group_2_data = df[~df["Service Name"].isin(group_1_tests)]

# Write Group 1 data to Excel
group_1_data.to_excel("group_1_data.xlsx", index=False)

# Write Group 2 data to Excel
group_2_data.to_excel("group_2_data.xlsx", index=False)
