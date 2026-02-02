

def calcular_dano(spell, nivel_slot):
    if not spell.dano_base:
        raise ValueError("Magia não causa dano")
    
    if spell.progressao_slot and nivel_slot in spell.progressao_slot:
        return spell.progressao_slot[nivel_slot]
    
    return spell.dano_base