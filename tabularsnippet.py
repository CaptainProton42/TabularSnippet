# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:03:58 2018

@author: DerSc
"""

# ***************************************************
# *     TXT zu LaTeX Tabellenkonvertierungstool     *
# *                2018 John Wigg                   *
# ***************************************************
#
# Spalten müssen durch Tabstopps getrennt sein.

#####################################################
# NUTZERVARIABLEN

ignore_lines = 1                        # Überspringt zu Beginn Zeilen
using_math_mode = False                  # Auf True setzen, wenn Einträge im Mathemodus gesetzt werden sollen
units = ['', '\\volt', '\\volt', '\\hertz', '\\second']    # Einheiten der einzelnen Spalten (benötigt das Package "siunitx").
path_data = 'example.txt'                # Speicherort der Daten

#####################################################
# NICHT EDITIEREN

import numpy as np
import tkinter as Tk

data = np.loadtxt(path_data, dtype=str, skiprows=ignore_lines)

rows = data.shape[0]
columns = data.shape[1]

root = Tk.Tk()
root.title("Tabular Snippet")
T = Tk.Text(root, height=rows, width=30*columns)
T.pack()

for i in range(rows):
    for j in range(columns):
        if (using_math_mode):
            if(units[j]):
                T.insert(Tk.END, '$\\SI{' + data[i, j] + '}{' + units[j] + '}$')
            else:
                T.insert(Tk.END, '$' + data[i, j] + '$')
        else:
            if(units[j]):
                T.insert(Tk.END, '\\SI{' + data[i, j] + '}{' + units[j] + '}')
            else:
                T.insert(Tk.END, data[i, j])
        if (j < columns - 1):
            T.insert(Tk.END, '\t& ')
    T.insert(Tk.END, ' \\\\ \n')
    
Tk.mainloop()
