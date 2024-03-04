from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
from flask_app.models import user

class Photospot:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.location = data['location']
        self.description = data['description']
        self.direct_sunlight = data['direct_sunlight']
        self.bathroom_avail = data['bathroom_avail']
        self.created_at = data['created_at']
        self.updated_at = data ['updated_at']
        self.host_id = data['user_id']
        self.host = None

    #create photospot
    @classmethod
    def create_photospot(cls,data):
        if not cls.validate_photospot(data):
            return False 
        query = """
            INSERT INTO photo_spot
            (title, location, description, direct_sunlight, bathroom_avail, user_id)
            VALUES 
            (%(title)s, %(location)s, %(description)s, %(direct_sunlight)s, %(bathroom_avail)s,%(user_id)s)
            ;"""
        return connectToMySQL('snapspot').query_db(query, data)

    #read photospot
    @classmethod
    def get_all_photospots_with_host(cls):
        query = """
            SELECT * FROM photo_spot
            JOIN users
            ON users.id = photo_spot.user_id
            ;"""
        results = connectToMySQL('snapspot').query_db(query)
        photospots = []
        for photospots_data in results:
            this_spot = cls(photospots_data)
            this_spot.host = user.User.parse_user(photospots_data)
            photospots.append(this_spot)
        return photospots
    
    @classmethod
    def get_photospot_by_id_w_host(cls,id):
        data = {'id': id }
        query = """
            SELECT * FROM photo_spot
            JOIN users
            ON users.id = photo_spot.user_id
            WHERE photo_spot.id = %(id)s
            ;"""
        result = connectToMySQL('snapspot').query_db(query,data)
        this_photospot = cls(result[0])
        this_photospot.host = user.User.parse_user(result[0])
        return this_photospot
    
    #update photospot
    @classmethod
    def edit_photospot(cls,data):
        if not cls.validate_photospot(data): 
            return False
        query = """
            UPDATE photo_spot
            SET
                title = %(title)s,
                location = %(location)s,
                description = %(description)s,
                direct_sunlight = %(direct_sunlight)s,
                bathroom_avail = %(bathroom_avail)s
            WHERE id = %(id)s
            ;"""
        connectToMySQL('snapspot').query_db(query,data)
        return True
    
    #delete photospot 
    @classmethod
    def delete_photospot(cls,id):
        data = {'id': id}
        query = """
            DELETE FROM photo_spot
            WHERE id = %(id)s
            ;"""
        return connectToMySQL('snapspot').query_db(query, data)
    
    #validations 
    @classmethod
    def validate_photospot(cls,data):
        is_valid = True 
        if len(data['title']) < 6:
            flash("Title must be at least 6 characters.","create_photospot")
            is_valid = False 
        if len(data['location']) < 8:
            flash("Location must be at least 8 characters.","create_photospot")
            is_valid = False 
        if len(data['description']) < 1:
            flash("Description is required ","create_photospot")
            is_valid = False
        if "direct_sunlight" not in data:
            flash("Please select Yes or No for Direct Sunlight.","create_photospot")
            is_valid = False 
        if "bathroom_avail" not in data:
            flash("Please select Yes or No for Bathrooms Available.","create_photospot")
            is_valid = False 
        return is_valid 