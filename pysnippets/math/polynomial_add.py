class Polynomial:
    def __init__(self, terms=None):
        self.terms = terms if terms is not None else []

    def add_term(self, coeff, exp):
        self.terms.append({'coeff': coeff, 'exp': exp})

    def display(self):
        result = ""
        for i, term in enumerate(self.terms):
            coeff = term['coeff']
            exp = term['exp']
            if coeff != 0:
                if i > 0 and coeff > 0:
                    result += " + "
                if exp == 0:
                    result += f"{coeff}"
                elif exp == 1:
                    result += f"{coeff}x"
                else:
                    result += f"{coeff}x^{exp}"
        return result if result else "0"

def merge_terms(terms):
    merged_terms = {}
    for term in terms:
        exp = term['exp']
        coeff = term['coeff']
        if exp in merged_terms:
            merged_terms[exp] += coeff
        else:
            merged_terms[exp] = coeff
    return [{'coeff': coeff, 'exp': exp} for exp, coeff in merged_terms.items()]

def add_polynomials(polynomials):
    all_terms = []
    for poly in polynomials:
        all_terms.extend(poly.terms)
    merged_terms = merge_terms(all_terms)
    merged_terms.sort(key=lambda x: x['exp'], reverse=True)
    return Polynomial(merged_terms)

