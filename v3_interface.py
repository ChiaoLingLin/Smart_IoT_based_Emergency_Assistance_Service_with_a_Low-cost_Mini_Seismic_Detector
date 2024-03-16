import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from firebase import firebase
import threading
import time

main_frame = None
my_canvas = None

def retrieve_data():
    url = "https://bamboo-storm-392603-default-rtdb.firebaseio.com/"
    fdb = firebase.FirebaseApplication(url, None)
    return fdb.get('/user', None)

def create_text_widget(frame, text_data):
    text = tk.Text(frame, height=5, width=700)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    text.configure(yscrollcommand=scrollbar.set)
    text.insert(tk.END, "Box Loacation: \n")
    text.insert(tk.END, text_data['boxLoaction'])
    text.insert(tk.END, '\n')
    text.insert(tk.END, "\nVictims: \n")
    text.insert(tk.END, text_data['List'])
    text.insert(tk.END, '\n\n\n')

def refresh_interface():
    global main_frame, my_canvas
    
    result = retrieve_data()
    
    #print('Now:', time.strftime('%H:%M:%S', time.localtime()))
    
    # Clear previous content
    if main_frame:
        main_frame.destroy()
    if my_canvas:
        my_canvas.destroy()
    
    # Create the main frame and canvas
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = tk.Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    frame2 = tk.Frame(second_frame)
    frame2.pack()
    
    text = tk.Text(frame2, height=1, width=700)
    text.pack(side=tk.LEFT, fill='x', expand=True)
    text.insert(tk.END, "地震盒即時資料系統/"+ str(time.strftime('%H:%M:%S', time.localtime()))+'\n')
    for v in result.values():
        for vv in v.values():
            frame = tk.Frame(second_frame)
            frame.pack()
            create_text_widget(frame, vv)
    
    second_frame.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))
    
    # Schedule the next refresh after 20 seconds
    threading.Timer(20, refresh_interface).start()

root = tk.Tk()
root.title("Earthquake Realtime Data")
root.geometry("700x700")

# Start refreshing the interface
refresh_interface()

root.mainloop()
