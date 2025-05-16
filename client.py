import hashpumpy
from server import verify  # هنستخدم verify من السيرفر عشان نثبت الهجوم

def perform_attack():
    intercepted_message = b"amount=100&to=alice"
    intercepted_mac = "616843154afc11960423deb0795b1e68"

    data_to_append = b"&admin=true"
    secret_length = 14  # طول السر اللي في السيرفر (supersecretkey)

    # نعمل الهجوم
    new_mac, new_message = hashpumpy.hashpump(intercepted_mac, intercepted_message.decode(), data_to_append.decode(), secret_length)

    print("Forged message:", new_message)
    print("Forged MAC:", new_mac)

    # نتحقق من الرسالة المزورة على السيرفر
    if verify(new_message, new_mac):
        print("Attack successful! Forged MAC is accepted by the server.")
    else:
        print("Attack failed. Forged MAC rejected.")

if __name__ == "__main__":
    perform_attack()
