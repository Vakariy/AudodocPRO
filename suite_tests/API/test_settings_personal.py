import pytest
from base.apibase import *

headers = Header(get_user_token())
@pytest.mark.Settings
@pytest.mark.API
def test_update_bank_detail():
    body = {
        "alias": NAME_SEPA,
        "iban": IBAN_SEPA,
        "bic": BIC_SEPA
    }

    response = requests.put(
        get_route_settings('put_bank_detail'),
        json=body,
        headers=headers.get_header()
    )

    assert response.status_code == 200, 'Bank detail settings was not updated'
    assert response.json()["data"]["alias"] == NAME_SEPA, 'Incorrect Sepa name'
    assert response.json()["data"]["iban"] == IBAN_SEPA, 'Incorrect Sepa IBAN'
    assert response.json()["data"]["bic"] == BIC_SEPA, 'Incorrect Sepa BIC'


@pytest.mark.Settings
@pytest.mark.API
def test_get_bank_detail():
    test_update_bank_detail()
    response = requests.get(
        get_route_settings('get_bank_detail'),
        headers=headers.get_header()
    )

    assert response.status_code == 200, 'Bank details service is not available'
    assert response.json()["data"]["alias"] == NAME_SEPA, 'Incorrect Sepa name'
    assert response.json()["data"]["iban"] == IBAN_SEPA, 'Incorrect Sepa IBAN'
    assert response.json()["data"]["bic"] == BIC_SEPA, 'Incorrect Sepa BIC'


@pytest.mark.Settings
@pytest.mark.API
def test_delete_bank_detail():
    test_update_bank_detail()

    response = requests.delete(
        get_route_settings('delete_bank_detail'),
        headers=headers.get_header()
    )
    getBankDetails = requests.get(
        get_route_settings('get_bank_detail'),
        headers=headers.get_header()
    )

    assert response.status_code == 204, 'Bank details was not deleted'
    assert getBankDetails.json()["data"]["alias"] == "", 'Incorrect Sepa name'
    assert getBankDetails.json()["data"]["iban"] == "", 'Incorrect Sepa IBAN'
    assert getBankDetails.json()["data"]["bic"] == "", 'Incorrect Sepa BIC'


@pytest.mark.Settings
@pytest.mark.API
def test_get_company_name():
    response = requests.get(
        get_route_settings('get_company_info'),
        headers=headers.get_header()
    )

    assert response.status_code == 200, 'Company info service is not available'


@pytest.mark.Settings
@pytest.mark.test
def test_update_company_name():
    response = requests.put(
        get_route_settings('put_company_inf'),
        headers=headers.get_header(),
        json=get_json_file('put_company_fr.json')
    )
    expected_data = get_json_file('get_company_fr.json')
    actual_data = json.loads(response.content)

    assert response.status_code == 200, 'Company info service is not available'
    assert expected_data == actual_data, 'Updated company information data is NOT saved'