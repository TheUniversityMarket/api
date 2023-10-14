from vgem import EM

def test_vgem():
    em = EM()

    password = "password123"

    hash_and_salt = em.hash(password, True)
    hash = hash_and_salt['hash']
    salt = hash_and_salt['salt']
    try:
        if em.check_hash(message=password,hash=hash, salt=salt, base64=True) is None:
            assert True
    except:
        assert False

if __name__ == "__main__":
    test_vgem()