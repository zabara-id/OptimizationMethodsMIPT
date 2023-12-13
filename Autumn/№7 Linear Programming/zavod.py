from pyomo.environ import *

model3 = ConcreteModel()

model3.y1 = Var(within=NonNegativeReals)
model3.y2 = Var(within=NonNegativeReals)
model3.y3 = Var(within=NonNegativeReals)

model3.prod1 = Constraint(expr = model3.y1<= 5000*6)
model3.prod2 = Constraint(expr = model3.y2<= 4000*6)
model3.prod3 = Constraint(expr = model3.y3<= 2000*6)
model3.storage = Constraint(expr = 30*model3.y1/1000 + 50*model3.y2/1000 + 220*model3.y3/1000 <= 2500)  # расширили объём места хранения до 2500
model3.min_headphone = Constraint(expr = -model3.y1 <= -4500)
model3.min_laptop = Constraint(expr = -model3.y3 <= -3000)
model3.max_headphone = Constraint(expr = model3.y1 <= 10000)
model3.max_phone = Constraint(expr = model3.y2 <= 14000)
model3.max_laptop = Constraint(expr = model3.y3 <= 7000)

model3.profit = Objective(expr = 5*model3.y1 + 7*model3.y2 + 12*model3.y3, sense=maximize)

solver = SolverFactory('glpk')
model3.dual = Suffix(direction=Suffix.IMPORT)
solver.solve(model3)

print("Values of y1, y2 and y3: ", model3.y1(), model3.y2(), model3.y3())
print("Максимальная прибыль с расшренным складом: ", model3.profit())
      
# solver = SolverFactory('glpk')
# model2.dual = Suffix(direction=Suffix.IMPORT)  # создаём суффикс объекта для хранения двойственых переменных
# solver.solve(model2)  # ещё раз прогоняем решение

# # выводим двойственные значения
# print("Оптимальное решение двойственной задачи для каждого из ограничений")
# for c in model2.component_objects(Constraint, active=True):
#     for index in c:
#         print(c, ": lambda = ",  model2.dual[c[index]])