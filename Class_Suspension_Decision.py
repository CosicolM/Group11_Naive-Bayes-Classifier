class NaiveBayesClassifier:
    def __init__(self):
        self.p_yes_str, self.p_no_str = "8/14", "6/14"
        self.p_yes_dec, self.p_no_dec = 0.57, 0.42

        self.table_yes = {
            'Weather': {'Typhoon': '3/8', 'Rainy': '1/8', 'Heat Index': '2/8', 'Earthquake': '2/8'},
            'Intensity': {'High': '5/8', 'Moderate': '3/8', 'Low': '0/8'},
            'Infrastructure': {'High Impact': '3/8', 'Moderate Impact': '4/8', 'Low Impact': '1/8'},
            'Public Health Risk': {'High': '5/8', 'Moderate': '3/8', 'Low': '0/8'}
        }

        self.table_no = {
            'Weather': {'Typhoon': '1/6', 'Rainy': '3/6', 'Heat Index': '2/6', 'Earthquake': '0/6'},
            'Intensity': {'High': '0/6', 'Moderate': '3/6', 'Low': '3/6'},
            'Infrastructure': {'High Impact': '0/6', 'Moderate Impact': '1/6', 'Low Impact': '5/6'},
            'Public Health Risk': {'High': '0/6', 'Moderate': '2/6', 'Low': '4/6'}
        }

    def get_val(self, table, category, feature):
        frac_str = table[category][feature]
        num, den = map(int, frac_str.split('/'))

        # Laplace smoothing
        num += 1
        den += len(table[category])

        return frac_str, num/den

    def solve(self):
        print("--- INPUT DATA ---")

        try:
            w = input("Weather (Typhoon/Rainy/Heat Index/Earthquake): ").title()
            i = input("Intensity (High/Moderate/Low): ").title()
            inf = input("Infra Impact (High/Moderate/Low): ").title() + " Impact"
            h = input("Health Risk (High/Moderate/Low): ").title()

            # YES
            f1y, v1y = self.get_val(self.table_yes, 'Weather', w)
            f2y, v2y = self.get_val(self.table_yes, 'Intensity', i)
            f3y, v3y = self.get_val(self.table_yes, 'Infrastructure', inf)
            f4y, v4y = self.get_val(self.table_yes, 'Public Health Risk', h)

            lik_y = v1y * v2y * v3y * v4y
            res_y = self.p_yes_dec * lik_y

            # NO
            f1n, v1n = self.get_val(self.table_no, 'Weather', w)
            f2n, v2n = self.get_val(self.table_no, 'Intensity', i)
            f3n, v3n = self.get_val(self.table_no, 'Infrastructure', inf)
            f4n, v4n = self.get_val(self.table_no, 'Public Health Risk', h)

            lik_n = v1n * v2n * v3n * v4n
            res_n = self.p_no_dec * lik_n

            print("\n" + "="*50)
            print(f"YES = {res_y:.6f}")
            print(f"NO  = {res_n:.6f}")
            print("="*50)

            if res_y > res_n:
                print("RESULT: SUSPEND CLASS = YES")
            else:
                print("RESULT: SUSPEND CLASS = NO")

        except KeyError:
            print("\n[!] Error: Invalid input.")


nb = NaiveBayesClassifier()
nb.solve()