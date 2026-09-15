import math
# Created by Riaan Coetzee u23525283
# === Explanation ===
"""
Economic Production Quantity (EPQ) is a mathematical model that is used 
if you are the manufacturer and seller of a product. It detrimines the 
optimal production quantity by incorporating the daily demand and daily 
production.
"""
# --------------------------------------------------------------------

# === Origional Inputs ===
annual_demand =         12000   # units per year
setup_cost =            50      # cost per production run, in Rand
holding_cost =          2       # cost per unit per year, in Rand
daily_demand_rate =     40      # units produced/sold per day
daily_production_rate = 100     # units your process can make per day
# -------------------------------------------------------------------

# === EPQ function ===
def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2*demand*setup)/(hold_cost*(1-d_rate/p_rate)))

# === EPQ ===
epq = calculate_epq(annual_demand,setup_cost,holding_cost,daily_demand_rate,
                    daily_production_rate)
# === Runs per year ===
runs_per_year = annual_demand/epq
# === Run lenght ===
run_length_days = epq/daily_production_rate
# === Max inventory level ===
max_inventory = epq*(1-daily_demand_rate/daily_production_rate)

# === Print ===
message = f"""Origional:
Optimal production quantity: {round(epq,2)}
Production runs per year: {round(runs_per_year,2)}
Length of each run (days): {round(run_length_days,1)}
Maximum inventory level: {round(max_inventory,2)}
"""
print(message)

# === Question 1 Inputs ===
annual_demand =         12000   # units per year
setup_cost =            50      # cost per production run, in Rand
holding_cost =          2       # cost per unit per year, in Rand
daily_demand_rate =     40      # units produced/sold per day
daily_production_rate = 150     # units your process can make per day
# -------------------------------------------------------------------

# === EPQ ===
epq = calculate_epq(annual_demand,setup_cost,holding_cost,daily_demand_rate,
                    daily_production_rate)
# === Runs per year ===
runs_per_year = annual_demand/epq
# === Run lenght ===
run_length_days = epq/daily_production_rate
# === Max inventory level ===
max_inventory = epq*(1-daily_demand_rate/daily_production_rate)

# === Print ===
message = f"""Question 1:
Optimal production quantity: {round(epq,2)}
Production runs per year: {round(runs_per_year,2)}
Length of each run (days): {round(run_length_days,1)}
Maximum inventory level: {round(max_inventory,2)}
"""
print(message)
print("""The production quantity goes down as compared to the origional 
because of the increased production rate.

This makes sence because the EPQ model balances setup cost and inventory 
handling cost, so when the machine operates faster, it impacts the way 
inventory is accumulated. It makes more sence to run the new machine for 
multiple shorter runs to minimise the costs due to inventory.
""")

# === Question 2 Inputs ===
annual_demand =         12000   # units per year
setup_cost =            50      # cost per production run, in Rand
holding_cost =          2       # cost per unit per year, in Rand
daily_demand_rate =     40      # units produced/sold per day
daily_production_rate = 100000  # units your process can make per day
# -------------------------------------------------------------------

# === EPQ ===
epq = calculate_epq(annual_demand,setup_cost,holding_cost,daily_demand_rate,
                    daily_production_rate)
# === Runs per year ===
runs_per_year = annual_demand/epq
# === Run lenght ===
run_length_days = epq/daily_production_rate
# === Max inventory level ===
max_inventory = epq*(1-daily_demand_rate/daily_production_rate)

# === Print ===
message = f"""Question 2:
Optimal production quantity: {round(epq,2)}
Production runs per year: {round(runs_per_year,2)}
Length of each run (days): {round(run_length_days,1)}
Maximum inventory level: {round(max_inventory,2)}
"""
print(message)
print("""Mathematically as p->infinity then 1-d/p -> 1-0=1 which means that 
the EPQ formula bedomes the EOQ formula.

In other terms it means that if p becomes to big it follows exactly like the 
EOQ because the amount needed can instantly be produced.
""")