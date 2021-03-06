from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def decision_manager_with_merchant_defined_information():
    try:
        # Setting the json message body
        request = CreateDecisionManagerCaseRequest()
        client_reference = Riskv1decisionsClientReferenceInformation()
        client_reference.code = "54323007"
        request.client_reference_information = client_reference.__dict__

        processing_info = Riskv1decisionsPaymentInformation()

        request.processing_information = processing_info.__dict__

        order_information = Riskv1decisionsOrderInformation()
		
        bill_to = Riskv1decisionsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.last_name = "smith"
        bill_to.address1 = "96, powers street."
        bill_to.postal_code = "03055"
        bill_to.locality = "Clearwater milford"
        bill_to.administrative_area = "NH"
        bill_to.first_name = "James"
        bill_to.phone_number = "7606160717"
        bill_to.company = "Visa"
        bill_to.email = "test@cybs.com"

        amount_details = Riskv1decisionsOrderInformationAmountDetails("USD")
        amount_details.total_amount = "144.14"

        order_information.bill_to = bill_to.__dict__
        order_information.amount_details = amount_details.__dict__
        request.order_information = order_information.__dict__

        payment_info = Riskv1decisionsPaymentInformation()
        card = Riskv1decisionsPaymentInformationCard()
        card.expiration_year = "2031"
        card.number = "4444444444444448"
        card.expiration_month = "12"
        payment_info.card = card.__dict__
        request.payment_information = payment_info.__dict__

        merchant_defined_information = []
        merchant_defined_information0 = Riskv1decisionsMerchantDefinedInformation()
        merchant_defined_information0.Key = "1"
        merchant_defined_information0.Value = "Test"

        merchant_defined_information1 = Riskv1decisionsMerchantDefinedInformation()
        merchant_defined_information1.Key = "2"
        merchant_defined_information1.Value = "Test2"
		
        merchant_defined_information.append(merchant_defined_information0.__dict__)
        merchant_defined_information.append(merchant_defined_information1.__dict__)
        request.merchant_defined_information = merchant_defined_information
        
        message_body = json.dumps(request.__dict__)

        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()

        dm_obj = DecisionManagerApi(details_dict1)
        return_data, status, body = dm_obj.create_decision_manager_case(message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("Exception when calling DecisionManagerApi->create_decision_manager_case: %s\n" % e)


if __name__ == "__main__":
    decision_manager_with_merchant_defined_information()
