# import bcrypt


# username=input("Enter Username: ")
# password=input("Enter Password: ")


# def hash_pas(password:str):
#     return bcrypt.hashpw(
#         password.encode('utf-8'),
#         bcrypt.gensalt()
#     ).decode('utf-8')

# hashed_pass=hash_pas(password)

# login={
#     'username':username,
#     'pass':hash_pas
# }

# print(login)
# print('----------------------------------------')
# print(f"  Hey {login['username'][0].upper()}{login['username'][1:len(login['username'])]} Welcome !")
# print('----------------------------------------')


fake_db={
    "username":"ram",
    "email":"priya@gmail.com"
}

