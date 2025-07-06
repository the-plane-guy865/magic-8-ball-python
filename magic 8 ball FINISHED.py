import tkinter as tk
import random as rdm

responses = ['Absolutely', 'Probably', 'Maybe', 'Very little chance', 'Unlikely', 'Highly Unlikely', 'No chance']


root = tk.Tk()
root.title('Magic 8 Ball')
root.geometry('200x105')

question_var = tk.StringVar()


def reset():
    response_DISPLAY.destroy()
    txt_box.delete(0, 'end')


def submit():
    question = question_var.get()

    CPU_response = tk.StringVar()
    CPU_response.set(rdm.choice(responses))
    global response_DISPLAY
    response_DISPLAY = tk.Label(root, textvariable=CPU_response, font=('calibre',10,'normal'))
    response_DISPLAY.pack()
    


txt_box = tk.Entry(root, textvariable=question_var, font=('calibre',10,'normal'))
txt_box.pack()

submit_btn=tk.Button(root,text = 'Submit', command = submit)
submit_btn.pack()

reset_btn=tk.Button(root,text = 'Reset', command = reset)
reset_btn.pack()


# README
print('**README**')
print('Magic 8 Ball by Luca R \nType in a question and click submit. The computer will give you an answer. \nClick reset to have another go \nCopyright Luca R 2025')




root.mainloop()



