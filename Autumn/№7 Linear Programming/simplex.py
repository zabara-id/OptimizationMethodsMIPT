from pyomo.environ import *

# Создаем модель
model = ConcreteModel()

# Определяем переменные
model.x_1 = Var(within=NonNegativeReals)
model.x_2 = Var(within=NonNegativeReals)
model.x_3 = Var(within=NonNegativeReals)

# Определяем ограничения
model.Constraint1 = Constraint(expr=2*model.x_1 - model.x_2 + 2*model.x_3 <= 9)
model.Constraint2 = Constraint(expr=3*model.x_1 + 5*model.x_2 + 4*model.x_3 <= 8)
model.Constraint3 = Constraint(expr=model.x_1 + model.x_2 + 2*model.x_3 <= 2)

# Определяем целевую функцию
model.obj = Objective(expr=-4*model.x_1 - 5*model.x_2 - 4*model.x_3, sense=minimize)

# Решаем задачу
solver = SolverFactory('glpk')
model.dual = Suffix(direction=Suffix.IMPORT)
solver.solve(model)

# Выводим результаты
print("Значение целевой функции =", model.obj())
print("x_1 =", model.x_1())
print("x_2 =", model.x_2())
print("x_3 =", model.x_3())

# Выводим двойственные значения
print("Двойственные значения:")
for c in model.component_objects(Constraint, active=True):
    for index in c:
        print(c, ":",  model.dual[c[index]])