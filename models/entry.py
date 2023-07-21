class Entry:
    '''
    Entry class representing the "Entries" table in the database.
    '''
    def __init__(self, id, concept, entry, mood_id, date):
        self.id = id
        self.concept = concept
        self.entry = entry
        self.mood_id = mood_id
        self.date = date
