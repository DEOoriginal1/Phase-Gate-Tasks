

import unittest 

from account import  *


class AccountTest(unittest.TestCase):


	
		
	def test_that_ANewAccount_hasAccountNumber_Generated_with_10_digits(self):
		
		account_firstname ,account_lastname ,phone_number,pin, username  = create_account_details()
		
		
		account = create_account(account_firstname,account_lastname,phone_number,pin,username)
		
		self.assertEqual(len(account["account_number"]), 10)
		self.assertEqual(account["balance"], 0.0)
		self.assertEqual(type(account), dict)
		
		
	def test_that_AccountNumber_Generated_start_with_double_zero(self):
		
		account_firstname ,account_lastname ,phone_number,pin, username  = create_account_details()
		
		account = create_account(account_firstname,account_lastname,phone_number,pin,username)
		
		self.assertEqual(len(account["account_number"]), 10)
		self.assertTrue(account["account_number"].startswith("00"))
				
			
	def test_that_a_newAccount_HasAZeroBalance(self):
	
		account_firstname ,account_lastname ,phone_number,pin, username  = create_account_details()
		account = create_account(account_firstname,account_lastname,phone_number,pin,username)
		
		account_balance =  0.0
		
		self.assertEqual(check_balance(account["account_number"]), account_balance)
		
			
				
	def test_that_TwoAccounts_have_different_RandomAccountNumber_Generated(self):
			
		account_firstname ,account_lastname ,phone_number,pin, username  = create_account_details()
		
		account_two_firstname =  "Addidas" 
		account_two_lastname =  "Michael"
		account_two_phone_number  =  "08017272819"
		pin = "9090"
		username = "add"
		
		
		account = create_account(account_firstname,account_lastname,phone_number,pin,username)
		account_two = create_account(account_two_firstname,account_two_lastname,account_two_phone_number,pin,username)
		
		self.assertEqual(len(account["account_number"]), 10)
		self.assertEqual(len(account_two["account_number"]), 10)
		
		self.assertTrue(account["account_number"].startswith("00"))
		self.assertTrue(account_two["account_number"].startswith("00"))
		
		self.assertNotEqual(account["account_number"], account_two["account_number"])
		

	def test_that_500_isdepositedInto_Account(self):
	
		firstname ,lastname ,phone_number,pin, username  = create_account_details()
		account = create_account(firstname,lastname,phone_number,pin, username)
		
		amount =  500.0
		account_number = account["account_number"]
		
		deposit(account_number,amount)
	
		self.assertEqual(500.0, account["balance"])
				
	
	def test_that_when_1500_isDepositedIntoAccount_and_700_isWithDrawn_BalanceIs_800(self):
	
		firstname ,lastname ,phone_number,pin, username  = create_account_details()
		account = create_account(firstname,lastname,phone_number,pin, username)
		
		account_number = account["account_number"]
		
		deposit(account_number,1500.0)
		
		withdraw(account_number,700.0, pin)
		
		self.assertEqual(800.0, account["balance"])
		
		
	def test_that_when_I_deposit_check_balance_returns_new_balance(self):
	
		firstname ,lastname ,phone_number,pin, username  = create_account_details()
		account = create_account(firstname,lastname,phone_number,pin, username)
		
		account_number = account["account_number"]
		
		self.assertEqual(check_balance(account_number), 0.0)
		
		deposit(account_number,1500.0)
		
		self.assertEqual(check_balance(account_number), 1500.0)
		
		
		
		

	
