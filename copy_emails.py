def copy_emails_for_group(n: int, filename: str="emails_real", sepr: str="\n") -> None:
	import pyperclip
	pyperclip.copy(f"{sepr}".join([email.split("\t")[0] for email in open(filename, "r").read().split("\n") if email.split("\t")[-1] == str(n)]))


if __name__ == "__main__":
	copy_emails_for_group(2)
