# Problem
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.


# Explaining the Solution

The idea is to use the built in string fucntions such as split and replace in order to santize each email. Once santized we add the clean email to the set. Set is a data structure in Python that is implemented using hashtables, hence the insert/lookup/delete times are O(1). After iterating we return the len of the set.


## Time Complexity

```
def sanitizeEmail(self, email: str) -> str:
        # split the localname and domain name
        raw_localname, domain = email.split('@')
        # logic to clean the email
        localname = raw_localname.split('+')[0].replace('.', '') # ignore everything after first + and remove all dots
        return localname + '@' +domain
```

santize email runtime is O(lenght of the string) since replace, split takes lenght of the string to find the characters/patterns

Since we do this for each email the overall all time complexity is O(N * M) where N is the number of emails and M is the average length of the string.