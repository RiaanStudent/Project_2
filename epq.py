import math

# === Inputs ===
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
epq = calculate_epq(annual_demand,setup_cost,holding_cost,daily_demand_rate,daily_production_rate)
# === Runs per year ===
runs_per_year = annual_demand/epq
# === Run lenght ===
run_length_days = epq/daily_production_rate
# === Max inventory level ===
max_inventory = epq*(1-daily_demand_rate/daily_production_rate)

# === Print ===
print("Optimal production quantity: "   , round(epq,2))
print("Production runs per year: "      , round(runs_per_year,2))
print("Length of each run (days): "     , round(run_length_days,1))
print("Maximum inventory level: "       , round(max_inventory,2))