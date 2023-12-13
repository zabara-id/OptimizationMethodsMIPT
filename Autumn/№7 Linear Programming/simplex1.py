from pyomo.environ import *

# Создаем модель
model = ConcreteModel()

# Определяем переменные
model.x1 = Var(domain=NonNegativeReals)
model.x2 = Var(domain=NonNegativeReals)
model.x3 = Var(domain=NonNegativeReals)

# Определяем целевую функцию
model.obj = Objective(expr = -9*model.x1 - 3*model.x2 - 7*model.x3, sense=minimize)

# Определяем ограничения
model.con1 = Constraint(expr = 2*model.x1 + model.x2 + 3*model.x3 <= 6)
model.con2 = Constraint(expr = 5*model.x1 + 4*model.x2 + model.x3 <= 12)
model.con3 = Constraint(expr = 3*model.x3 <= 1)

# Решаем задачу
solver = SolverFactory('glpk')
solver.solve(model)

# Выводим результаты
print("Значение x1 =", model.x1.value)
print("Значение x2 =", model.x2.value)
print("Значение x3 =", model.x3.value)