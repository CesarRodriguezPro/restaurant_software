from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from api_keys.brevo_api_key import brevo_api


def send_text_message():
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = brevo_api
    api_instance = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(configuration))
    send_transac_sms = sib_api_v3_sdk.SendTransacSms(
        sender="+12124704458",
        recipient="+12124704458",
        content="test ",
    )

    try:
        api_response = api_instance.send_transac_sms(send_transac_sms)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionalSMSApi->send_transac_sms: %s\n" % e)