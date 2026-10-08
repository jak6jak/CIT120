'''
Prgram assignment instructions:
Design a program for MCTC. The current tuition is $5,000 per year, and tuition is expected to increase by 3 percent each year. 
Display the tuition and the year for the next 10 years.  
You are required to use a loop. Name your file: HW08-<last name><first initial>


THE FUN:
Assignment never states how the tuition should be displayed.
I will be displaying the tuition as a line graph.
'''
from tkinter import *




def main():
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)


    # draw the graph
    canvas = Canvas(root)
    canvas.grid(column=0, row=0, sticky=(N, W, E, S))
    canvas.create_line(50, 250, 450, 250, width=2)  # x-axis
    canvas.create_line(50, 250, 50, 50, width=2)     # y-axis
    canvas.create_text(250, 280, text="Year", font=("Arial", 12))
    # draw the years on the x-axis
    for i in range(11):
        year = 2026 + i
        canvas.create_text(45*i + 100, 260, text=str(year), font=("Arial", 10))
    canvas.create_text(20, 150, text="Tuition", font=("Arial", 12), angle=90)
    root.mainloop()


if __name__ == "__main__":
    main()
