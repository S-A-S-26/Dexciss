# Copyright (c) 2023, sujit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryTransaction(Document):
	# pass
	def before_submit(self):
		article=frappe.get_doc("Article",self.article)
		print("*"*20)
		print(article.status)
		if self.type=="Issue":
			self.check_membership()
			print(article.status=="Available")
			if article.status != "Available":
				frappe.throw("Sorry but the article has been already issued to another member")
			article.status="Issued"
			article.save()

		elif self.type=="Return":
			print("inside return")
			print(article)
			print(article.status!="Issued")
			# frappe.throw("interrupt")
			if article.status != "Issued":
				frappe.throw("Article can be only returned if it has been issued currently this article is available")
			article.status="Available"
			article.save()
		
		#max no articles limit 
		limit=frappe.db.get_single_value("Library Settings","max_articles")
		count=frappe.db.count(
			"Library Transaction",
			{
				"library_member":self.library_member,
				"type":"Issue",
				"docstatus":1,
			}
		)
		if count>=limit:
			frappe.throw("Max limit for articles reached")

	# def after_delete(self):
	# 	article=frappe.get_doc("Article",self.article)
	# 	print("#"*40)
	# 	print(article_clear)
	# 	article.status="Available"
	# 	article.save()
	# 	frappe.throw("interrupt")

	def check_membership(self):
		print("*"*20)
		print(f"self.date:{self.date}")
		x=frappe.get_doc("Library Membership",{"library_member":self.library_member,})
		print(f"Library Membership:{x}")
		print(x.full_name)
		print(x.from_date)
		print(x.to_date)
		exists=frappe.db.exists(
			'Library Membership',
			{
				'library_member':self.library_member,
				'docstatus':DocStatus.submitted(),
				'from_date':("<=",self.date),
				'to_date':(">=",self.date),

			},
		)
		print(exists)
		print("*"*20)
		if not exists:
			frappe.throw("Membership expired please kindly renew")






