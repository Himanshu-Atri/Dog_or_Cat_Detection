# Importing Necessary Libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import numpy
import numpy as np
import tensorflow
from tensorflow.keras.models import load_model

# loading the model 
model = load_model("catVsdogs.keras")
bgcolor = '#2F3C7E'
fgcolor = '#FBEAEB'

# Initializing the GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Cat or Dog')
top.configure(background= bgcolor)

label1=Label(top,background=fgcolor,font=('arial',15,"bold"))
sign_image=Label(top)

def Detect(file_path):
    global label_packed
    
    image=Image.open(file_path)

    image=image.resize((224,224))
    image=np.expand_dims(image,axis=0)
    image=np.array(image, dtype=np.float32)
    
    image=np.delete(image,0,1)
    image=np.resize(image,(224,224,3))
    
    animal_dict= ['cat', 'dog']
    
    image=np.array([image], dtype=np.float32)/255.0
    
    prediction=model.predict(image)
    pred=int(np.round(prediction[0][0]))
    
    label1.configure(foreground=bgcolor,text=f"It's a {animal_dict[pred]}")

# Defining Show_detect button function
def show_Detect_button(file_path):
    Detect_b=Button(top,text="Detect Image",command=lambda: Detect(file_path),padx=10,pady=5)
    Detect_b.configure(background=fgcolor,foreground=bgcolor,font=('arial',10,'bold'))
    Detect_b.place(relx=0.79,rely=0.46) 

# Definig Upload Image Function
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        show_Detect_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an Image",command=upload_image,padx=10,pady=5)
upload.configure(background=fgcolor,foreground=bgcolor,font=('arial',10,'bold'))
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand=True)
label1.pack(side="bottom",expand=True)
heading=Label(top,text="Animal Detector",pady=20,font=('arial',20,"bold"))
heading.configure(background=fgcolor,foreground=bgcolor)
heading.pack()
top.mainloop()