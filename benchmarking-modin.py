import modin.pandas as md
import time
import random
import pandas as pd
import cProfile


filename = 'large_file.csv'

print('reading data into Pandas dataframe')
df = pd.read_csv(filename)
print(df.head())

print('reading data into Modin dataframe')
mdf = md.read_csv(filename)
print(mdf.head())

def benchmark(function, df):
    start = time.time()
    function(df)
    end = time.time()
    print("{} seconds for '{}' '{}'".format((end - start), df.__module__.split('.')[0], function.__name__))


# def add_bonus(df):
#     df['bonus'] = df['salary'] * 0.2


# # #### simple test for adding new column 

# benchmark(add_bonus, mdf)
# benchmark(add_bonus, df)


print('large DataFrame shape:', df.shape)
print('large Modin DataFrame shape:', mdf.shape)


def get_mean(df):
    x = df.salary.mean()
    return x

def get_max(df):
    x = df.salary.max()
    return x

def get_sum(df):
    x = df.salary.sum()
    return x

def filter_test(df):
    x = df[df['salary']>5000]
    return x

def run_benchmarks():
    for i,f in enumerate([
#                           add_bonus,
                          get_mean,
                          get_max,
                          get_sum,
                          filter_test
                         ]):
        benchmark(f, mdf)
        benchmark(f, df)
                          

def f(x):
    return (13*x+5)%7

def apply_func(df):
    df['random']= df['salary'].apply(f)
    
def value_count(df):
    x = df.salary.value_counts()
    return x

print('running benchmarks()')
cProfile.run('run_benchmarks()')


# benchmark(apply_func, mdf)
# benchmark(apply_func, df)
# benchmark(value_count, mdf)
# benchmark(value_count, df)


# mdf.salary.value_counts()

# print(df.salary.value_counts())


