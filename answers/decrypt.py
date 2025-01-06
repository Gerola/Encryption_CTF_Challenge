import base64
import getpass


def decode_payload():
    encode_message = input("Please paste in your encoded message in list form: ")
    if '[' not in encode_message or ']' not in encode_message:
        raise TypeError("Place the encoded message in the brackets") 
    encode_message = encode_message.replace("[","").replace("]","").replace("'","").split(",")
    keyphrase = getpass.getpass("What is your phrase?   (This will not echo back): ")

    value = (getpass.getpass("What is your value?    (This will not echo back): "))
    try:
        value = int(value)
    except:
        raise TypeError("Please have the value be a number, not any letters")
    final_decode = []
    hex_values = []
    for x in encode_message:
        decode_message = x.strip().encode("ascii")
        hex_values.append((base64.b64decode(decode_message).decode("ascii")))

    for v in range(0,len(hex_values)):
        final_decode.append((chr(int(hex_values[v],16) ^  (value*ord(keyphrase[v % len(keyphrase)])))))
        
    command = "".join(final_decode)    
    print(command)



decode_payload()