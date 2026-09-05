import customtkinter as ctk
import random

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


root = ctk.CTk()
root.title("Selection Sort")
root.geometry("800x600")
root.configure(fg_color="#F4E1FF")
root.resizable(False,False)

header_frame=ctk.CTkFrame(
    root,
    fg_color="transparent",
)
header_frame.pack(pady=(15,5))

title_label=ctk.CTkLabel(
    header_frame,
    text="SELECTION SORT",
    font=("Segoe UI",22,"bold"),
    text_color="#280006"
)
title_label.pack(pady=(25,10))

subtitle=ctk.CTkLabel(
    header_frame,
    text="Algorithm Visualizer",
    font=("Segoe UI",24,"bold"),
    text_color="#64748B",
)
subtitle.pack()

status_label=ctk.CTkLabel(
    root,
    text=">Ready",
    font=("Consolas",12,"bold"),
    fg_color="#EAB308",
    corner_radius=8,
    padx=16,
    pady=6 
)
status_label.pack(pady=5)

control_frame=ctk.CTkFrame(
    root,fg_color="transparent"
)
control_frame.pack(pady=10)

card_frame=ctk.CTkFrame(
    root,
    fg_color="#FBF1FC",
    corner_radius=15,
    border_width=1,
    border_color="#E2E8F0"
)
card_frame.pack(padx=20,pady=10,fill="both",expand=True)


canvas = ctk.CTkCanvas(
    card_frame,
    width=740,
    height=400,
    bg="#FAFAFA",
    highlightbackground="#334155",
    highlightthickness=1
)
canvas.pack(pady=15)

speed_label=ctk.CTkLabel(
    control_frame,
    text="Speed:",
    font=("Segoe UI",11,"bold"),
    text_color="#94A3B8"
)
speed_label.pack(side="left",padx=(20,5))

speed_slider=ctk.CTkSlider(
    control_frame,
    from_=50,
    to=1000,
    number_of_steps=10,
    width=110,
    button_color="#6366F1",
    progress_color="#3B82F6"
)
speed_slider.set(200)
speed_slider.pack(side="left",padx=5)

def draw_grid():
    canvas.delete("grid_pattern")
    

    for x in range(30,740,30):
        canvas.create_line(x,0,x,400,
        fill="#F1F5F9",tags="grid_pattern")
    for y in range(30,400,30):
        canvas.create_line(0,y,740,y,
        fill="#F1F5F9",tags="grid_pattern")
    canvas.create_line(20,400,720,400,fill="#CBD5E1",
    width=2,tags="grid_pattern")

def gen_array():
    values.clear()
    rectangle.clear()
    text_label.clear()

    canvas.delete("all")
    draw_grid()

    for i in range(6):
        n = random.randint(10,300)
        values.append(n)

    for i,num in enumerate(values):
        x=200+i*60
        height=num*0.8+20
        y=400-height

        rect=canvas.create_rectangle(
            x,y,x+30,400,fill="#38BDF8",
            outline="#0284C7",
            width=2
        )
        rectangle.append(rect)

        txt=canvas.create_text(
            x+15,y-12,text=num,
            fill="#3F0230",
            font=("Segoe UI",10,"bold")
        )
        text_label.append(txt)


values=[]
rectangle=[]
text_label=[]


def selection_sort():
    def outer_loop(i):
        if i<len(values)-1:
            mini=i
            def inner_loop(j,mini):
                if j<len(values):

                    status_label.configure(
                        text=f"Comparing {values[j]} with {values[mini]}......"
                    )
                    for k in range(i+1,len(values)):
                        if k!=mini:
                            canvas.itemconfig(rectangle[k],fill="#38BDF8",outline="#0284C7")
                        else:
                            canvas.itemconfig(rectangle[k],fill="#FACC15",outline="#CA8A04")    

                    canvas.itemconfig(rectangle[j],fill="#FB923C",outline="#EA580C")



                    canvas.itemconfig(
                        rectangle[j],fill="#FB923C",
                        outline="#EA580C"
                    )
                    canvas.itemconfig(text_label[j],fill="#3F0230")
                    if values[j]<values[mini]:
                        mini=j
                        
                    root.after(int(speed_slider.get()),lambda:inner_loop(j+1,mini))
                else:
                    values[i],values[mini]=values[mini],values[i]

                    x_i=200+i*60
                    x_mini=200+mini*60
                    h_i=values[i]*0.8+20
                    h_mini=values[mini]*0.8+20

                    canvas.coords(rectangle[i],x_i,400-h_i,x_i+30,400)
                    canvas.coords(rectangle[mini],x_mini,400-h_mini,x_mini+30,400)

                    canvas.coords(text_label[i], x_i + 15, 400 - h_i - 12)
                    canvas.coords(text_label[mini], x_mini + 15, 400 - h_mini - 12)

                    canvas.itemconfig(text_label[i], text=values[i])
                    canvas.itemconfig(text_label[mini], text=values[mini])
                    

                    canvas.itemconfig(rectangle[i],fill="#4ADE80",outline="#16A34A")
                    
                    root.after(int(speed_slider.get()),lambda:outer_loop(i+1))
            inner_loop(i+1,mini)
        else:
            canvas.itemconfig(rectangle[-1],fill="#4ADE80",outline="#16A34A")
            status_label.configure(text="Array Sorted!")
    outer_loop(0)        


gen_button=ctk.CTkButton(
    control_frame,
    text="[GENERATE]",
    command=gen_array,
    font=("Segoe UI",12,"bold"),
    fg_color="#334155",
    hover_color="#475569",
    text_color="#F8FAFC",
    corner_radius=8,
    width=130,
    height=38
)
gen_button.pack(side="left",padx=10)

start_btn=ctk.CTkButton(
    control_frame,
    text="[START]",
    command=selection_sort,
    font=("Segoe UI",12,"bold"),
    fg_color="#6366F1",
    hover_color="#4F46E5",
    text_color="#FFFFFF",
    corner_radius=8,
    width=130,
    height=38,
)
start_btn.pack(side="left",padx=10)

root.mainloop()




