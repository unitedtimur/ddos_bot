# Import modules
import lib.Impulse.tools.addons.twilight.xor as Xor
import lib.Impulse.tools.addons.twilight.salt as Salt
import lib.Impulse.tools.addons.twilight.hash as Hash

# Encrypt function
def Encrypt(text, key):
    
    salt = Hash.getSaltByKey(key, text)
    saltedText = Salt.protect(text, salt)
    xoredText  = Xor.encode(saltedText, key)
    return xoredText

# Decrypt function
def Decrypt(text, key):
    unxoredText = Xor.decode(text, key)
    salt = Hash.getSaltByKey(key, unxoredText)
    unsaltData  = Salt.unprotect(unxoredText, salt)
    return unsaltData
