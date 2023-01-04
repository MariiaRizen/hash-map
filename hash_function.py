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

        # генеруємо хеш у нашій таблиці
        hashed_key = hash(key) % self.size

        # отримуємо рядок хеш-таблиці по індексу ключа
        bucket = self.hash_table[hashed_key]

        found_key = False
        # перевіряємо чи існує запис з таким ключем
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            # оновлюємо значення, якщо запис з ключем уже існує
            bucket[index] = (key, val)
        else:
            # добавляємо значення, якщо не існує
            bucket.append((key, val))

    # повертаємо потрібне значення за допомогою ключа
    def get_val(self, key):

        # генеруємо хеш у нашій таблиці
        hashed_key = hash(key) % self.size

        # отримуємо рядок хеш-таблиці по хешу
        bucket = self.hash_table[hashed_key]

        found_key = False
        # перевіряємо чи існує запис з таким ключем
        for index, record in enumerate(bucket):
            record_key, record_val = record

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

        # генеруємо хеш у нашій таблиці
        hashed_key = hash(key) % self.size

        # отримуємо рядок хеш-таблиці по хешу
        bucket = self.hash_table[hashed_key]

        found_key = False
        # перевіряємо чи існує запис з таким ключем
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        # якщо у нас існує значення, по даному ключу, то видаляємо його
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
