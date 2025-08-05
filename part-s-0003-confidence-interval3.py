import statsmodels.stats.api as sms

print(sms.DescrStatsW(price_expectations).tconfint_mean())

# (np.float64(74.27627428961813), np.float64(75.07692571038186))

