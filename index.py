import os

var="yes"
print("Brodcast is Live now!!:")
print("\n1)Audio Broadcast")
print("\n2)Video Brodcast")

while var=="yes" or var=="Yes":
 server_input = int(input('\nEnter your Choice:'))

 if server_input == 1:
    os.system('python server1.py')
 elif server_input == 2:
    os.system('python server2.py')
 print("Wanna continue?!")
 var = input('\nEnter your Choice:(Yes/No)')
