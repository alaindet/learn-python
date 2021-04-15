class Database():

    def __init__(self, connection):
        self.connection = connection

    def execute(self, prepared_statement, bindings={}):
        """
        TODO:
        - Use context manager for cursor?
        """
        cursor = self.connection.connection.cursor()
        cursor.execute(prepared_statement, self._convert_bindings(bindings))
        self.connection.connection.commit()
        last_id = cursor.lastrowid
        cursor.close()
        return last_id

    def fetch(self, prepared_statement, bindings={}):
        cursor = self.connection.connection.cursor()
        cursor.execute(prepared_statement, self._convert_bindings(bindings))
        self.connection.connection.commit()
        result = cursor.fetchall()
        cursor.close()
        return result

    def insert(self, table, bindings={}):
        """
        Example:
        db.insert('books', {
            'name': 'Some book name',
            'author': 'Some book author',
            'read': False,
        })
        """
        fields = ', '.join(bindings)
        render = lambda key: f':{key}'
        placeholders = ', '.join([render(key) for key in bindings])
        statement = f'INSERT INTO {table} ({fields}) VALUES ({placeholders})'
        return self.execute(statement, bindings)

    def select(self, table, fields='*', where='TRUE', bindings={}):
        """
        TODO:
        - Does not allow LIMIT, OFFSET and GROUP BY clauses

        Example:
        result = db.select(
            'books',
            '*',
            [ 'name = :name' ],
            { ':name': 'Some book name' }
        )
        """
        where_clause = self._parse_where_clause(where)
        statement = f'SELECT {fields} FROM {table} WHERE {where_clause}'
        return self.fetch(statement, bindings)

    def update(self, table, assignments={}, where='TRUE', bindings={}):
        """
        Example:
        db.update(
            'books',
            {
                'name': ':name',
                'author': ':author',
                'read': ':read',
            },
            'id = :id',
            {
                ':id':'2,
                ':name': 'Some updated book name',
                ':author': 'Some updated book author',
                ':read': True,
            }
        )
        """
        render = lambda key: f'{key} = :{key}'
        set_clause = ', '.join([render(key) for key in assignments])
        where_clause = self._parse_where_clause(where)
        statement = f'UPDATE {table} SET {set_clause} WHERE {where_clause}'
        self.execute(statement, bindings)

    def delete(self, table, where='TRUE', bindings={}):
        """
        Example:
        db.delete('books', 'id = :id', {':id': 1})
        """
        where_clause = self._parse_where_clause(where)
        statement = f'DELETE from {table} WHERE {where_clause}'
        self.execute(statement, bindings)

    def _parse_where_clause(self, where):
        conditions = where if isinstance(where, list) else [where]
        return ' AND '.join(conditions)

    def _convert_bindings(self, bindings={}):
        converted = {}

        for key in bindings:

            new_key = key[1:] if key.startswith(':') else key

            # Cast booleans to integers
            if isinstance(bindings[key], bool):
                converted[new_key] = int(bindings[key])
                continue

            # Default
            converted[new_key] = bindings[key]

        return converted
