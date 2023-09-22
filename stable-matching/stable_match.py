class StableMatch():

    def __init__(self, men_pref, women_pref):
        self.men_pref = men_pref
        self.women_pref = women_pref
    
    def stable_match():
        pass


if __name__ == "__main__":
    while True:
        try:
            n = 0
            l = input('What is the number of men and women that you must match, currently we only support the same number? (Press q to quit) \n')
            if l == 'q':
                break
            n = int(l)
            men_pref = []
            for i in range(1, n+1):
                preference = []
                for j in range(1, n+1):
                    p = input(f'What is the {j} th preference of the man {i} \n')
                    preference.append(int(p))
                print(f'The preferences that you have entered for man id {i} is {preference}')
                men_pref.append(preference)
            women_pref = []
            for i in range(1, n+1):
                preference = []
                for j in range(1, n+1):
                    p = input(f'What is the {j} th preference of the women {i} \n')
                    preference.append(int(p))
                print(f'The preferences that you have entered for women id {i} is {preference}')
                women_pref.append(preference)
            print('Calulation stable matching for the values that you have entered!')
            print(StableMatch(men_pref=men_pref, women_pref=women_pref).stable_match())
            print('Thank You!')
        except Exception:
            print('Invalid input')
            continue