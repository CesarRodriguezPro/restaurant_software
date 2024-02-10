from twilio.rest import Client
from api_keys.twilio import ACCOUNT_SID, AUTH_TOKEN, verify_sid


def test_send_sms():
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    verified_number = "+12124704458"

    client = Client(account_sid, auth_token)

    verification = client.verify.v2.services(verify_sid).verifications.create(to=verified_number, channel="sms")
    print(verification.status)
    otp_code = input("Please enter the OTP:")
    verification_check = client.verify.v2.services(verify_sid).verification_checks.create(to=verified_number, code=otp_code)
    print(verification_check.status)
