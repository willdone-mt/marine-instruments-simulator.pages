# Coding Conventions

- Consider the people who will read your code, and make it look nice for them. It's sort of like driving a car: Perhaps you love doing donuts when you're alone, but with passengers the goal is to make the ride as smooth as possible.

- some youtube tips i found ...

# Reusability

Pattern and Repeating Codes

- always define and declare functions and variables after imports. if cant, put it exactly above the code that used it for readability.

- Put codes that repeatingly found in most files in their own files, then import it.

# Readability

- the general order for coding is:
    1. imports
    2. defining and declaring
    3. main codes
    
    mean while debugging codes can be everywhere
    
- We ALWAYS put spaces after list items and method parameters (`[1, 2, 3]`, not `[1,2,3]`), around operators (`x += 1`, not `x+=1`), and around hash arrows.

# Encouraged Aestethic
This is done because the main designer of this project arent so educated in coding.

- we put an empty line between rows with different indent
    ```python
    a line of codes
                                       # <- empty/blank line
        different indent line of codes
        same indent line of codes

            another different indent
    ```

- We put comments to group rows of code with a same topic, like headings, and place a blank line above it. comments for grouping doesnt follow the code's indentations. 
    ```python
    # TOPIC TITLE =====
    rows of codes with same topic
    rows of codes with same topic

    # subtopic title
        rows of codes with same topic
    # =====

    # TOPIC TITLE =====
    rows of codes with different topic

        rows of codes with different topic
    # =====
    ```
    Topic are an obligated to write, meanwhile subtopic are not if the codes are clear enough

- non-grouping comments always once indented than the commented row of code
    ```python
        # Hello World!
    a line of codes

        different indent line of codes
        same indent line of codes
            # this should fix the issue!

                # This is neat!
            another different indent
    ```

