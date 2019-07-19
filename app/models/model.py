def calculate_dry_results(a1, a2, a3, a4, a5, a6):
    total_int_values_in_list = int(a1)+int(a2)+int(a3)+int(a4)+int(a5)+int(a6)
    if total_int_values_in_list<5:
        return "dummy thiqué dry wall"
    elif total_int_values_in_list<10:
        return "Eco Friendly Drywall"
    elif total_int_values_in_list<12:
        return "Moisture Resistant Drywall"
    elif total_int_values_in_list<14:
        return "Sound Proof Drywall"
    elif total_int_values_in_list<16:
        return "Mold Resistant Drywall"
    elif total_int_values_in_list<18:
        return "Paperless Drywall"
    elif total_int_values_in_list<100:
        return "God Drywall"
    return "dope dry wall"
    
