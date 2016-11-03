with open('hobby.txt') as f:
    for line in f:
        parts = line.split(';')
        hobby = Hobby()
        hobby.name = parts[0]
        hobby.photo = parts[1]
        hobby.description = parts[2]
        hobby.save()
