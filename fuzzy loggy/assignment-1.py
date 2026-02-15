def get_tri(x, a, b, c):
    """Calculates triangular membership"""
    return max(0, min((x - a) / (b - a) if b != a else 1, (c - x) / (c - b) if c != b else 1))

def get_trap(x, a, b, c, d):
    """Calculates trapezoidal membership"""
    return max(0, min((x - a) / (b - a) if b != a else 1, 1, (d - x) / (d - c) if d != c else 1))

def compute_washing_logic(stain_val, load_val):
    # 1. Fuzzification
    s_light = get_trap(stain_val, 0, 0, 25, 45)
    s_mod   = get_tri(stain_val, 35, 50, 65)
    s_heavy = get_trap(stain_val, 55, 75, 100, 100)

    l_small = get_trap(load_val, 0, 0, 2, 4)
    l_std   = get_tri(load_val, 3, 5, 7)
    l_bulk  = get_trap(load_val, 6, 8, 10, 10)

    # 2. Rule Evaluation (MIN)
    r1 = min(s_light, l_small)
    r2 = min(s_light, l_std)
    r3 = min(s_light, l_bulk)
    r4 = min(s_mod, l_small)
    r5 = min(s_mod, l_std)
    r6 = min(s_mod, l_bulk)
    r7 = min(s_heavy, l_small)
    r8 = min(s_heavy, l_std)
    r9 = min(s_heavy, l_bulk)

    # 3. Aggregation & Defuzzification (Centroid Method)
    numerator = 0
    denominator = 0
    
    for t in range(0, 61):  # Discrete time steps 0-60
        # Output Clipping (MAX of associated rules)
        brief_clip    = max(r1, r2)
        normal_clip   = max(r3, r4, r5)
        extended_clip = max(r6, r7, r8, r9)
        
        # Combine with output membership shapes
        m_brief = min(brief_clip, get_trap(t, 0, 0, 15, 25))
        m_norm  = min(normal_clip, get_tri(t, 20, 35, 50))
        m_ext   = min(extended_clip, get_trap(t, 45, 55, 60, 60))
        
        # Aggregate Max
        agg_score = max(m_brief, m_norm, m_ext)
        
        numerator += t * agg_score
        denominator += agg_score

    # Final Crisp Value
    return numerator / denominator if denominator != 0 else 0

# Test Case: 55% Stain, 5/10 Load
print(f"Optimal Cycle Time: {compute_washing_logic(55, 5):.2f} minutes")