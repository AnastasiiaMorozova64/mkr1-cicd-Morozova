class Nation:
    def __init__(self, title, territory_size, citizen_count):
        self.title = title
        self.territory_size = float(territory_size)
        self.citizen_count = int(citizen_count)    
    def __repr__(self):
        return f"{self.title} - {self.territory_size} км, {self.citizen_count} людей"

class DemographicStats:
    def __init__(self, source_file):
        self.nation_list = self.load_nation_data(source_file)
    
    def load_nation_data(self, source_file):
        registry = []
        with open(source_file, "r", encoding="utf-8") as file:
            for entry in file:
                attributes = entry.strip().split(", ")
                if len(attributes) != 3:
                    continue  # Пропускаємо некоректні записи
                
                try:
                    country_entry = Nation(attributes[0], attributes[1], attributes[2])
                    registry.append(country_entry)
                except ValueError:
                    continue  # Ігноруємо помилкові рядки
        return registry 
       
    def arrange_by_territory(self):
        return sorted(self.nation_list, key=lambda nation: nation.territory_size, reverse=True)
    
    def arrange_by_citizens(self):
        return sorted(self.nation_list, key=lambda nation: nation.citizen_count, reverse=True)

def execute():
    source_file = "population_countries_data.txt"  # Змінити на фактичний файл
    stats_handler = DemographicStats(source_file)
    
    print("\nРанжування за територією:")
    for nation in stats_handler.arrange_by_territory():
        print(nation)
    
    print("\nРанжування за чисельністю населення:")
    for nation in stats_handler.arrange_by_citizens():
        print(nation)

if __name__ == "__main__":
    execute()