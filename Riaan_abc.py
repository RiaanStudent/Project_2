# Created by Riaan Coetzee u23525283
# === Explanation ===
"""This code is for classifing items into A, B and C tiers to 
better define the most important items to keep a focus on, 
based on 80%, 15%, and 5% contibution to total sales"""
# --------------------------------------------------------------------

# === Origional Input === 
skus = [
    {"sku": "BRK-100",  "demand": 2000,   "cost": 45},
    {"sku": "GSK-220",  "demand": 1500,   "cost": 30},
    {"sku": "BLT-010",  "demand": 10000,  "cost": 2},
    {"sku": "BRG-330",  "demand": 800,    "cost": 60},
    {"sku": "SEAL-500", "demand": 3000,   "cost": 5},
    {"sku": "MTR-700",  "demand": 50,     "cost": 800},
    {"sku": "WSH-050",  "demand": 20000,  "cost": 0.5},
    {"sku": "CBL-900",  "demand": 400,    "cost": 25},
]
# ----------------------------------------------------------

# === Vale function ===
def usage_value(demand, cost):
    return demand*cost

# === Tier assignment function ===
def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"

# Calculating value
for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

# Sorting skus
skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

# Calculating cumulative percentage
total_value = sum(item["value"] for item in skus_sorted)
running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total/total_value)*100

# Assigning tiers
for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])

# Counting tiers
tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1

# === Print ===
print(f"{'Origional':^50}")
for item in skus_sorted:
    print(f"{item["sku"]:<9}| value: {item["value"]:<7}| cum %: {round(item["cum_pct"], 1):<5}| tier: {item["tier"]:<1} |")

print(f"\nTier Counts\nA: {tier_counts["A"]}\nB: {tier_counts['B']}\nC: {tier_counts['C']}")

# === Question 1 Input === 
skus = [
    {"sku": "BRK-100",  "demand": 2000,   "cost": 45},
    {"sku": "GSK-220",  "demand": 1500,   "cost": 30},
    {"sku": "BLT-010",  "demand": 10000,  "cost": 2},
    {"sku": "BRG-330",  "demand": 800,    "cost": 60},
    {"sku": "SEAL-500", "demand": 3000,   "cost": 5},
    {"sku": "MTR-700",  "demand": 50,     "cost": 800},
    {"sku": "WSH-050",  "demand": 20000,  "cost": 0.5},
    {"sku": "CBL-900",  "demand": 400,    "cost": 25},
    {"sku": "DRB-445",  "demand": 1000,   "cost": 19},
    {"sku": "RIA-911",  "demand": 3500,   "cost": 67},
]
# ----------------------------------------------------------

# === Vale function ===
def usage_value(demand, cost):
    return demand*cost

# === Tier assignment function ===
def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"

# Calculating value
for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

# Sorting skus
skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

# Calculating cumulative percentage
total_value = sum(item["value"] for item in skus_sorted)
running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total/total_value)*100

# Assigning tiers
for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])

# Counting tiers
tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1

# === Print ===
print(f"{'Question 1':^50}")
for item in skus_sorted:
    print(f"{item["sku"]:<9}| value: {item["value"]:<7}| cum %: {round(item["cum_pct"], 1):<5}| tier: {item["tier"]:<1} |")

print(f"\nTier Counts\nA: {tier_counts["A"]}\nB: {tier_counts['B']}\nC: {tier_counts['C']}")
print(f"\nNo the split does not change much\n")
# === Question 2 Input === 
skus = [
    {"sku": "BRK-100",  "demand": 2000,   "cost": 45},
    {"sku": "GSK-220",  "demand": 1500,   "cost": 30},
    {"sku": "BLT-010",  "demand": 10000,  "cost": 2},
    {"sku": "BRG-330",  "demand": 800,    "cost": 60},
    {"sku": "SEAL-500", "demand": 3000,   "cost": 5},
    {"sku": "MTR-700",  "demand": 50,     "cost": 800},
    {"sku": "WSH-050",  "demand": 20000,  "cost": 0.5},
    {"sku": "CBL-900",  "demand": 400,    "cost": 25},
]
# ----------------------------------------------------------

# === Tier assignment function ===
def assign_tier(cum_pct):
    if cum_pct <= 70:
        return "A"
    elif cum_pct <= 90:
        return "B"
    else:
        return "C"

# === Vale function ===
def usage_value(demand, cost):
    return demand*cost

# === Tier assignment function ===
def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"

# Calculating value
for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

# Sorting skus
skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

# Calculating cumulative percentage
total_value = sum(item["value"] for item in skus_sorted)
running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total/total_value)*100

# Assigning tiers
for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])

# Counting tiers
tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1

# === Print ===
print(f"{'Question 2':^50}")
for item in skus_sorted:
    print(f"{item["sku"]:<9}| value: {item["value"]:<7}| cum %: {round(item["cum_pct"], 1):<5}| tier: {item["tier"]:<1} |")

print(f"\nTier Counts\nA: {tier_counts["A"]}\nB: {tier_counts['B']}\nC: {tier_counts['C']}")
print(f"\nMore items gets classified as A and B\n")
# === Origional Input === 
skus = [
    {"sku": "BRK-100",  "demand": 2000,   "cost": 45},
    {"sku": "GSK-220",  "demand": 1500,   "cost": 30},
    {"sku": "BLT-010",  "demand": 10000,  "cost": 2},
    {"sku": "BRG-330",  "demand": 800,    "cost": 60},
    {"sku": "SEAL-500", "demand": 3000,   "cost": 5},
    {"sku": "MTR-700",  "demand": 50,     "cost": 800},
    {"sku": "WSH-050",  "demand": 20000,  "cost": 0.5},
    {"sku": "CBL-900",  "demand": 400,    "cost": 25},
]
# ----------------------------------------------------------

# === Classify function ===
def classify_inventory(skus):
    # Calculating value
    for item in skus:
        item["value"] = item["demand"]*item["cost"]

    # Sort skus
    skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

    # Calculating cumulative percentage
    total_value = sum(item["value"] for item in skus_sorted)
    running_total = 0
    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total/total_value)*100

    # Assigning tiers
    for item in skus_sorted:
        if item["cum_pct"] <= 80:
            item["tier"] = "A"
        elif item["cum_pct"] <= 95:
            item["tier"] = "B"
        else:
            item["tier"] = "C"

    # Output string
    message = f""
    for item in skus_sorted:
        message = message + f"{item["sku"]:<9}| value: {item["value"]:<7}| cum %: {round(item["cum_pct"], 1):<5}| tier: {item["tier"]:<1} |\n"
    return message

print(f"\n{'Question 3':^50}")
print(classify_inventory(skus))
# Counting tiers
tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1

# # === Print ===
print(f"Tier Counts\nA: {tier_counts["A"]}\nB: {tier_counts['B']}\nC: {tier_counts['C']}")
