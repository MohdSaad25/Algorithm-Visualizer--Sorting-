import tkinter as tk
import random
root = tk.Tk()
root.title("Algorithm Visualizer")
root.geometry("800x600")
root.configure(bg="#F8FAFC")
root.resizable(False,False)

#------Title Header------
header_frame = tk.Frame(root, bg="#F8FAFC")
header_frame.pack(pady=(25, 5))
title_label=tk.Label(header_frame,text="ALGORITHM VISUALIZER",
font=("Segoe UI",22,"bold"),
bg="#F8FAFC",
fg="#334155"
)
title_label.pack()

#------Control Pannel (buttons)-----

control_frame=tk.Frame(root,bg="#F8FAFC")
control_frame.pack(pady=15)

#------Status Bar------
status_frame=tk.Frame(root,bg="#F1F5F9", padx=16, pady=6)
status_frame.pack()
status =tk.Label(root,
text=">Ready ⸜(｡˃ ᵕ ˂ )⸝",
bg="#E2E8F0",
font=("Consolas",11),
fg="#4dabf7",
)

status.pack(pady=5)


#------Visualizer Canvas------

canvas = tk.Canvas(root,width=740,
    height=400,
    bg="#FFFFFF",
    highlightbackground="#E2E8F0",
    highlightthickness=1)
canvas.pack(pady=5)


values=[]
rectangle=[]
text_labels=[]

#------Background Grid-------

def draw_bg_grid():
    canvas.delete("grid_pattern")
    grid_color = "#E2E8F0"
    for x in range(30, 740, 30):
        canvas.create_line(x, 0, x, 400, fill=grid_color, width=1, tags="grid_pattern")
    for y in range(30, 400, 30):
        canvas.create_line(0, y, 740, y, fill=grid_color, width=1, tags="grid_pattern")
    canvas.create_line(20, 400, 720, 400, fill="#64748B", width=2, tags="grid_pattern")
    draw_cute_mascot()
#------Just for fun-------

def draw_cute_mascot():
    
    canvas.create_oval(
        640, 20, 700, 60, fill="#FFFFFF", outline="#CBD5E1", width=2
    )
    canvas.create_oval(
        620, 30, 670, 70, fill="#FFFFFF", outline="#CBD5E1", width=2
    )
    canvas.create_oval(
        660, 30, 710, 70, fill="#FFFFFF", outline="#CBD5E1", width=2
    )

    canvas.create_oval(645, 42, 649, 48, fill="#334155")
    canvas.create_oval(675, 42, 679, 48, fill="#334155")

    canvas.create_oval(638, 48, 646, 53, fill="#FDA4AF", outline="")
    canvas.create_oval(678, 48, 686, 53, fill="#FDA4AF", outline="")

    canvas.create_arc(
        657, 45, 667, 53, start=200, extent=140, style="arc", width=2
    )



#_________________________________________________

def generate_array():
    values.clear()
    for rect in rectangle:
        canvas.delete(rect)
    for text in text_labels:
        canvas.delete(text)     
    rectangle.clear()
    text_labels.clear()

    
    draw_bg_grid() 
    for i in range(6):
        num = random.randint(10,300)
        values.append(num)
    print(values)  



    for i, num in enumerate(values):
        x = 200 + i*60
        height=num*0.8+20
        y = 400 - height

        rect = canvas.create_rectangle(
        x, y, x+30, 400,
        fill="#60A5FA",
        outline="#021E4C",
        width=2
        )

        rectangle.append(rect)
        text = canvas.create_text(
        x+15, y+10,
        text=num,
        fill="white"
        )
        text_labels.append(text) 
    status.config(text=">New Array Generated",fg="#64748B",bg="#E2E8F0")

#________________________________________________

def bubble_sort(values):
        def bubble_step(j,i):   
                status.config(text=f"> Comparing {values[j]} and {values[j+1]}...(⊙_⊙)",fg="#F59E0B")
                for k in range(len(values)-1-i):
                     canvas.itemconfig(rectangle[k],fill="#e04df7")


                if j+1<len(values)-1-i:
                    canvas.itemconfig(rectangle[j],fill="#F97316", outline="#944106")
                    canvas.itemconfig(rectangle[j+1],fill="#F97316",outline="#944106")


                if values[j]>values[j+1]:
                    values[j],values[j+1]=values[j+1],values[j]

                    height1=values[j]*0.8+20
                    canvas.coords(rectangle[j],200+j*60,400-height1,230+j*60,400) #changing bar positions
                    canvas.coords(text_labels[j],200+j*60+15,400-height1+10) #changing bars text


                    height2=values[j+1]*0.8+20
                    canvas.coords(rectangle[j+1],200+(j+1)*60,400-height2,230+(j+1)*60,400)
                    canvas.coords(text_labels[j+1],200+(j+1)*60+15,400-height2+10)


                    canvas.itemconfig(text_labels[j],text=values[j])  #changing bars text value
                    canvas.itemconfig(text_labels[j+1],text=values[j+1])


                if j<len(values)-2:
                    root.after(200,bubble_step,j+1,i)
                 
                else:
                    if i<len(values)-2:
                        root.after(200,bubble_step,0,i+1)
                        canvas.itemconfig(rectangle[len(values)-1-i],fill="#34D399",outline="#0F7F56")
                    else:
                        for rect in rectangle:
                            canvas.itemconfig(rect,fill="#34D399",outline="#0F7F56")
                        status.config(text=">Sort Completed! (★‿★)" ,fg="#10B981")    
                        print("Sort Completed") 
                        print("Sorted Values:",values)   
                
        bubble_step(0,0)

#_________________________________________________
 
generate_button = tk.Button(control_frame,text="[ GENERATE ]",
command=generate_array,bg="#E2E8F0",
fg="#334155",
activebackground="#CBD5E1",
activeforeground="#334155",
font=("Segoe UI", 10, "bold"),
relief="flat",
bd=0,
padx=15,
pady=7,
cursor="hand2")
generate_button.pack(side="left",padx=10)

start_button = tk.Button(control_frame,text="[ START ]",
command=lambda: bubble_sort(values),bg="#818CF8",
fg="#FFFFFF",
activebackground="#6366F1",
activeforeground="#FFFFFF",
font=("Segoe UI", 10, "bold"),
relief="flat",
bd=0,
padx=18,
pady=8,cursor="hand2")
start_button.pack(side="left",padx=8)
canvas.pack()
print(values) 
root.mainloop()

#---------------------------------------------------

















