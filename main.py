# 1-masala
class FootballPlayer:
    def __init__(self, fullname, number):
        self.fullname = fullname
        self.number = number

    def __repr__(self):
        return f"Maydondagi {self.number}-raqamli futbolchi — {self.fullname}"


player = FootballPlayer("Jasur Iskandarov", 10)
print(player)


# 2-masala
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} buyurtmasi: {self.price} so'm"


food = Food("Osh", 30000)
print(food)


# 3-masala
class BankCard:
    def __init__(self, owner, bank):
        self.owner = owner
        self.bank = bank

    def __repr__(self):
        return f"{self.owner}ning banki — {self.bank}"


card = BankCard("Madina Sobirova", "Xalq banki")
print(card)


# 4-masala
class Game:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def __repr__(self):
        return f"{self.title} o'yini | Janri: {self.genre}"


game = Game("Minecraft", "Sandbox")
print(game)


# 5-masala
class Passport:
    def __init__(self, fullname, seria):
        self.fullname = fullname
        self.seria = seria

    def __repr__(self):
        return f"Pasport egasi: {self.fullname} | Seriya: {self.seria}"


passport1 = Passport("Bunyod Shokirov", "AC 1234567")
passport2 = Passport("Sarvar Xojametov", "AD 12356392")

print(passport1)
print(passport2)
