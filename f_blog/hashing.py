from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash:

    def bcrypt(password):
        hashedPassword = pwd_cxt.hash(password)

        return hashedPassword

    def verify(hashed_password, plain_password):
        verify_password = pwd_cxt.verify(plain_password, hashed_password)

        return verify_password
