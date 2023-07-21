class EntryTag:
    '''
    EntryTag class representing the "Entry_tags" table in the database.
    '''
    def __init__(self, id, tag_id, entry_id):
        self.id = id
        self.tag_id = tag_id
        self.entry_id = entry_id
