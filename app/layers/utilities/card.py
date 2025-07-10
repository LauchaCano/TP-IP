class Card:
    def __init__(self, name, base, image, types, hp, attack, defense, user=None, id=None):
        self.name = name.capitalize()  # Nombre del pokemon
        self.hp = hp  # Puntos de vida  
        self.attack = attack # Ataque
        self.defense = defense  # Defensa
        self.base = base  # NIVEL BASE
        self.image = image  # URL de la imagen
        self.user = user  # Usuario asociado (si corresponde)
        self.id = id  # ID único (si corresponde)
        self.types = types or []  # Asegura que sea una lista por defecto
        
    def __str__(self):
        return (f'name: {self.name}, height: {self.height}, weight: {self.weight}, '
                f'base: {self.base}, image: {self.image}, user: {self.user}, id: {self.id}')

    # Método equals.
    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return (self.name, self.height, self.weight, self.id) == \
               (other.name, other.height, other.weight, other.id)

    # Método hashCode.
    def __hash__(self):
        return hash((self.name, self.height, self.weight, self.id))
