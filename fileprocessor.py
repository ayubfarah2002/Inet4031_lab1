with open("fileprocessor.input", "r") as file:

    lines = file.readlines()

user_data=[]

for line in lines:

    if line.startswith("#"):
    data = line.strip().split(":")

    user_data.append(data)

print("Printing out User Data:")
for user in user_data:
    username, password, userid, groupid = user
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

print("End of User Data")
