#https://www.geeksforgeeks.org/hash-map-in-python/
class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    #створюємо порожній список сегментів заданого розміру
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    #вставляє пару ключ-значення в хеш-мапу
    def set_val(self, key, val):

        # за допомогою хеш-функціі одержуємо індекс з ключем
        hashed_key = hash(key) % self.size

        #отримуємо сегмент списка по індексу ключа
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # перевіряємо чи ключ сегмента відповідає ключу, який потрібно вставити
            if record_key == key:
                found_key = True
                break

        # якщо відповідає, то змінюємо значення, якщо не відповідає, добавляємо новий ключ-значення
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    # повертаємо потрібне значення за допомогою ключа
    def get_val(self, key):

        # отримуємо індекс з ключем за допомогою хеш-функціі
        hashed_key = hash(key) % self.size

        # отримуємо комірку, яка відповідає індексу
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # перевіряємо чи ключ сегмента відповідає ключу, який нам потрібно
            if record_key == key:
                found_key = True
                break

        # якщо у нас існує значення, то даному ключу, повертаємо значення, інакше запис не знайдено
        if found_key:
            return record_val
        else:
            return "No record found"

    #  видалення значення за ключем
    def delete_val(self, key):

        # отримуємо індекс з ключем, використовуючи хеш-функцію
        hashed_key = hash(key) % self.size

        # отримуємо комірку, яка відповідає індексу
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # перевіряємо чи комірка має той самий ключ, по якою ми маємо видалити значення
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # Виведення елементів хеш-мапи
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)



if __name__ == "__main__":
    hash_table = HashTable(50)

    # вставлення деяких значень
    hash_table.set_val('gfg@example.com', 'some value')
    print(hash_table)
    print()

    hash_table.set_val('portal@example.com', 'some other value')
    print(hash_table)
    print()

    # пошук/доступ до запису за допомогою ключа
    print(hash_table.get_val('portal@example.com'))
    print()

    # видалення значення
    hash_table.delete_val('portal@example.com')
    print(hash_table)
