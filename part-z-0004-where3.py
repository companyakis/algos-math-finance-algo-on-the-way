cost_and_sales = np.array([-500, 65, 24, 46, 87, 87, 65, 112, 98, 100, 61, 77])

print(np.where(cost_and_sales.cumsum() > 0, "Yes, sales exceeds initial cost.", "Not yet!" ))

# ['Not yet!' 'Not yet!' 'Not yet!' 'Not yet!' 'Not yet!' 'Not yet!'
#  'Not yet!' 'Not yet!' 'Yes, sales exceeds initial cost.'
#  'Yes, sales exceeds initial cost.' 'Yes, sales exceeds initial cost.'
#  'Yes, sales exceeds initial cost.']
