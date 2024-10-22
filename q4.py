import pickle
import os

#save user pref
def save_pref(pref, filename='user_pref.pkl'):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(pref, file)
        print("pref saved successfully.")
    except Exception as e:
        print(f"Error saving pref: {e}")

#load user pref
def load_pref(filename='user_pref.pkl'):
    if not os.path.exists(filename):
        print("pref file not found. Loading default pref.")
        return default_pref()

    try:
        with open(filename, 'rb') as file:
            pref = pickle.load(file)
        print("pref loaded successfully.")
        return pref
    except (pickle.UnpicklingError, EOFError, FileNotFoundError) as e:
        print(f"Error loading pref: {e}")
        print("Loading default pref.")
        return default_pref()

#default pref
def default_pref():
    return {
        'theme': 'light',
        'language': 'English',
        'notifications': True
    }


# Load pref
user_pref = load_pref()

#current pref
print(f"Current pref: {user_pref}")

#updating
user_pref['theme'] = 'dark'
user_pref['language'] = 'Spanish'


save_pref(user_pref)
