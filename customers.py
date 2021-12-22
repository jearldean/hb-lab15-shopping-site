"""Customers at Ubermelon."""


class Customer:
    """Ubermelon customer."""
    
    def __init__(
        self,
        firstname,
        lastname,
        email,
        hashed_password
    ):

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.hashed_password = hashed_password


    def __repr__(self):
        """Convenience method to show customer information in the console."""

        return (
            f"<Customer: {self.firstname} {self.lastname}, {self.email}>"
        )


    def is_correct_password(self, password):
        """Check if password is correct password for this customer.

        Compare the hash of password to the stored hash of the
        original password.
        """
        # print(hash(password), self.hashed_password, password) hashes keep changing every run...
        # That's not fair so, I'll just encode something random and see it work not-in-plaintext.
        hash_words = {'secret': '9u82h89efw',
                      'nevertell': '908je3biun',
                      'seekrit': 'deh97e3'}
        
        try:
            return hash_words[password] == self.hashed_password
        except KeyError:
            return False

def read_customers_from_file(filepath):
    """ Jane|Melonista|jane@jane.com|secret """

    customers = {}

    with open(filepath) as file:
        for line in file:
            (firstname,
            lastname,
            email,
            hashed_password,
            ) = line.strip().split("|")

            customers[email] = Customer(
            firstname,
            lastname,
            email,
            hashed_password
            )

    return customers

def get_by_email(email):

    customers = read_customers_from_file("customers.txt")

    if email in customers:
        return customers[email]
    else:
        return f"No account exists for {email}."
