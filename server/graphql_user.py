import graphene, json
class User:
    """Representation of user with Graphene

    Fields
    -----
    id : int
        Unique User ID for the user
    email : str
        Email address of the user
    displayName : str
        Display name for the user on the website
    coinVal : int
        Number of "CoinCoins" the user has
    """
    def __init__(self, id: int, email: str, displayName: str, coinVal: int):
        self.id = id
        self.email = email
        self.displayName = displayName
        self.coinVal = coinVal

    
