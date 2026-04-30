class Solution:
    def maskPII(self, s: str) -> str:
        # check if input is email
        if s[0].isalpha():
            s = s.lower()
            at_position = s.find('@')

            return s[0]+'*****'+s[at_position-1:]
        
        # handle phone number
        digits = ''.join(c for c in s if c.isdigit())
        country_code_length = len(digits)-10
        suffix = '***-***-'+digits[-4:]

        if country_code_length==0:
            return suffix
        else:
            return f'+{"*"*country_code_length}-{suffix}'