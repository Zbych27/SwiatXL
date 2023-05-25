class Util:
    @staticmethod
    def company_from_email(email):
        parts = email.split("@")
        parts1 = parts[1].split(".")
        return parts1[0]
