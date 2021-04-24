def hero_fight(hero_1, hero_2):
    if hero_1.get('strength') > hero_2.get('strength') and hero_1.get('speed') > hero_2.get('speed'):
        return f"Grande vitória do {hero_1.get('name')}"
    
    elif (hero_1.get('strength') == hero_2.get('strength') and hero_1.get('speed') > hero_2.get('speed')) or hero_1.get('strength') > hero_2.get('strength') and hero_1.get('speed') == hero_2.get('speed'):
        return f"Vitória do {hero_1.get('name')}"
    
    elif (hero_1.get('strength') == hero_2.get('strength') and hero_1.get('speed') < hero_2.get('speed')) or hero_1.get('strength') < hero_2.get('strength') and hero_1.get('speed') == hero_2.get('speed'):
        return f"Vitória do {hero_2.get('name')}"
    
    elif (hero_1.get('strength') > hero_2.get('strength') and hero_1.get('speed') < hero_2.get('speed')) or (hero_1.get('strength') < hero_2.get('strength') and hero_1.get('speed') > hero_2.get('speed')) or (hero_1.get('strength') == hero_2.get('strength') and hero_1.get('speed') == hero_2.get('speed')) :
        return f"Empate entre os herois {hero_1.get('name')} e {hero_2.get('name')}"
    
    return f"Grande vitória do heroi {hero_2.get('name')}"