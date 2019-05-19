import hz_mesage as message

try:
    message.hz_send_message.send("小米")

except Exception as result:
    print(result)
