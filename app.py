import tkinter
window = tkinter.Tk()
window.title("T004")
window.geometry("900x400")

top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")


label = tkinter.Label(window, text="This is my app.",  bg ="black", fg = "white", font = "56" ).pack()




window.mainloop()