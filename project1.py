import tkinter as tk
import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
def highlightit(start,end):
    txt.tag_add('error','1.'+str(start),'1.'+str(end))
    txt.tag_config('error',background='yellow')

def txtcheck():
    text = txt.get('0.0',tk.END)
    correcttext=tool.correct(text)
    txtc.delete('0.0',tk.END)
    txtc.insert('0.0',correcttext)
    errors = tool.check(text)
    for e in errors:
        print (e.offset , e.offset+e.errorLength)
        highlightit(e.offset , e.offset+e.errorLength)

window = tk.Tk()
window.title('المصحح اللغوي 0.1')
window.geometry("400x350")
lbl = tk.Label(window,text='برنامج مصحح لغوي وقواعدي')
btn = tk.Button (window,text='Check', command=txtcheck)
txt = tk.Text(window,height=6, font=('Arial Bold',15))
txtc = tk.Text(window,height=6, font=('Arial Bold',15))
lbl.pack()
btn.pack()
txt.pack()
txtc.pack()
window.mainloop()
