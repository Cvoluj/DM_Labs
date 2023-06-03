from tkinter import *


## Константи
font = ["Helvetica", 10, "bold"]
font2 = ["Calibri", 10]
background = "#ffffff"
buttonHeight = 2
buttonWidth = 16
rect_size = 27
edges = []
matrix_of_sum = []
filename1 = 'PIB.txt'
n_string = 'n'
m = None
n = None
created_mn = ''
def save_file(filename):
    name = NameEntry.get()
    surname = SurnameEntry.get()
    familia = FamiliaEntry.get()
    with open(filename, 'w') as writer:
        writer.write(name+' ')
        writer.write(surname+' ')
        writer.write(familia+' ')


def read_file(filename):
    with open(filename) as reader:
        fullname = reader.readline()
    fullnamelist = fullname.split()
    NameEntry.delete(0, END)
    SurnameEntry.delete(0, END)
    FamiliaEntry.delete(0, END)
    NameEntry.insert(0, fullnamelist[0])
    SurnameEntry.insert(0, fullnamelist[1])
    FamiliaEntry.insert(0, fullnamelist[2])


def calc(m):
    global n_string
    no_repeat_name = []
    name = NameEntry.get()+' '+SurnameEntry.get()+' '+FamiliaEntry.get()
    names = name.split()

    for parts in names:
        for letter in parts:
            if letter not in no_repeat_name:
                no_repeat_name.append(letter)

    no_repeat_name.sort(reverse=True)  # Сортуємо символи у зворотньому алфавітному порядку
    n = len(no_repeat_name)
    n_string = str(n)
    update(n_and_mEntry, n_and_mLabel, no_repeat_name)
    if n_and_mEntry.get() != '':
        m = int(n_and_mEntry.get())

        def generate_subsets(n, m):
            subsets = []
            for i in range(1 << n):
                binary = bin(i)[2:].zfill(n)  # Перетворюємо число на двійковий вектор
                count_ones = binary.count('1')
                if count_ones <= m:
                    subset = [no_repeat_name[j] for j in range(n) if binary[j] == '1']
                    subsets.append(subset)

            subsets.sort(key=lambda x: (-len(x), x),
                         reverse=True)  # Сортуємо підмножини у антилексикографічному порядку

            return subsets

        result = generate_subsets(n, m)

        for subset in result:
            AList.insert(END, ''.join(subset))


def update(entry, label, name):
    created_mn = 'Утворена множина:\n{0!s}\n\n'.format(''.join(name))
    entry.configure(state=NORMAL)
    label.configure(text="{0!s}Увведіть значення для m від 1 до {1!s}".format(created_mn, n_string))


win = Tk()
win.title('lab5')
win.geometry('530x450')

myInfo = LabelFrame(win, text='Інформація про студента', font=font, labelanchor='n')
PIBEntry_Label = LabelFrame(win)
infoText = Label(myInfo, text="Бережанський\nДанііл\nВадимович\nГрупа - ІО-24, номер - 1\n(2401 % 26) + 1 = {0!s}".format((2401 % 26) + 1),
                 font=("Helvetica", 13), justify=LEFT)
infoText.grid(row=0, column=0, padx=10, sticky="nsew")
myInfo.grid(row=0, column=0, padx=20, pady=10, sticky="we")
PIBEntry_Label.grid(row=0, column=1, padx=20, pady=10, sticky="we", columnspan=2)
EnterPibLabel = Label(PIBEntry_Label, text="Введіть своє П.І.Б:", font=font)
EnterPibLabel.grid(column=0, row=0, padx=10, pady=10, sticky="we", columnspan=2)
NameEntry = Entry(PIBEntry_Label, width=18, bd=1, font=font2)
SurnameEntry = Entry(PIBEntry_Label, width=18, bd=1, font=font2)
FamiliaEntry = Entry(PIBEntry_Label, width=18, bd=1, font=font2)
SaveButton = Button(PIBEntry_Label, text="Зберегти", command=lambda: save_file(filename1))
ReadButton = Button(PIBEntry_Label, text="Зчитати з файлу", command= lambda: read_file(filename1))
n_and_mLabel = Label(PIBEntry_Label, text="{0!s}Увведіть значення для m від 1 до {1!s}".format(created_mn, n_string))
n_and_mEntry = Entry(PIBEntry_Label, state=DISABLED)

CalcButton = Button(PIBEntry_Label, text="Запустити алгоритм", command= lambda: calc(m))


NameEntry.grid(row=1, column=0, sticky="we", padx=3, pady=1, columnspan=2)
SurnameEntry.grid(row=2, column=0, sticky="we", padx=3, pady=1, columnspan=2)
FamiliaEntry.grid(row=3, column=0, sticky="we", padx=3, pady=1, columnspan=2)
SaveButton.grid(row=4, column=0, sticky="we", padx=3, pady=1)
ReadButton.grid(row=4, column=1, sticky="we", padx=3, pady=1)
n_and_mLabel.grid(row=5, columnspan=2, column=0, sticky="we", pady=1, padx=3)
n_and_mEntry.grid(row=6, column=0, columnspan=2, sticky="we", pady=1, padx=3)
CalcButton.grid(row=7, column=0, columnspan=2, sticky="we", padx=3, pady=1)


ListLabel = LabelFrame(win, text="Згенеровані підмножини", font=font, labelanchor='n')
ListLabel.grid(row=1, columnspan=3, column=0, sticky="nswe", padx=4,pady=4)
ListLabel.grid_rowconfigure(0, weight=1)
ListLabel.grid_columnconfigure(0, weight=1)

AScroll = Scrollbar(ListLabel)
AList = Listbox(ListLabel, font=font2)
AScroll.config(command=AList.yview)
AList.config(yscrollcommand=AScroll.set, selectmode="none")
AList.grid(row=1, column=0, sticky="NSEW")
AScroll.grid(row=1, column=1, sticky="ns", padx=(0, 5))


win.mainloop()
