from pulp import LpMaximize, LpProblem, LpVariable, value, LpStatus, PULP_CBC_CMD

def optimize_production(water_limit, sugar_limit, lemon_juice_limit, fruit_puree_limit):
    model = LpProblem("Maximize_Production", LpMaximize)

    lemonade = LpVariable('lemonade', lowBound=0, cat='Integer')
    fruit_juice = LpVariable('fruit_juice', lowBound=0, cat='Integer')

    model += lemonade + fruit_juice, "Total_Products"

    # limits
    model += 2 * lemonade + 1 * fruit_juice <= water_limit, "Water_limit"
    model += 1 * lemonade <= sugar_limit, "Sugar_limit"
    model += 1 * lemonade <= lemon_juice_limit, "Lemon_juice_limit"
    model += 2 * fruit_juice <= fruit_puree_limit, "Fruit_puree_limit"

    solver = PULP_CBC_CMD(msg=False)
    model.solve(solver)

    return {
        "Статус": LpStatus[model.status],
        "Кількість лимонаду": lemonade.varValue,
        "Кількість фруктового соку": fruit_juice.varValue,
        "Максимальна загальна кількість продуктів": value(model.objective)
    }

# set limits
results = optimize_production(
    water_limit=100,
    sugar_limit=50,
    lemon_juice_limit=30,
    fruit_puree_limit=40
)

# output
for key, val in results.items():
    print(f"{key}: {val}")
