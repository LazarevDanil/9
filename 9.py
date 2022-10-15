#Параметры (при изменении все элементы адаптируются)
size = 200
margin = 20

#-------------
from tkinter import *
from tkinter.messagebox import *
import random

#-Окно и поле-
root = Tk()
root.title('Девятьнашки')
stringsize = ""
for i in [str(size*4+margin*2),'x',str(size*3+margin*2)]:    
    stringsize = f'{stringsize+i}'

root.geometry(stringsize)

canvas = Canvas(root,width=3*size+2*margin,height=3*size+2*margin,bg='#fb9e24')
canvas.pack(side=LEFT)

#Cловарь для возможных переходов-
base = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[4,6,8],8:[5,7]}

#-Функция нажатия на цифру-
def swap(event):
    nowx = (event.y-margin)//size
    nowy = (event.x-margin)//size
    #-Отсеиваем нажатия за пределы игрового поля
    if nowx<0 or nowx>3 or nowy<0 or nowy>3:
        pass
    #-------------------------------------------
    number = nowx*3+nowy
    for i in base[number]:
        if order[i] == 0:
            order[number],order[i] = order[i],order[number]
            break
    field()
    #-Проверяем, решена ли головолимка
    if order == [1,2,3,4,5,6,7,8,0]:
                showinfo('УРА!','Задача решена!')

#Функция генерации правильной последовательности для игрового поля
def rand_check():
    answer = []
    allnumbers = [0,1,2,3,4,5,6,7,8]
    for i in range (9):
        now = random.randint(0,len(allnumbers)-1)
        answer.append(allnumbers[now])
        allnumbers.pop(now)
    count = 0
    #Делаем число "беспорядков" четным
    for i in range(len(answer)):
        if answer[i] == 0:
            continue
        for j in range(i,len(answer)):
            if answer[j] == 0:
                continue
            elif answer[i] > answer[j]:
                count += 1
    if count%2 == 1:
        for i in range(8):
            if answer[i]>answer[i+1]:
                answer[i],answer[i+1] = answer[i+1],answer[i]
                break
    #--------------
    return answer


#Заполнение поля
# order = [1,2,3,4,5,7,8,6,0] # для проверки можно вручную задать нужную конфигурацию
order = rand_check()

#Сохраняем поле для возможности переиграть
orderstart = []
for i in range(len(order)):
    orderstart.append(order[i])

#-Функция генерации поля-
nums = []
def field():
 #Очищаем предыдущее поле
    for i in nums:
        canvas.delete(i)
 #------------------------
    for i in range(3):
        for j in range(3):
            x = margin + j*size
            y = margin + i*size
            canvas.create_rectangle(x,y,x+size,y+size,fill='#7f320c')
            if order[i*3+j] == 0:   
                number = canvas.create_text(x+size/2,y+size/2,text=str(order[i*3+j]),
                    fill='#7f320c',font=('Comic Sans MS',size//2))
            else:
                number = canvas.create_text(x+size/2,y+size/2,text=str(order[i*3+j]),
                    fill='#fb9e24',font=('Comic Sans MS',size//2))
            nums.append(number)
field()

#Функция перезапуска игры
def again(event):
    for i in range(len(orderstart)):
        order[i] = orderstart[i]
    field()

#Функция запуска новой игры
def new(event):
    neworder = rand_check()
    for i in range(len(neworder)):
        orderstart[i] = neworder[i]
        order[i] = neworder[i]
    field()

#Кнопки для новой игры и перезапуска

butagain = Button(text='Ещё раз',
               bg='#7f320c', fg='#fb9e24',  # цвет фона и надписи
               activebackground='#7f320c',  # цвет нажатой кнопки
               activeforeground='#f4880b',  # цвет надписи когда кнопка нажата
               font=("Comic Sans MS", size//10))  # шрифт и размер надписи
butagain.pack(side = TOP,expand=1,fill=BOTH)
butagain.bind('<Button-1>', again)

butnew = Button(text=('Новая\nигра'),                 
               bg='#7f320c', fg='#fb9e24',  # цвет фона и надписи
               activebackground='#7f320c',  # цвет нажатой кнопки
               activeforeground='#f4880b',  # цвет надписи когда кнопка нажата
               font=("Comic Sans MS", size//10))  # шрифт и размер надписи
butnew.pack(side = BOTTOM,expand=1,fill=BOTH)
butnew.bind('<Button-1>', new)
#------------

canvas.bind('<Button-1>',swap)
root.mainloop()