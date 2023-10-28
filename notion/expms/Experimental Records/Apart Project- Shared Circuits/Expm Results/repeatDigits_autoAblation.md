# repeatDigits_autoAblation

[repeatDigits_autoAblation.ipynb](https://colab.research.google.com/drive/1CK6-kvazMUCH-8aVFQ-GA3IYX1g5MBUp#scrollTo=BBb8m1bIqMup)

doesn’t have 9.1 (which isn’t our main focus anyways; we don’t want 9.1 in all circs)

data_list = [(0, 1), (0, 2), (0, 3), (0, 5), (0, 7), (0, 9), (1, 0), (1, 5), (1, 7), (2, 2), (2, 9), (3, 6), (3, 7), (3, 9), (5, 1), (9, 9), (10, 1), (10, 2), (10, 3), (10, 5), (10, 6), (11, 4), (11, 8)]

This has very few heads in common with IOI. What about “repeating letters?” is it the same?

[repeatLetters_autoAblation.ipynb](https://colab.research.google.com/drive/1qdY3fwH17OP7bAdRL5PK5uqLrmQiGGTr#scrollTo=rIAwX3xfiB3b)

Why would you need anything more than induction heads for “repeating tokens?” Can’t they all use the same circuit? Run a sanity check on “repeat letters”

Note that certain letters like “A” are different from others because they are often followed by a different word such as “A hat”. It’s rarer to have “B hat”.

This removes 9.9.

Actually there’s an issue; the “corruptions” are STILL REPEATING! So it’s the exact same data samples in both clean and corrupted datasets, meaning they have almost the same distributions and mean. 

Instead, you should corrupt using sequences instead of repeating.

NOTE: The clean and corrupted prompt lists (size of dataset) MUST be the same size for the activations to replace; this is due to batch size being the first dim of z (actv vector) and means vector. Batch size is init using the dataset size.

There’s no 9.9 in letters.

Compare letters sequence with “Adam Bob Claire”… Are there overlaps in circuit?