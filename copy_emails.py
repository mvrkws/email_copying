import pyperclip

def copy_emails_from_group(n, sepr="\n"):
	copy = ""

	for email in open("emails_real", "r").read().split("\n"):
		try:
			email, group = email.split("\t")
		except:
			continue

		if group == str(n):
			copy += email + sepr

	pyperclip.copy(copy[:-len(sepr)])

copy_emails_from_group(2)