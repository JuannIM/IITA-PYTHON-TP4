class Hand:
    """
    Represents a hand with a maximum lifting capacity.
    """
    def __init__(self, max_weight: float):
        self.max_weight = max_weight

    def can_lift(self, weight: float) -> bool:
        """
        Checks if the hand can lift a given weight.
        """
        return weight <= self.max_weight

class Person:
    """
    Represents a person with two hands and a total lifting strength.
    """
    def __init__(self, left_hand: Hand, right_hand: Hand, total_strength: float):
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.total_strength = total_strength

    def can_lift(self, weight: float) -> str:
        """
        Determines if the person can lift the given weight.
        """
        if self.left_hand.can_lift(weight):
            return "Can lift with the left hand."
        if self.right_hand.can_lift(weight):
            return "Can lift with the right hand."
        if weight <= self.total_strength:
            return "Can lift using both hands."
        return "Cannot lift the object."

# User input section
left_hand_capacity = float(input("Enter left hand lifting capacity: "))
right_hand_capacity = float(input("Enter right hand lifting capacity: "))
total_strength = float(input("Enter total lifting strength: "))
person = Person(Hand(left_hand_capacity), Hand(right_hand_capacity), total_strength)

while True:
    weight = float(input("Enter the weight of the object (or -1 to exit): "))
    if weight == -1:
        break
    print(person.can_lift(weight))
