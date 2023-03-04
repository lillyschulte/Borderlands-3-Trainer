import tkinter as tk
import pyMeow as pm

class App:
    def __init__(self, master):
        self.master = master
        self.slider = tk.Scale(self.master, from_=0, to=9999, orient=tk.HORIZONTAL)
        self.slider.pack()
        self.keys_button = tk.Button(self.master, text="GIMME DEM KEYS", command=self.on_keys_button_click)
        self.keys_button.pack()
    
    def on_keys_button_click(self):
        value = int(self.slider.get())
        process = pm.open_process(processName="Borderlands3.exe")
        base_address = pm.get_module(process, "Borderlands3.exe")["base"]
        keys_offsets = [0xA0, 0x638, 0x0, 0x4D8, 0x928, 0x1B0, 0x1238, 0x8]
        keys_addr = pm.pointer_chain_64(process, base_address + 0x06DFD920, keys_offsets)
        pm.w_int(process, keys_addr, value)

root = tk.Tk()
app = App(root)
root.mainloop()
