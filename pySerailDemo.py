    import serial
    import tkinter as tk 

    def click(): 
        ser.write(b'Test pySerial\n\r')

    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM2'
    ser.open()

    gui = tk.Tk()

    btn = tk.Button(gui,text = 'click', command = click)
    btn.pack()

    tk.mainloop()
