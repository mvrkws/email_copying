# email_copying

The file ```emails``` is a plain file with the following structure:

```txt
username@uib.no    1
username@uib.no    1
username@uib.no    2
username@uib.no    4
```

Each row is seperated with \n, and each row has \t seperation between an email address and a group number.

The function ```copy_emails_from_group(n)``` in ```copy_emails.py``` will copy all the relevant emails to your clipboard to paste into Outlook in order to invite all emails to a meeting.

NOTE:
Either use another file (like emails_real) to store actual emails, or make sure you don't upload the updated file to github. As to not publish emails publically.