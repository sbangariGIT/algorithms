class Solution:
    def sanitizeEmail(self, email: str) -> str:
        # split the localname and domain name
        raw_localname, domain = email.split('@')
        # logic to clean the email
        localname = raw_localname.split('+')[0].replace('.', '') # ignore everything after first + and remove all dots
        return localname + '@' +domain
    
    def numUniqueEmails(self, emails) -> int:
        valid_emails = set()
        for email in emails:
            valid_emails.add(self.sanitizeEmail(email))
        return len(valid_emails)
