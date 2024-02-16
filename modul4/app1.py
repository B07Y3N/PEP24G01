def check_password():
    requires_chars = ["!", "@", "%"]
    password = input('Introduceti o parola: ')
    print(password)
    condition_not_ok = False
    if len(password) < 7:
        print("Wrong lenght password")
        condition_not_ok = True

        # check_password()
    else:
        # for char_ in password:
        #     if char_ in requires_chars:
        #         break
        # else:
        #     check_password()
        for character in requires_chars:
            if character in password:
               break
        else:
             print("The password must contain: ! @ %")
             condition_not_ok = True


        for character in range(10):
            if str(character) in password:
                break
        else:
            print("Password must contain: number")
            condition_not_ok = True
        if condition_not_ok:
            check_password()

check_password()

