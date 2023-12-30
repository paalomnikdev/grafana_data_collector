from pprint import pprint as pp

country = {'AE': 11,
 'AL': 2,
 'AR': 5,
 'AT': 63,
 'AU': 48,
 'BA': 3,
 'BD': 1,
 'BE': 56,
 'BG': 57,
 'BH': 14,
 'BR': 3,
 'CA': 392,
 'CH': 49,
 'CL': 1,
 'CN': 6,
 'CR': 2,
 'CY': 2,
 'CZ': 71,
 'DE': 261,
 'DK': 24,
 'EE': 5,
 'ES': 98,
 'FI': 33,
 'FR': 34,
 'GB': 555,
 'GE': 1,
 'GR': 12,
 'HK': 21,
 'HR': 1,
 'HU': 20,
 'ID': 10,
 'IE': 14,
 'IL': 4,
 'IN': 31,
 'IS': 1,
 'IT': 74,
 'JP': 17,
 'KH': 1,
 'KR': 37,
 'KW': 3,
 'LB': 1,
 'LK': 1,
 'LT': 34,
 'LU': 3,
 'LV': 4,
 'ME': 2,
 'MK': 18,
 'MM': 1,
 'MN': 7,
 'MT': 2,
 'MX': 13,
 'MY': 10,
 'NL': 406,
 'NO': 69,
 'NZ': 14,
 'OM': 6,
 'PA': 5,
 'PH': 10,
 'PL': 95,
 'PR': 5,
 'PT': 35,
 'PY': 2,
 'QA': 3,
 'RO': 47,
 'RS': 34,
 'RU': 30,
 'SA': 8,
 'SE': 214,
 'SG': 37,
 'SI': 19,
 'SK': 47,
 'SN': 1,
 'SO': 1,
 'TH': 20,
 'TR': 16,
 'TW': 29,
 'TZ': 3,
 'UA': 20,
 'US': 1481,
 'VE': 3,
 'VN': 2,
 'ZA': 14}

pp([(c, country[c]) for c in country])