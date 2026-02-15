import numpy as np

# --- Mathematical Logic Functions ---
def get_tri(x, a, b, c):
    return max(0, min((x - a) / (b - a) if b != a else 1, (c - x) / (c - b) if c != b else 1))

def get_trap(x, a, b, c, d):
    return max(0, min((x - a) / (b - a) if b != a else 1, 1, (d - x) / (d - c) if d != c else 1))

def compute_tip_system(service_score, food_score):
    # 1. FUZZIFICATION
    s_poor = get_trap(service_score, 0, 0, 2, 4)
    s_avg  = get_tri(service_score, 3, 5, 7)
    s_exc  = get_trap(service_score, 6, 8, 10, 10)

    f_bad = get_trap(food_score, 0, 0, 3, 6)
    f_del = get_trap(food_score, 5, 8, 10, 10)

    # 2. RULE EVALUATION (Mamdani OR-max logic)
    r1_strength = max(s_poor, f_bad) # Cheap
    r2_strength = s_avg              # Average
    r3_strength = max(s_exc, f_del)  # Generous

    # 3. AGGREGATION & DEFUZZIFICATION (Centroid)
    num, den = 0, 0
    # Evaluate across tip range 5% to 30%
    for t in np.linspace(5, 30, 100):
        # Clipping membership shapes
        m_cheap = min(r1_strength, get_trap(t, 5, 5, 10, 15))
        m_avg   = min(r2_strength, get_tri(t, 12, 18, 24))
        m_gen   = min(r3_strength, get_trap(t, 20, 25, 30, 30))
        
        # Aggregate with MAX
        agg_val = max(m_cheap, m_avg, m_gen)
        num += t * agg_val
        den += agg_val

    return num / den if den != 0 else 17.5

# --- Simulation results ---
test_scenarios = [(2, 2), (5, 5), (9, 9), (8, 3), (4, 9)]
print("--- Restaurant Tipping Simulation ---")
for s, f in test_scenarios:
    print(f"Service: {s}/10, Food: {f}/10 -> Tip: {compute_tip_system(s, f):.2f}%")