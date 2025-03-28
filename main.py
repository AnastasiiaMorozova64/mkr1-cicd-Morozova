class Nation:
    def __init__(self, title, territory_size, citizen_count):
        self.title = title
        self.territory_size = float(territory_size)
        self.citizen_count = int(citizen_count)

def execute():
    print("its main")

if __name__ == "__main__":
    execute()