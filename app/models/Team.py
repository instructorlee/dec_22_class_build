from app.models.character import Character

class Team:

    members = [
    ]

    @classmethod
    def add_member(cls, member_data):
        member_data['id'] = len(cls.members) + 1 # create an ID
        cls.members.append(member_data)

    @classmethod
    def save_member(cls, member_data):
        cls.members = [member_data if data['id'] == member_data['id'] else data for data in cls.members] # list comprehension

    @classmethod
    def get_member(cls, id):
        found_member = None
        
        for member in cls.members:
            if member['id'] == id:
                found_member = member

        return found_member

    @classmethod
    def delete_member(cls, id):
        
        start_length = len(cls.members)
        cls.members = [member for member in cls.members if member['id'] != id]

        return start_length != len(cls.members) # do not do this the first time through. Save it for extra functionality

