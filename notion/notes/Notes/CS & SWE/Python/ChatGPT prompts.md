# ChatGPT prompts

- in python, from a list of a strings , select 4 random items that aren't repeated and store it in a list. store the list ina a list of lists. make sure each list in the stored lists is also not repeated. the order of each string in the list doesn't matter (combinations not permutations)
    
    You can use the `random.sample()` function from the Python `random` module to select random items from a list without repetition. To ensure that each list of strings is not repeated, you can keep track of the generated lists using a set. Here's an example implementation that meets your requirements:
    
    ```
    import random
    
    def generate_random_lists(strings, num_lists, num_items):
        result = []
        used_lists = set()
    
        while len(result) < num_lists:
            items = random.sample(strings, num_items)
            items_set = frozenset(items)
    
            if items_set not in used_lists:
                result.append(items)
                used_lists.add(items_set)
    
        return result
    
    # Example usage
    strings = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    num_lists = 5
    num_items = 4
    
    random_lists = generate_random_lists(strings, num_lists, num_items)
    for lst in random_lists:
        print(lst)
    
    ```
    
    In this example, the `generate_random_lists()` function takes the `strings` list, the desired number of lists (`num_lists`), and the desired number of items per list (`num_items`) as input. It returns a list of lists, where each inner list contains four randomly selected non-repeated items from the `strings` list.
    
    The function uses a `while` loop to generate the required number of lists. It selects a sample of `num_items` items using `random.sample()` and converts it into a frozenset. This frozenset is then checked against the `used_lists` set to ensure uniqueness. If the frozenset is not in the set, the list is added to the `result` list, and the frozenset is added to the `used_lists` set.
    
    Note that the `random.sample()` function raises a `ValueError` if the `num_items` parameter is larger than the size of the input list. Make sure to handle such cases appropriately if needed.