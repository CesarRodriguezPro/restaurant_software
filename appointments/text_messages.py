from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk import TransactionalSMSApi
from sib_api_v3_sdk.rest import ApiException
from api_keys.brevo_api_key import brevo_api


def send_text_message(request, recipient, message) -> TransactionalSMSApi:
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = brevo_api
    api_instance = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(configuration))
    send_transac_sms = sib_api_v3_sdk.SendTransacSms(
        sender=request.user.company.telephone,
        recipient=recipient,
        content=message,
    )
    try:
        api_response: TransactionalSMSApi = api_instance.send_transac_sms(send_transac_sms)
        return api_response

    except ApiException as e:
        print(f"Exception when calling TransactionalSMSApi->send_transac_sms:{e}")