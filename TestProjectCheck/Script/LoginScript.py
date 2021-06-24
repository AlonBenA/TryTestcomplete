def LoginTest():
    UserName = "SUPER_YAACOV"
    Password = "Rafael6"
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("https://rafael-test.wfsaas.com/workforce/Desktop.do")
    #Enters text in the text box.
    Aliases.browser.pageWorkforceTime.formLogonform.UserNameTextBox.SetText(UserName)
    #Enters text in the text box.
    Aliases.browser.pageWorkforceTime.formLogonform.PassWordTextBox.SetText(Password)
    #Simulates a left-button single click in a window or control as specified (relative position, shift keys).
    Aliases.browser.pageWorkforceTime.formLogonform.LoginButton.Click()
