import jwt
import datetime
import time
import config

def generate_token(payload):

    exp_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    payload['exp'] = exp_time


    payload['iat'] = datetime.datetime.utcnow()


    encode_jwt = jwt.encode(
        payload=payload,
        key=config.JWT_SECRET,
        algorithm='HS256',
    )

    return encode_jwt

def decode_token(token):
    try:

        decoded = jwt.decode(
            token,
            config.JWT_SECRET,
            algorithms=['HS256'],
        )
        return decoded
    except jwt.ExpiredSignatureError:

        return {'error': 'Token has expired.'}
    except jwt.InvalidTokenError:

        return {'error': 'Invalid token.'}


payload_data = {
    'my_name': 'Vasyl',
    'password': 'kdfjhgkl;dfjkgdfkluhg;.dfjglkdfgkdfli;ghdfljgkljdfgkl;dfg',
}


token = generate_token(payload_data)
print("Encoded Token:", token)


time.sleep(3)


decoded_payload = decode_token(token)
print("Decoded Payload:", decoded_payload)
