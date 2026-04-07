from selene import browser, be, have

def test_login_correct_password(browser_open):
    browser.open('/cms/system/login')

    browser.element('.login-form [name=email]').type('leyavoo@gmail.com')
    browser.element('.login-form [name=password]').type('edbrwkqd13321-ew!E')
    browser.element('.login-form .btn-success').click()

    browser.element('.logined-form').should(have.text('Здравствуйте'))


def test_login_wrong_password(browser_open):
    browser.open('/cms/system/login')

    browser.element('.login-form [name=email]').type('leyavoo@gmail.com')
    browser.element('.login-form [name=password]').type('wrong-password')
    browser.element('.login-form .btn-success').click()

    browser.element('.login-form .btn-success.btn-error').should(be.visible)
    browser.element('.login-form .btn-success.btn-error').with_(timeout=6).should(be.hidden)





