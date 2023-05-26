class Util:
    @staticmethod
    def company_from_email(email):
        """
        Funkja pomocnicza kreująca nazwę firmy na podstawie przekazanego adresu email
        """
        parts = email.split("@")
        parts1 = parts[1].split(".")
        return parts1[0]
