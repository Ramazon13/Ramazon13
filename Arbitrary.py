# default arguments = A default for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1.positional, 2.default, 3. keyboard, 4. ARBITRARY

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
         print(f"{kwargs.get('street')}")
         print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
                   street="123 Fake St",
                   pobox="PO box #1001",
                   city="Detroit",
                   state="MI",
                   zip="54321")
