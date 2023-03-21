from tkinter import *
def ownunite(canvas1, first, second, WifeHusband, MotherInlaw, dick1, dick2):
    canvas1.delete("all")
    for i in range(len(first)):
        canvas1.create_text(30 + i * 74, 25, text=str(first[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 32], [35 + i * 74, 42], fill="black")
        dick1.update({first[i]: [30 + i * 74, 37]})
    for i in range(len(second)):
        canvas1.create_text(30 + i * 74, 175, text=str(second[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 158], [35 + i * 74, 168], fill="black")
        dick2.update({second[i]: [30 + i * 74, 163]})
    union = set(WifeHusband).union(set(MotherInlaw))
    for i in union:
        canvas1.create_line(dick1[i[0]], dick2[i[1]], arrow=LAST)
    canvas1.grid(row=2, column=0, columnspan=5)


def ownintersect(canvas1, first, second, WifeHusband, MotherInlaw, dick1, dick2):
    canvas1.delete("all")
    for i in range(len(first)):
        canvas1.create_text(30 + i * 74, 25, text=str(first[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 32], [35 + i * 74, 42], fill="black")
        dick1.update({first[i]: [30 + i * 74, 37]})
    for i in range(len(second)):
        canvas1.create_text(30 + i * 74, 175, text=str(second[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 158], [35 + i * 74, 168], fill="black")
        dick2.update({second[i]: [30 + i * 74, 163]})
    intersection = set(WifeHusband).intersection(set(MotherInlaw))
    for i in intersection:
        canvas1.create_line(dick1[i[0]], dick2[i[1]], arrow=LAST)
    canvas1.grid(row=2, column=0, columnspan=5)


def owndiff(canvas1, first, second, WifeHusband, MotherInlaw, dick1, dick2):
    canvas1.delete("all")
    for i in range(len(first)):
        canvas1.create_text(30 + i * 74, 25, text=str(first[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 32], [35 + i * 74, 42], fill="black")
        dick1.update({first[i]: [30 + i * 74, 37]})
    for i in range(len(second)):
        canvas1.create_text(30 + i * 74, 175, text=str(second[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 158], [35 + i * 74, 168], fill="black")
        dick2.update({second[i]: [30 + i * 74, 163]})
    difference = set(MotherInlaw).difference(set(WifeHusband))
    for i in difference:
        canvas1.create_line(dick1[i[0]], dick2[i[1]], arrow=LAST)
    canvas1.grid(row=2, column=0, columnspan=5)


def Udifference(canvas1, first, second, WifeHusband, MotherInlaw, dick1, dick2):
    canvas1.delete("all")
    for i in range(len(first)):
        canvas1.create_text(30 + i * 74, 25, text=str(first[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 32], [35 + i * 74, 42], fill="black")
        dick1.update({first[i]: [30 + i * 74, 37]})
    for i in range(len(second)):
        canvas1.create_text(30 + i * 74, 175, text=str(second[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 158], [35 + i * 74, 168], fill="black")
        dick2.update({second[i]: [30 + i * 74, 163]})
    union = set(WifeHusband).union(set(MotherInlaw))
    universaldiffernce = union.difference(set(MotherInlaw))
    for i in universaldiffernce:
        canvas1.create_line(dick1[i[0]], dick2[i[1]], arrow=LAST)
    canvas1.grid(row=2, column=0, columnspan=5)


def inversing(canvas1, first, second, WifeHusband, MotherInlaw, dick1, dick2):
    canvas1.delete("all")
    for i in range(len(first)):
        canvas1.create_text(30 + i * 74, 25, text=str(first[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 32], [35 + i * 74, 42], fill="black")
        dick1.update({first[i]: [30 + i * 74, 37]})
    for i in range(len(second)):
        canvas1.create_text(30 + i * 74, 175, text=str(second[i]), font="Arial 10", anchor=CENTER)
        canvas1.create_oval([25 + i * 74, 158], [35 + i * 74, 168], fill="black")
        dick2.update({second[i]: [30 + i * 74, 163]})
    for i in WifeHusband:
        canvas1.create_line(dick2[i[1]], dick1[i[0]], arrow=LAST)
    canvas1.grid(row=2, column=0, columnspan=5)