import unittest
from Package1.TC_loginTest import LoginTest
from Package1.TC_SignUpTest import signUpTest
from Package2.TC_paymentTest import paymentTest
from Package2.TC_PaymentReturns import paymentReturnsTest
#################################################################

#Get all tests from each class

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(signUpTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(paymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(paymentReturnsTest)

#Create a test suit
sanity= unittest.TestSuite([tc1])
faunctional=unittest.TestSuite([tc1, tc2])

#Run the suit
unittest.TextTestRunner().run(faunctional)