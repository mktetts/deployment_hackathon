import json
import os
import python_backend.contract.deploy



def doctorDetailsInstance(w3):
	json_file_path = os.path.join(os.path.dirname(__file__), 'DoctorDetailContract.json')

	with open(json_file_path, 'r') as contract:
		Contract = json.load(contract)
	doctor_details_contract_abi = Contract["abi"]
	doctor_details_contract_address = python_backend.contract.deploy.doctor_details_contract_address
	# doctor_details_contract_address = "0x38BBC8EE210f378586Dc0203242fdfb190C8C1DB"
	if doctor_details_contract_address == "":
		return False
	doctor_detailsContract = w3.eth.contract(address = doctor_details_contract_address, abi = doctor_details_contract_abi)
	
	return doctor_detailsContract

def prescriptionDetailsInstance(w3):
	json_file_path = os.path.join(os.path.dirname(__file__), 'PrescriptionDetailContract.json')

	with open(json_file_path, 'r') as contract:
		Contract = json.load(contract)
	prescription_details_contract_abi = Contract["abi"]
	prescription_details_contract_address = python_backend.contract.deploy.prescription_details_contract_address
	# prescription_details_contract_address = "0x341A76e8f9FB98e1d8DCC78e3779FCF56F9A8312"
	if prescription_details_contract_address == "":
		return False
	prescription_detailsContract = w3.eth.contract(address = prescription_details_contract_address, abi = prescription_details_contract_abi)
	
	return prescription_detailsContract

def decodeInputData(w3, transactionHash, contract):
	transaction = w3.eth.get_transaction(transactionHash)
	decoded_input = contract.decode_function_input(transaction["input"])
	return (decoded_input[1]['_prescription'])
	