class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1<= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self): # метод для вывода количества этажей в здании
        return self.number_of_floors

    def __str__(self): # метод для вывода информации о здании
        return f'Название : {self.name}, количество этажей : {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)



if __name__ == '__main__':
    print(h1)
    print(h2)


    print(len(h1)) # выводит количество этажей в здании
    print(len(h2)) # выводит количество этажей в здании

