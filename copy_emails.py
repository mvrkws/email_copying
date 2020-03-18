import pyperclip

def copy_emails_from_group(n : int, filename: str="emails_real", sepr: str="\n") -> None:
	pyperclip.copy(f"{sepr}".join([email.split("\t")[0] for email in open(filename, "r").read().split("\n") if email.split("\t")[-1] == str(n)]))


copy_emails_from_group(2)
