def mapper(key, value):
    if 'invalid user' in value:
        yield value.split(':')[0], 1

def reducer(key, values):
    yield key, sum(values)

if __name__ == '__main__':
    import dumbo
    dumbo.run(mapper, reducer)
