class Customer:
    def __init__(self, name, MembershipType):
        self.name = name
        self.MembershipType = MembershipType
        #print("customer created")


C = Customer("Dini", "Glod")
print(C.name, C.MembershipType)
c1 = Customer("osman", "silver")
print(c1.name, c1.MembershipType)