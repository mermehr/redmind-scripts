def rep_list(items):
    # Handles an empty list
    if not items:
        return ''
    # Returns the only item (e.g., ['apples'] → 'apples')
    elif len(items) == 1:
        return items[0]
    # Joins everything up to the last item, then adds 'and <last item>'
    else:
        return ', '.join(items[:-1]) + '. and ' + items[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']

print(rep_list(spam))
print(rep_list([]))