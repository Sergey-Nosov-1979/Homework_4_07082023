'''В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой 
грядке, причём кусты высажены только по окружности. Таким образом, у каждого 
куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать 
за один заход собирающий модуль, находясь перед некоторым кустом заданной во 
входном файле грядки.'''


n_bushes = input('Введите количество кустов черники на грядке: N = ')
n_bushes = int(n_bushes)
garden_bed = list()
for i in range(n_bushes):
    berries =input('Введите количество ягод на i кусте: ai = ')
    berries = int(berries)
    garden_bed.append(berries)
garden_bed_count = list()
for i in range(len(garden_bed)):
       garden_bed_count.append(garden_bed[i-2] + garden_bed[i-1] + garden_bed[i])
harvest = max(garden_bed_count)
print("Максимальный собранный урожай за один заход собирающим модулем составляет", harvest, "шт. ягод")
