import os
import timeit

from kmp import kmp_search
from boyer_moore import boyer_moore_search
from rabin_karp import rabin_karp_search

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def time_search_algorithm(algorithm, text, pattern, iterations=10):
    return timeit.timeit(lambda: algorithm(text, pattern), number=iterations)

def main():
    current_directory = os.getcwd()
    files_directory = os.path.join(current_directory, 'files')
    article_1 = read_file(os.path.join(files_directory, 'file_1.txt'))
    article_2 = read_file(os.path.join(files_directory, 'file_2.txt'))
    pattern_1 = 'деякі реалізації'
    pattern_2 = 'Hello world'

    # Timing the KMP search
    kmp_time_1 = time_search_algorithm(kmp_search, article_1, pattern_1)
    kmp_time_2 = time_search_algorithm(kmp_search, article_2, pattern_2)

    # Timing the Boyer-Moore search
    bm_time_1 = time_search_algorithm(boyer_moore_search, article_1, pattern_1)
    bm_time_2 = time_search_algorithm(boyer_moore_search, article_2, pattern_2)

    # Timing the Rabin-Karp search
    rk_time_1 = time_search_algorithm(rabin_karp_search, article_1, pattern_1)
    rk_time_2 = time_search_algorithm(rabin_karp_search, article_2, pattern_2)

    print(f"KMP search times: {kmp_time_1}s, {kmp_time_2}s")
    print(f"Boyer-Moore search times: {bm_time_1}s, {bm_time_2}s")
    print(f"Rabin-Karp search times: {rk_time_1}s, {rk_time_2}s")

if __name__ == '__main__':
    main()
