from selene import browser, have, be


def test_student_registration_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('ivanov@example.com')

    browser.element('#gender-radio-1').click()

    browser.element('#userNumber').type('9991234567')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="4"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1995"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--015').click()

    browser.element('#subjectsInput').type('Maths').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys(__file__)

    browser.element('#currentAddress').type('Moscow, Russia')

    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()

    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').click()

    browser.element('.modal-content').should(be.visible)
    browser.element('.modal-content').all('tr').should(
        have.exact_texts(
            'Label Values',
            'Student Name Ivan Ivanov',
            'Student Email ivanov@example.com',
            'Gender Male',
            'Mobile 9991234567',
            'Date of Birth 15 May,1995',
            'Subjects Maths',
            'Hobbies Sports',
            'Picture test_student_registration_form.py',
            'Address Moscow, Russia',
            'State and City NCR Delhi'
        )
    )
