class Hand:
    """
    Represents a hand with a maximum weight capacity.
    """
    def __init__(self, max_weight: float):
        """
        Initializes the hand with its maximum carrying capacity.
        
        :param max_weight: Maximum weight the hand can hold.
        """
        self.max_weight = max_weight
    
    def can_hold(self, weight: float) -> bool:
        """
        Checks if the hand can hold a given weight.
        
        :param weight: The weight to check.
        :return: True if the hand can hold the weight, False otherwise.
        """
        return weight <= self.max_weight


class Person:
    """
    Represents a person with two hands and a total lifting strength.
    """
    def __init__(self, left_hand: Hand, right_hand: Hand, total_strength: float):
        """
        Initializes a person with two hands and total lifting strength.
        
        :param left_hand: The left hand object.
        :param right_hand: The right hand object.
        :param total_strength: The maximum weight the person can lift using both hands.
        """
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.total_strength = total_strength
    
    def can_lift(self, weight: float) -> str:
        """
        Determines if the person can lift an object using one or both hands.
        
        :param weight: The weight of the object.
        :return: A message indicating whether the person can lift the object and with which hand(s).
        """
        if self.left_hand.can_hold(weight):
            return "Can lift with the left hand."
        elif self.right_hand.can_hold(weight):
            return "Can lift with the right hand."
        elif weight <= self.total_strength:
            return "Can lift using both hands."
        return "Cannot lift the object. Too heavy."


# Example Usage:
left = Hand(10)
right = Hand(15)
person = Person(left, right, 20)

# Test Cases:
print(person.can_lift(8))   # Should be able to lift with the left hand
print(person.can_lift(12))  # Should be able to lift with the right hand
print(person.can_lift(18))  # Should be able to lift using both hands
print(person.can_lift(25))  # Should not be able to lift
