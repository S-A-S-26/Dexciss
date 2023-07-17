# Copyright (c) 2023, sujit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

import time

class LibraryMembership(Document):
	# pass
	def before_submit(self):
		exists=frappe.db.exists(
			"Library Membership",
			{
				#my experimentaly play code
				# "full_name":self.full_name,
				# "docstatus":1,

				"library_member":self.library_member,
				"docstatus":DocStatus.submitted(),
				"to_date":(">",self.from_date),
			},
		)
		print("*"*20)
		print(f"This is custom print inserted")
		print(type(exists))
		print(f"self.library_member:{self.library_member}\ndocstatus:{DocStatus.submitted()}\nself.from_date:{self.from_date}\nexists:{exists}\nself.full_name:{self.full_name}")

		print("*"*20)
		time.sleep(2)

	#my experimental play code
		# exit=None
		# if exists:
		# 	frappe.throw(f"A record with {self.name} already exists where user is {self.full_name}")

		if exists:
			frappe.throw ("there is an active membership for this member")

		loan=frappe.db.get_single_value("Library Settings","loan_period")
		self.to_date=frappe.utils.add_days(self.from_date,loan or 30)
