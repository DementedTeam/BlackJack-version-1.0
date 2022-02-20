import random

#koloda = [6,7,8,9,10,2,3,4,11] * 4
cards =  [6,7,8,9,10,2,3,4,11] * 4

random.shuffle(koloda)

count = 0
#Добавляю цикл while 
while True:
    what  = input('Вы желаете взять карту? y/n\n')
    if what  == 'y':
        current = cards.pop()
        print ('Вам попалась карта достоинстовом %d' %current)
        count += current
        if count > 21:
            print('Извините вы проиграли, до новых встреч')
            break
        
        else:
            print('У вас %d очков.' %count)
            
    elif choice == 'n':
        print('У вас %d очков вы закончили игру.Удачи '%count)
        break
