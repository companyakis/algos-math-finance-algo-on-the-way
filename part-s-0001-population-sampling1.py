import numpy as np

np.random.seed(2025)

# min - max salary USD, 10000 people

salary_data = np.random.randint(2000, 8000, 10000)

print(salary_data[: 5])

# salary data of 100 people

salary_sampling_data1 = np.random.choice(salary_data, 100)

salary_sampling_data2 = np.random.choice(salary_data, 100)

salary_sampling_data3 = np.random.choice(salary_data, 100)

print(f"Population salary mean: {np.mean(salary_data)}")

print(f"Sample 1 salary mean: {np.mean(salary_sampling_data1)}")

print(f"Sample 2 salary mean: {np.mean(salary_sampling_data2)}")

print(f"Sample 3 salary mean: {np.mean(salary_sampling_data3)}")

print(f"Samples avearge salary: {(np.mean(salary_sampling_data1) + np.mean(salary_sampling_data2) + np.mean(salary_sampling_data3)) / 3}")

"""
[4910 2323 7331 3932 6256]
Population salary mean: 5023.3901
Sample 1 salary mean: 4928.47
Sample 2 salary mean: 5376.74
Sample 3 salary mean: 4940.98
Samples avearge salary: 5082.063333333333

"""
