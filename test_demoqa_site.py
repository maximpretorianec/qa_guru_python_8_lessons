from selene import browser, have,  be
import random, os


def test_form(browser_setup):

    browser.element('[id="firstName"]').type('Name')
    browser.element('[id="lastName"]').type('FamilyName')
    browser.element('[id="userEmail"]').type('user@qa.com')
    browser.element('[id="userNumber"]').type('9991111111')
    browser.element('[id="currentAddress"]').type('Street')
    browser.element("#subjectsInput").type("Arts").press_enter()
    random_gender = str(random.randint(1,3))
    random_hobbies = str(random.randint(1,3))
    gender_dict = {"1": "Male", "2": "Female", "3": "Other"}
    hobbies_dict = {"1": "Sports", "2": "Reading", "3": "Music"}
    browser.element('[for="gender-radio-' + random_gender + '"]').click()
    browser.element('[for="hobbies-checkbox-' + random_hobbies + '"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath("Duck.jpg"))
    browser.element('#dateOfBirthInput').should(be.not_.blank).click()
    browser.element('.react-datepicker__month-select').send_keys('September')
    browser.element('.react-datepicker__year-select').send_keys('1993')
    browser.element('[aria-label*="September 24th, 1993"]').click()
    browser.element('#state').click().element('#react-select-3-option-1').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()
    browser.element("#submit").click()

    browser.element('.modal-header').should(
        have.text('Thanks for submitting the form')
    )
    browser.element('.table > tbody').should(
        have.text('Student Name Name FamilyName')). \
        should(have.text('Student Email user@qa.com')). \
        should(have.text(f'Gender {gender_dict[random_gender]}')). \
        should(have.text('Mobile 9991111111')). \
        should(have.text('Date of Birth 24 September,1993')). \
        should(have.text('Subjects Arts')). \
        should(have.text(f'Hobbies {hobbies_dict[random_hobbies]}')). \
        should(have.text('Duck.jpg')). \
        should(have.text('Address Street')). \
        should(have.text('State and City Uttar Pradesh Lucknow'))
