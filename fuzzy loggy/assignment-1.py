import numpy as np

# --- Mathematical Logic Functions ---
def get_tri(x, a, b, c):
    """Calculates triangular membership [cite: 127]"""
    return max(0, min((x - a) / (b - a) if b != a else 1, (c - x) / (c - b) if c != b else 1))

def get_trap(x, a, b, c, d):
    """Calculates trapezoidal membership [cite: 136]"""
    return max(0, min((x - a) / (b - a) if b != a else 1, 1, (d - x) / (d - c) if d != c else 1))

def compute_washing_logic(stain_val, load_val):
    # 1. FUZZIFICATION [cite: 104, 185]
    # Stain Density (0-100) [cite: 26, 30]
    s_light = get_trap(stain_val, 0, 0, 25, 45)
    s_mod   = get_tri(stain_val, 35, 50, 65)
    s_heavy = get_trap(stain_val, 55, 75, 100, 100)

    # Fabric Weight / Load (0-10) [cite: 27, 53]
    l_small = get_trap(load_val, 0, 0, 2, 4)
    l_std   = get_tri(load_val, 3, 5, 7)
    l_bulk  = get_trap(load_val, 6, 8, 10, 10)

    # 2. RULE EVALUATION (Mamdani AND-min) [cite: 103, 192]
    r1 = min(s_light, l_small)  # Brief
    r2 = min(s_light, l_std)    # Brief
    r3 = min(s_light, l_bulk)   # Normal
    r4 = min(s_mod, l_small)    # Normal
    r5 = min(s_mod, l_std)      # Normal
    r6 = min(s_mod, l_bulk)     # Extended
    r7 = min(s_heavy, l_small)  # Extended
    r8 = min(s_heavy, l_std)    # Extended
    r9 = min(s_heavy, l_bulk)   # Extended

    # 3. AGGREGATION & DEFUZZIFICATION (Centroid Method) [cite: 112, 220]
    numerator = 0
    denominator = 0
    
    # Universe of discourse: 0 to 60 minutes [cite: 28, 118]
    for t in range(0, 61):  
        # Output Clipping (MAX of associated rules)
        brief_clip    = max(r1, r2)
        normal_clip   = max(r3, r4, r5)
        extended_clip = max(r6, r7, r8, r9)
        
        # Combine with output membership shapes [cite: 174, 181, 182]
        m_brief = min(brief_clip, get_trap(t, 0, 0, 15, 25))
        m_norm  = min(normal_clip, get_tri(t, 20, 35, 50))
        m_ext   = min(extended_clip, get_trap(t, 45, 55, 60, 60))
        
        # Aggregate with MAX [cite: 237]
        agg_score = max(m_brief, m_norm, m_ext)
        
        numerator += t * agg_score
        denominator += agg_score

    # Final Crisp Value calculation [cite: 115, 242]
    return numerator / denominator if denominator != 0 else 0

# --- Simulation results ---
# Using the test case format from your Restaurant Tipping code
test_scenarios = [(15, 2), (50, 5), (85, 9), (30, 8), (75, 2)]
print("--- Washing Machine Controller Simulation ---")
for s, l in test_scenarios:
    print(f"Stain: {s}%, Load: {l}/10 -> Cycle Time: {compute_washing_logic(s, l):.2f} minutes")