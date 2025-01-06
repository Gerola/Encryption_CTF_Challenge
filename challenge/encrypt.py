import base64
import getpass

def encode_payload():
    message = input("What would you like to encode?: ")
    keyphrase = getpass.getpass("What is your phrase?   (This will not echo back): ")
    value = (getpass.getpass("What is your value?    (This will not echo back): "))

    try:
        value = int(value)
    except:
        raise TypeError("Please have the value be a number, not any letters")
    
    new_message = []
    for place in range(0,len(message)):
        new_message.append(hex(ord(message[place]) ^ (value*ord(keyphrase[place % len(keyphrase)]))))
   
    final_encode = []
    for m in new_message:
        hex_value = m.encode("ascii")
        final_encode.append(((base64.b64encode(hex_value)).decode("ascii")))
   
    print(f"The final encoded payload is {final_encode}\n\nDon't forget your keyphrase and value or you wont be able to decode the message!")


encode_payload()