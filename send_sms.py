from kavenegar import KavenegarAPI, APIException, HTTPException

def decode_farsi_bytes(byte_string):
    return byte_string.decode('utf-8', errors='replace')

def send_sms(text):
    try:
        api = KavenegarAPI('326466645550326453507235576470764A506E3379652B74414E384457494F6B514F45667947596C636B513D')
        params = {'receptor': '09053357762', 'type': 'call', 'message': text}
        response = api.sms_send(params)
        
        print(response)
        if response[0].status == 200:
            print("SMS Sent successfully!")
        else:
            error_message = decode_farsi_bytes(response.message)
            print(f"Error {response.status}: {error_message}")
            
    except APIException as e:
        print(f"API Exception: {e}")
        
    except HTTPException as e:
        print(f"HTTP Exception: {e}")
