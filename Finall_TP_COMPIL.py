# ----------------Info Developer-------------
# -Last Name : Lecheheb
# -First Name : Djaafar
# -Country : Algeria
# -Age : 26
# -Skills : Python - HTML - CSS - C
# -instagram : @ddos_attack_co
# ------------Fallowed Me for instagram-------

# install this

# pip install tkinter
# pip install termcolor
# pip install pyfiglet

#مكتبه تكنتر تساعدنا على انشاء واجهة باستخدام البايثون
from tkinter import *
#مكتبه النظام تساعدنا في تغير مسار النظام من اجل الصور
import os
from tkinter import messagebox
# هذه المكتبه تساعدنا في اخيار الملفات من داخل الواجهة
from tkinter.filedialog import askopenfilename, asksaveasfilename
# زخرفه النص
import termcolor
import pyfiglet

# chang path system
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Create Screen

# --------------------------------------

# تخزين المسار الملف الجديد لاستعماله مجددا
file_path = ''
def set_file_path(path):
    global file_path
    file_path = path
def main():
        

    # وضع صلاحيات تكنتر داخل متغير
    scr0 = Tk()
    # التحكم في ابعاد الواجهة
    scr0.geometry('860x500+300+130')
    # التحكم في تكبير تصغير النافذه
    scr0.resizable(False, False)
    # كتابه العنوان النافذه
    scr0.title("Code Editor (TP_COMPIL)")
    # وضع ايقونه لنافذه
    scr0.iconbitmap('programmer.ico')
    # لون النافذه
    scr0.config(background='#bdbdbd')


    # --------------------------------------
    # محرر الاكواد
    def root():
        # Create Screen
        root = Tk()
        # ابعاد الشاشه
        root.geometry('1000x600+230+70')
        # عدم تحكم في ابعاد الشاشه
        root.resizable()
        # عنوان اشاشه
        root.title("Code Editor (TP_COMPIL)")
        # ايقونه الشاشه
        root.iconbitmap('programmer.ico')
        # لون الخلفيه
        root.config(background='#bdbdbd')
        # --------------------------------------


        # دالة فتح الملف

        def open_file():
            # هنا ناخذ المسار الملف الذي اخترناه
            path = askopenfilename(filetypes=[("Text Files", "*.txt")])
            # نفتح الملف و نكتب فيه كل الذي مكتوب في المحرر
            with open(path, "r") as file:
                codes = file.read()
                Writ_Code.delete('1.0', END)
                Writ_Code.insert('1.0', codes)
                # نحفظ المسار هنا
                set_file_path(path)

        # دالة حفظ الملف

        def Save():
            code = Writ_Code.get('1.0', END)
            file = open(file_path, "w")
            # for x in code :
            #   file.write(x)
            file.write(code)
            file.close()
            set_file_path(file_path)

        # دالة انشاء الملف و حفظ النص

        def Save_As():
            if file_path == "":
                path = asksaveasfilename(filetypes=[('Text Files', '*.txt')])
            else:
                path = file_path
            with open(path, 'w') as file:
                code = Writ_Code.get('1.0', END)
                file.write(code)
                set_file_path(path)

        # --------------------------------------
        # تصفيه النص من الرموز و المسافات

        def last_car(text):
            last = len(text)
            for x in range(0, len(text)):
                if text[x] == "$":
                    last = x
            return last

        def fun_rm(text):
            if text.count('$') % 2 != 0:
                if text[-1] == '$':
                    return text[:-1]
                else:
                    return text[:last_car(text)]

            else:
                return text

        def chang_text(text_new, number=0):

            starting = 0
            lasting = 0
            num = text_new.count("$")/2

            if num > 0:

                starting = text_new.index("$", lasting)
                lasting = text_new.index("$", starting+1)
                text_new = text_new[:starting]+" "+text_new[lasting+1:]
                return chang_text(text_new, num-1)
            text_md = text_new

            return text_md

        def Tp_2():
            if file_path == "":
                path = "changes.txt"
                with open(path, 'w') as file:
                    code = Writ_Code.get('1.0', END)
                    file.write(code)
                set_file_path(path)
                file = open(file_path)
                Save()
            else:

                # copy_file_no_enter()
                file = open(file_path)
            file_code_Not_Comment_and_pass = open(
                r'file_code_not_comment_and_pass.txt', 'w')
            Save()
            # Loop file
            for x in file.readlines():
                # x.strip() --> stop for last character
                lin = x.strip()
                if lin == "" or lin == '$':
                    continue
                if lin[0] == '$' and lin[-1] == '$':
                    if lin.count('$') == 2:
                        continue
                if lin[0] == '$' and lin[-1] != '$':
                    if lin.count('$') == 1:

                        file_code_Not_Comment_and_pass.close()
                        print(
                            "Program  is Finch \n Pleas Fallowed Me For Instagram \n @ddos_attack_co")
                        exit()

                # lin.split() -->  text -> list
                list_pass = lin.split()
                for com in list_pass:
                    lin_x = com
                    if lin_x[0] == '$' and lin_x[-1] == '$':
                        continue
                    else:
                        word = chang_text(fun_rm(com))
                        file_code_Not_Comment_and_pass.write(word)
                        file_code_Not_Comment_and_pass.write(" ")
                file_code_Not_Comment_and_pass.write("\n")
            file_code_Not_Comment_and_pass.close()
            file.close()
            # run()

        # --------------------------------------
        # تحليل الكود

        def num_str(word, x):
            list_num = []
            text = word[x:]
            if text[0] in "+-":
                list_num.append(text[0])
                text = word[x+1:]
            for com in text:
                if com in "0123456789.":
                    list_num.append(com)
                else:
                    return "".join(list_num)
            return "".join(list_num)

        def car_str(word, x):
            list_num = []
            text = word[x:]
            for com in text:
                if com in "ABCDEFGHIJKLMNOPQRSTYVUWXYZabcdefghijklmnopqrstxuyvwzy123456789_":
                    list_num.append(com)
                else:
                    return "".join(list_num)
            return "".join(list_num)
        tp_4_chain = []

        def Tp_3(text):
            if file_path == "":
                messagebox.showerror(
                    "ERROR!", "you can't Analyses the Code Save the Text first then Run it")
            else:

                tp = []
                list_text = text.split()
                # tp_4_chain = []
                for word in list_text:
                    x = 0
                    while x < len(word):
                        if len(word)-1 < 1:

                            tp.append((word[x])+"#")
                            tp_4_chain.append(word[x])

                            break
                        elif (word[x] in "0123456789."):
                            number = num_str(word, x)
                            for car in number:
                                x += 1
                            tp.append((number)+"#")
                            tp_4_chain.append(number)

                            x -= 1
                        elif (word[x] in "+-" and word[x+1] in "0123456789."):
                            number = num_str(word, x)
                            for car in number:
                                x += 1
                            tp.append((number)+"#")
                            tp_4_chain.append(number)

                            x -= 1
                        elif (word[x] == "+" and word[x+1] == "+" and word[x+2] in "1234567890."):
                            tp.append((word[x])+"#")
                            tp_4_chain.append(word[x])

                            x += 1
                        elif (word[x] == "+" and word[x+1] == "+"):
                            tp.append((word[x]+word[
                                x+1])+'#')
                            tp_4_chain.append(word[x]+word[
                                x+1])
                            x += 2
                        elif (word[x] in "ABCDEFGHIJKLMNOPQRSTYVXUWXYZabcdefghijklmnopqrsxutyvwzy"):
                            number = car_str(word, x)
                            for car in number:
                                x += 1
                            tp.append((number)+"#")
                            tp_4_chain.append(number)
                            x -= 1

                        elif word[x] in "+-*/!=<>" and word[x+1] == "=":
                            tp.append((word[x]+word[
                                x+1])+'#')
                            tp_4_chain.append(word[x]+word[
                                x+1])
                            x += 1
                        else:
                            tp.append((word[x]+"#"))
                            tp_4_chain.append(word[x])
                        x += 1
                return " ".join(tp)

        # --------------------------------------
        def Tp_4(lists):
            identificateur = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
            separateur = [">", "<", ";", ":", "&&", "||", ",", "."]
            intager = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-"]
            floats = ["0", "1", "2", "3", "4", "5",
                    "6", "7", "8", "9", ".", "+", "-"]
            operations = ["=", "*", "/", "+", "-",
                        "!=", ">=", "<=", "==", "--", "++"]
            chiffre = ["(", ")", "{", "}", "[", "]"]

            def vi_int(word):
                for x in word:
                    if x not in intager or word.count("-") > 1 or word.count("+") > 1 or word == "+" or word == "-":
                        return False
                return True

            def vi_separateur(word):
                if word not in separateur:
                    return False
                return True

            def vi_operations(word):

                if word not in operations:
                    return False
                return True

            def vi_chiffre(word):

                if word not in chiffre:
                    return False
                return True

            def vi_float(word):
                for x in word:
                    if x not in floats or lists.count(".") > 1 or lists.count("-") > 1 or lists.count("+") > 1 or lists[0] not in "1234567890+-" or lists[lists.index(".")-1] in "+-":
                        return False
                return True

            def vi_string(lists):
                for x in lists:
                    if x not in identificateur or lists[0] in "1234567890":
                        return False
                return True

            def test_finall(lists):
                if lists.strip() == "_":
                    return f"{lists} is ERROR!!"
                elif vi_int(lists):
                    return f"{lists} is Integer"
                elif vi_operations(lists):
                    return f"{lists} is operations"
                elif vi_float(lists):
                    return f"{lists} is Float"
                elif vi_string(lists):
                    return f"{lists} is identificateur"
                elif vi_separateur(lists):
                    return f"{lists} is separateur"
                elif vi_chiffre(lists):
                    return f"{lists} is chiffre"
                else:
                    return f"{lists} is ERROR!!"
            return test_finall(lists)

        def run_Tp_4():
            codes = ""
            final = []
            file = open("file_code_not_comment_and_pass.txt")

            for n in tp_4_chain:
                final.append((Tp_4(n.strip())+'\n'))
            for x in final:
                codes += x
            # code_s = Tp_3(file.read().strip())
            lab_run.config(text=(codes))
            lab_run.place(x=3, y=0)
            tp_4_chain.clear()
            file.close()

        def run_tp_3():
            Tp_2()
            codes = ""
            final = []
            file = open("file_code_not_comment_and_pass.txt", "r")
            for x in file.readlines():
                final.append((Tp_3(x)+'\n'))
            for x in final:

                codes += x
            # code_s = Tp_3(file.read().strip())
            # lab_run = Label()
            lab_run3.config(text=(codes))
            lab_run3.place(x=3, y=0)
            file.close()
        # --------------------------------------


        # --------------------------------------
        # حقول الكاتبه
        Writ_Code = Text(root, width=55, height=32)
        Writ_Code.place(x=7, y=4)
        # --------------------------------------
        # انشاء شريط المعلومات
        main_Of = Menu(root)
        # اظافه مصفوف للشريط
        # --------------------------------------
        o_file = Menu(main_Of,  tearoff=0)
        o_file.add_command(label="Open", command=open_file)
        o_file.add_separator()
        o_file.add_command(label="Save", command=Save)
        o_file.add_separator()
        o_file.add_command(label="Save As", command=Save_As)
        o_file.add_separator()
        o_file.add_command(label="Exit", command=root.quit)
        main_Of.add_cascade(label="file", menu=o_file)
        # --------------------------------------

        o_analyses = Menu(main_Of, tearoff=0)
        o_analyses.add_command(label="Lexical", command=Tp_2)
        o_analyses.add_separator()
        o_analyses.add_command(label="Syntaxique", command=run_tp_3)
        main_Of.add_cascade(label="Analyses", menu=o_analyses)
        # --------------------------------------
        root.config(menu=main_Of)
        # --------------------------------------
        # مركز طباعه الحل
        fr1 = Frame(root, background='#212121', width=492, height=250)
        fr1.place(x=500, y=4)
        # مركز analyses الحل
        fr2 = Frame(root, background='#212121', width=492, height=250)
        fr2.place(x=500, y=300)

        lab_run = Label(fr2, bg="#212121", fg='white')
        lab_run3 = Label(fr1, bg="#212121", fg='white')
        # lab_run.place(x=3, y=0)
        # الازرار
        # الزر لحذف النص

        def sup_txt():
            Writ_Code.delete('1.0', END)

        btn_sup = Button(root, text="Supreme", font=(
            'Courier', 15), fg='#bdbdbd', bg='red', width=15, command=sup_txt)
        btn_sup.place(x=7, y=530)

        # الزر البدا
        bt_run = Button(root, text="RUN", font=('Courier', 15),
                        fg='#bdbdbd', bg='green', width=15, command=run_tp_3)
        bt_run.place(x=210, y=530)
        # الزر التحليل
        bt_ana = Button(root, text="Analyses", font=('Courier', 15),
                        fg='#bdbdbd', bg='#34495E', width=15, command=run_Tp_4)
        bt_ana.place(x=650, y=255)

        root.mainloop()


    def but_Main():
        btn4 = Button(scr0, text="Exit", font=("Times Naw Roman", 20, "underline"),
                    bg='Black', command=scr0.quit, width=10, fg="#bdbdbd", cursor='cross')
        btn4.place(x=690, y=4)
    # -----------------------------------------------------------------


    def Team():
        fr3 = Frame(scr0, background="#bdbdbd", width="860", height='500')
        fr3.place(x=0, y=0)
        # lab1 = Label(scr0,text="Show Team ",font=('Courier',15) , fg="White" , bg = "Black",width=500)
        # lab1.place(x=0,y=0)
        lb_0 = Label(scr0, text="L3 Gr3 B", font=(
            "Times Naw Roman", 20, "underline"), bg='#bdbdbd')
        lb_0.pack()
        lb_0 = Label(scr0, text="Team :", font=(
            "Times Naw Roman", 20, "underline"), bg='#bdbdbd')
        lb_0.place(x=10, y=100)
        lb_0 = Label(scr0, text="Lecheheb Djaafar", font=(
            "Times Naw Roman", 20, "underline"), bg='#bdbdbd')
        lb_0.place(x=30, y=140)
        lb_0 = Label(scr0, text="bebboukha Safa", font=(
            "Times Naw Roman", 20, "underline"), bg='#bdbdbd')
        lb_0.place(x=30, y=210)
        lb_0 = Label(scr0, text="benmoussa ahmed redouane", font=(
            "Times Naw Roman", 20, "underline"), bg='#bdbdbd')
        lb_0.place(x=30, y=290)
        but_Main()


    # -----------------------------------------------------------------

    # -----------------------------------------------------------------
    photo = PhotoImage(file="BG_COM.png")
    Edit_Photo = photo.subsample(3, 3)
    show_photo = Label(scr0, image=Edit_Photo)
    show_photo.place(x=340, y=100)
    lb_0 = Label(scr0, text="Welcome to the initiation of practical work",
                font=("Times Naw Roman", 20, "underline"), bg='#bdbdbd')
    lb_0.pack()
    lb_1 = Label(scr0, text="TP_COMPIL", font=(
        "Times Naw Roman", 20, "underline"), bg='#bdbdbd')
    lb_1.pack()
    # -----

    # -----------------------------------------------------------------
    # Button main
    # -----------------------------------------------------------------
    btn1 = Button(scr0, text="Start", font=("Times Naw Roman", 20,
                "underline"), bg='#bdbdbd', width=10, command=root, cursor='trek')
    btn1.place(x=20, y=180)
    btn2 = Button(scr0, text="Team", font=("Times Naw Roman", 20,
                "underline"), bg='#bdbdbd', width=10, command=Team, cursor='heart')
    btn2.place(x=20, y=260)
    btn3 = Button(scr0, text="Exit", font=("Times Naw Roman", 20,
                "underline"), bg='#bdbdbd', command=scr0.quit, width=10, cursor='cross')
    btn3.place(x=20, y=340)
    # -----------------------------------------------------------------


    scr0.mainloop()

print(termcolor.colored(pyfiglet.figlet_format("DDOS_ATTACK_CO"), color="red"))

print(" Go to my Instagram account < @ddos_attack_co > and Fallowed Me \n Enter...", end="")
enter = input("")

main()